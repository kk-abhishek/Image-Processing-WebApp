import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageEnhance
from io import BytesIO
from urllib.parse import urlparse
import time
import requests

# Function to adjust brightness and contrast
def adjust_brightness_contrast(image, alpha=1.2, beta=30):
    return cv2.addWeighted(image, alpha, image, 0, beta)

# Function to sharpen the image
def sharpen_image(image):
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    return cv2.filter2D(image, -1, kernel)

# Function to adjust contrast
def adjust_contrast(image, factor=1.5):
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    enhancer = ImageEnhance.Contrast(pil_image)
    enhanced_image = enhancer.enhance(factor)
    return cv2.cvtColor(np.array(enhanced_image), cv2.COLOR_RGB2BGR)

# Image Upscaling using Bicubic Interpolation
def upscale_image(image, scale_factor):
    height, width = image.shape[:2]
    new_dimensions = (int(width * scale_factor), int(height * scale_factor))
    return cv2.resize(image, new_dimensions, interpolation=cv2.INTER_CUBIC)

# High-quality image enhancement
def high_quality_enhancement(image):
    upscaled_image = upscale_image(image, scale_factor=2)  # 2x upscale
    sharpened_image = sharpen_image(upscaled_image)
    return cv2.bilateralFilter(sharpened_image, d=9, sigmaColor=75, sigmaSpace=75)

# Helper function to check if path is a URL
def is_url(path):
    return urlparse(path).scheme in ("http", "https")

# Convert image to bytes for downloading
def convert_to_bytes(image):
    if isinstance(image, np.ndarray):
        if image.shape[-1] == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
    elif isinstance(image, Image.Image):
        image = image.convert("RGB")
    else:
        raise ValueError("Unsupported image format.")
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer.getvalue()

# Main application logic
st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

# Sidebar setup
st.sidebar.title("Image Input Options")
uploaded_file = st.sidebar.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
url_input = st.sidebar.text_input("Enter an image URL")
image = None

# Load image from file or URL
if uploaded_file:
    image = cv2.cvtColor(np.array(Image.open(uploaded_file)), cv2.COLOR_RGB2BGR)
elif url_input:
    try:
        response = requests.get(url_input)
        response.raise_for_status()
        image = np.array(Image.open(BytesIO(response.content)))
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    except Exception as e:
        st.sidebar.error(f"Failed to load image from URL: {e}")

# Image enhancement buttons and display
if image is not None:
    st.subheader("Image Enhancement Options")
    col1, col2, col3, col4 = st.columns(4)
    enhanced_image = None

    with col1:
        if st.button(" ✨ Enhance Quality"):
            enhanced_image = high_quality_enhancement(image)
    with col2:
        if st.button(" 🌗 Adjust Contrast"):
            enhanced_image = adjust_contrast(image)
    with col3:
        if st.button(" 🔆 Adj Brightness"):
            enhanced_image = adjust_brightness_contrast(image)
    with col4:
        if st.button(" ⚔️ Sharpen Image"):
            enhanced_image = sharpen_image(image)

    st.subheader("Original Image")
    st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="Original Image", use_container_width=True)

    if enhanced_image is not None:
        st.subheader("Enhanced Image")
        st.image(cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB), caption="Enhanced Image", use_container_width=True)
