import streamlit as st
import serial
import time
# from h6.zoom_h6 import ZoomH6  # assuming H6Recorder is your control class
from h6 import ZoomH6 

# Initialize serial connection (adjust to your port)
serial_port = '/dev/ttyUSB0'
# Instantiate recorder
recorder = ZoomH6(serial_port)

# Initialize recorders
recorder.initialize()
# App state
st.set_page_config(layout="wide")
st.title("Zoom H6 Controller")

# Track selection and peak detection simulation
st.subheader("Channel Selection and Signal Indicator")
selected_channel = st.radio("Select Channel", options=[1, 2, 3, 4], horizontal=True)

# Simulate peak levels (replace with actual level data from h6 lib if available)
def get_peak_level(channel):
    # Simulated peak level (replace with actual H6 response if supported)
    import random
    level = random.randint(0, 100)
    return level

col1, col2, col3, col4 = st.columns(4)
for i, col in enumerate([col1, col2, col3, col4], start=1):
    with col:
        peak = get_peak_level(i)
        color = "white"
        if selected_channel == i:
            color = "green"
        if peak > 80:
            color = "red"
        st.markdown(f'<div style="width:50px;height:50px;background:{color};border-radius:5px;text-align:center;line-height:50px;">{i}</div>', unsafe_allow_html=True)

# Controls
st.subheader("Recording Control")
col_rec, col_stop, col_pause = st.columns(3)

with col_rec:
    if st.button("🔴 Record"):
        recorder.record()
        st.success("Recording...")

with col_stop:
    if st.button("⏹ Stop"):
        recorder.stop()
        st.warning("Stopped")

with col_pause:
    if st.button("⏸ Pause"):
        recorder.pause()
        st.info("Paused")

# Volume control
st.subheader("Volume Sliders")
volumes = {}
for i in range(1, 5):
    volumes[i] = st.slider(f"Mic {i} Volume", min_value=0, max_value=100, value=50, key=f"vol_{i}")

if st.button("Set Volumes"):
    for ch, vol in volumes.items():
        recorder.set_volume(ch, vol)
    st.success("Volume levels updated")

