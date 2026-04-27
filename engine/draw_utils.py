import cv2

def draw_person(frame, box, track_id):
    x1,y1,x2,y2 = box
    cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
    cv2.putText(frame,f"ID {track_id}",(x1,y1-10),
                cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)

def draw_weapon(frame, box):
    x1,y1,x2,y2 = box
    cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)
    cv2.putText(frame,"Weapon",(x1,y1-10),
                cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)

def draw_alert(frame, msg):
    cv2.rectangle(frame,(0,0),(frame.shape[1],40),(0,0,0),-1)
    cv2.putText(frame,msg,(10,28),
                cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,255),2)

def draw_time(frame, sec):
    mins = int(sec//60)
    secs = int(sec%60)
    txt = f"{mins:02d}:{secs:02d}"
    cv2.putText(frame,txt,(frame.shape[1]-100,30),
                cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)