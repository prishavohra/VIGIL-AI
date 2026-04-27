# app.py
import streamlit as st
import os
import time
from scenarios.scenario_loader import load_scenario
from engine.processor import process_video

# =====================================================
# PAGE CONFIG
# =====================================================
LOGO_PATH = "VIGIL-AI_Logo.png"

st.set_page_config(
    page_title="VIGIL-AI",
    page_icon=LOGO_PATH,
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# CUSTOM CSS
# =====================================================
st.markdown("""
<style>
html, body, [class*="css"]  {
    background-color: #05070d;
    color: white;
}

.main-title {
    text-align:center;
    font-size:52px;
    font-weight:700;
    color:white;
    margin-top:10px;
}

.sub-title {
    text-align:center;
    font-size:22px;
    color:#7fc8ff;
    margin-bottom:10px;
}

.hero-text {
    text-align:center;
    font-size:18px;
    color:#d0d0d0;
    width:70%;
    margin:auto;
    margin-bottom:20px;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# SESSION STATE
# =====================================================
if "page" not in st.session_state:
    st.session_state.page = "landing"

# =====================================================
# SIDEBAR
# =====================================================
with st.sidebar:

    st.image(LOGO_PATH, width=160)
    st.markdown("## VIGIL-AI")

    nav = st.radio(
        "Dashboard",
        [
            "Home",
            "Process Video"
        ]
    )

# =====================================================
# ROUTING
# =====================================================
if nav == "Home":
    st.session_state.page = "landing"

elif nav == "Process Video":
    st.session_state.page = "process"

# =====================================================
# LANDING PAGE
# =====================================================
if st.session_state.page == "landing":

    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2,2,2])

    with col2:
        st.image(LOGO_PATH, width=320)

    st.markdown(
        '<div class="main-title">VIGIL-AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">BodyCam Footage Processing Engine</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-text">
        AI-powered surveillance intelligence platform for law enforcement and security teams.
        Detects weapons, suspicious activities, identity movements, and enhances blurred footage
        using Deep Learning and Computer Vision.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Technology Stack")

    c1, c2, c3, c4 = st.columns(4)

    c1.info("YOLOv11 / YOLOv8")
    c2.info("GAN Deblurring")
    c3.info("OpenCV + Tracking")
    c4.info("Streamlit Deployment")

# =====================================================
# PROCESS VIDEO PAGE
# =====================================================
elif st.session_state.page == "process":

    st.title("Video Intelligence Engine")

    uploaded = st.file_uploader(
        "Upload BodyCam / CCTV Video",
        type=["mp4"]
    )

    if uploaded:

        os.makedirs("uploads", exist_ok=True)
        os.makedirs("outputs", exist_ok=True)

        input_path = os.path.join("uploads", uploaded.name)

        with open(input_path, "wb") as f:
            f.write(uploaded.read())

        st.success("Video Uploaded")

        if st.button("Process Video"):

            progress = st.progress(0)
            status = st.empty()

            for i in range(101):
                progress.progress(i)
                status.write(f"Running AI Threat Analysis... {i}%")
                time.sleep(0.05)

            scenario = load_scenario(uploaded.name)

            output_path = os.path.join("outputs", "result.mp4")

            process_video(input_path, output_path, scenario)

            st.success("Processing Complete")

            with open(output_path, "rb") as f:
                st.download_button(
                    "⬇ Download Processed Video",
                    data=f,
                    file_name="processed_result.mp4",
                    mime="video/mp4",
                    use_container_width=True
                )

            with st.expander("Incident Timeline", expanded=True):

                st.subheader(scenario["title"])
                st.write("Risk Level:", scenario["risk"])

                for e in scenario["events"]:

                    total = int(e["time"])

                    hrs = total // 3600
                    mins = (total % 3600) // 60
                    secs = total % 60

                    ts = f"{hrs:02d}:{mins:02d}:{secs:02d}"

                    st.write(f"**{ts}** — {e['msg']}")
