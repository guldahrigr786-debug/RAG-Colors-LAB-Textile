import streamlit as st
import numpy as np
from skimage.color import lab2rgb

st.set_page_config(
    page_title="RGB & LAB Color Generator",
    page_icon="🎨",
    layout="centered"
)

st.title("🎨 RGB & LAB Color Generator")
st.subheader("Textile Engineering Color Application")
st.write("Roll No: 25TE051")

st.divider()

# Primary RGB Colors
st.header("1. Primary RGB Colors")

rgb_color = st.selectbox(
    "Select Primary RGB Color",
    ["Red", "Green", "Blue"]
)

rgb_values = {
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255)
}

r, g, b = rgb_values[rgb_color]

st.write(f"**RGB Values:** R = {r}, G = {g}, B = {b}")

st.markdown(
    f"""
    <div style="
        background-color: rgb({r},{g},{b});
        height: 180px;
        border-radius: 15px;
        border: 2px solid black;
        margin-top: 10px;">
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# LAB Color Generator
st.header("2. LAB Color Generator")
st.write("Change the L*, a* and b* values to generate different colors.")

L = st.slider(
    "L* (Lightness)",
    min_value=0.0,
    max_value=100.0,
    value=50.0,
    step=1.0
)

a = st.slider(
    "a* (Green ↔ Red)",
    min_value=-128.0,
    max_value=127.0,
    value=0.0,
    step=1.0
)

b_lab = st.slider(
    "b* (Blue ↔ Yellow)",
    min_value=-128.0,
    max_value=127.0,
    value=0.0,
    step=1.0
)

lab = np.array([[[L, a, b_lab]]])
rgb = lab2rgb(lab)[0][0]

R = int(round(rgb[0] * 255))
G = int(round(rgb[1] * 255))
B = int(round(rgb[2] * 255))

R = max(0, min(255, R))
G = max(0, min(255, G))
B = max(0, min(255, B))

st.write(f"**LAB Values:** L* = {L}, a* = {a}, b* = {b_lab}")
st.write(f"**Generated RGB:** R = {R}, G = {G}, B = {B}")

st.markdown(
    f"""
    <div style="
        background-color: rgb({R},{G},{B});
        height: 220px;
        border-radius: 15px;
        border: 2px solid black;
        margin-top: 15px;">
    </div>
    """,
    unsafe_allow_html=True
)

st.success("Color generated successfully!")

st.divider()

st.header("3. Color Information")
st.write(
    """
    **RGB:** RGB stands for Red, Green and Blue. It is an additive
    color model commonly used in digital displays.

    **LAB:** CIELAB is a device-independent color space. L* represents
    lightness, a* represents the green-red axis, and b* represents
    the blue-yellow axis.
    """
)

st.caption("Developed for Textile Engineering — Roll No. 25TE051")
