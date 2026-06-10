import streamlit as st
from PIL import Image
import io

from cartoonifier import (
    cartoonify,
    pencil_sketch,
    watercolor
)

st.set_page_config(
    page_title="AI Cartoon Studio",
    layout="wide"
)

st.title("🎨 AI Cartoon Studio")

st.write(
    "Upload an image and transform it into Cartoon, Sketch, or Watercolor style."
)

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

effect = st.selectbox(
    "Choose Effect",
    [
        "Cartoon",
        "Pencil Sketch",
        "Watercolor"
    ]
)

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")

    if effect == "Cartoon":
        result = cartoonify(image)

    elif effect == "Pencil Sketch":
        result = pencil_sketch(image)

    else:
        result = watercolor(image)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("Processed Image")
        st.image(result, use_container_width=True)

    result_image = Image.fromarray(result)

    buffer = io.BytesIO()
    result_image.save(buffer, format="PNG")

    st.download_button(
        label="📥 Download Image",
        data=buffer.getvalue(),
        file_name="processed_image.png",
        mime="image/png"
    )