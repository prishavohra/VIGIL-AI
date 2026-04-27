import cv2
import glob
import os
import re

# =====================================================
# BASE LABEL ROOT
# Example:
# labels_shooting/
# labels_arrest/
# labels_fight/
# =====================================================
BASE_LABEL_PATH = r"C:\Users\Prisha\OneDrive - Vohra Soft\My Laptop 2.0\Uni\Academics\Sem 6\CV\VIGIL-AI\labels"

IMG_W = None
IMG_H = None


# =====================================================
# YOLO NORMALIZED TO PIXEL BOX
# =====================================================
def yolo_to_box(xc, yc, w, h):

    x1 = int((xc - w / 2) * IMG_W)
    y1 = int((yc - h / 2) * IMG_H)
    x2 = int((xc + w / 2) * IMG_W)
    y2 = int((yc + h / 2) * IMG_H)

    return [x1, y1, x2, y2]


# =====================================================
# AUTO LABEL NAME SYSTEM
# Different classes for every video supported
# =====================================================
def get_label_name(cls_id, class_names):

    if cls_id < len(class_names):
        return class_names[cls_id]

    return f"OBJ{cls_id}"


# =====================================================
# DRAW ALERTS
# =====================================================
def draw_alert(frame, msg, y_offset=0):

    height, width = frame.shape[:2]

    msg_clean = msg.replace("🔴", "").replace("⚠️", "").replace("🟡", "").strip()

    color = (255, 0, 0)   # blue default

    if "HIGH RISK" in msg_clean:
        color = (0, 0, 255)

    elif "WEAPON DROP" in msg_clean:
        color = (0, 255, 255)

    elif "SUSPICIOUS ACTIVITY" in msg_clean:
        color = (255, 0, 0)

    font = cv2.FONT_HERSHEY_DUPLEX
    scale = 0.55
    thickness = 1

    text_size = cv2.getTextSize(msg_clean, font, scale, thickness)[0]

    x = (width - text_size[0]) // 2
    y = 30 + y_offset

    cv2.putText(
        frame,
        msg_clean,
        (x, y),
        font,
        scale,
        color,
        thickness,
        cv2.LINE_AA
    )


# =====================================================
# LOAD CLASS NAMES AUTOMATICALLY
# Looks for classes.txt in labels folder
# =====================================================
def load_class_names(label_folder):

    classes_file = os.path.join(label_folder, "classes.txt")

    if os.path.exists(classes_file):

        with open(classes_file, "r") as f:
            names = [x.strip() for x in f.readlines() if x.strip()]

        return names

    # fallback generic labels
    return []


# =====================================================
# MAIN VIDEO PROCESSOR
# =====================================================
def process_video(input_path, output_path, scenario):

    global IMG_W, IMG_H

    filename = os.path.basename(input_path).lower()
    video_name = os.path.splitext(filename)[0]

    # =================================================
    # AUTO LABEL FOLDER
    # Upload arrest.mp4 -> labels_arrest
    # =================================================
    LABEL_FOLDER = os.path.join(BASE_LABEL_PATH, f"labels_{video_name}")

    print("Using labels folder:", LABEL_FOLDER)

    # =================================================
    # LOAD CLASS NAMES
    # =================================================
    class_names = load_class_names(LABEL_FOLDER)

    print("Classes:", class_names)

    # =================================================
    # OPEN VIDEO
    # =================================================
    cap = cv2.VideoCapture(input_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0:
        fps = 30

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    total_video_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    IMG_W = width
    IMG_H = height

    # =================================================
    # OUTPUT
    # =================================================
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    frame_no = 0

    # =================================================
    # LOAD TXT LABEL FILES
    # =================================================
    label_files = glob.glob(
        os.path.join(LABEL_FOLDER, "**", "*.txt"),
        recursive=True
    )

    # remove classes.txt
    label_files = [x for x in label_files if "classes.txt" not in x.lower()]

    def get_frame_num(path):

        name = os.path.basename(path)

        match = re.search(r'frame_(\d+)', name)

        if match:
            return int(match.group(1))

        nums = re.findall(r'\d+', name)

        if nums:
            return int(nums[0])

        return 999999

    label_files = sorted(label_files, key=get_frame_num)

    print("Total labels:", len(label_files))

    # =================================================
    # MAIN LOOP
    # =================================================
    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame_no += 1

        # =============================================
        # MATCH VIDEO FRAMES TO LABEL FRAMES
        # Works for any number of label files
        # =============================================
        if len(label_files) > 0:

            num_labels = len(label_files)

            label_index = int((frame_no - 1) * num_labels / total_video_frames)
            label_index = min(label_index, num_labels - 1)

            file = label_files[label_index]

            with open(file, "r") as f:
                lines = f.readlines()

            for line in lines:

                vals = line.strip().split()

                if len(vals) < 5:
                    continue

                cls = int(vals[0])

                xc = float(vals[1])
                yc = float(vals[2])
                w = float(vals[3])
                h = float(vals[4])

                x1, y1, x2, y2 = yolo_to_box(xc, yc, w, h)

                label = get_label_name(cls, class_names)

                # =====================================
                # WEAPON DETECTION
                # =====================================
                if "weapon" in label.lower() or "gun" in label.lower() or "knife" in label.lower():

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 1)

                    cv2.putText(
                        frame,
                        label.upper(),
                        (x1, max(20, y1 - 6)),
                        cv2.FONT_HERSHEY_DUPLEX,
                        0.75,
                        (0, 0, 255),
                        1,
                        cv2.LINE_AA
                    )

                # =====================================
                # PERSON / OTHER IDS
                # =====================================
                else:

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)

                    cv2.putText(
                        frame,
                        label,
                        (x1, max(20, y1 - 6)),
                        cv2.FONT_HERSHEY_DUPLEX,
                        0.75,
                        (0, 255, 0),
                        1,
                        cv2.LINE_AA
                    )

        # =================================================
        # TIMESTAMP
        # =================================================
        sec = int(frame_no / fps)

        hrs = sec // 3600
        mins = (sec % 3600) // 60
        secs = sec % 60

        timestamp = f"{hrs:02d}:{mins:02d}:{secs:02d}"

        cv2.putText(
            frame,
            timestamp,
            (width - 135, 25),
            cv2.FONT_HERSHEY_DUPLEX,
            0.55,
            (255, 255, 255),
            1,
            cv2.LINE_AA
        )

        # =================================================
        # EVENTS
        # =================================================
        current_alerts = []

        for e in scenario["events"]:
            if sec == e["time"]:
                current_alerts.append(e["msg"])

        for i, msg in enumerate(current_alerts):
            draw_alert(frame, msg, y_offset=i * 28)

        out.write(frame)

    cap.release()
    out.release()

    print("✅ Processing complete:", output_path)