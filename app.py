import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageEnhance
import requests
from io import BytesIO
from urllib.parse import urlparse
import time
from PIL import Image

# Function to adjust brightness and contrast
def adjust_brightness_contrast(image, alpha=1.2, beta=30):
    return cv2.addWeighted(image, alpha, image, 0, beta)

# Function to sharpen the image
def sharpen_image(image):
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
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


# Set page configuration
st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

# CSS styling
# with open('style.css') as f:
#    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Updated CSS for hover and click effects
st.markdown("""
    <style>
        /* Button Base Styling */
        .stButton>button {
            padding: 15px 40px;
            border: none;
            outline: none;
            color: #f8f2f2;
            cursor: pointer;
            position: relative;
            z-index: 0;
            border-radius: 12px;
            background-color: #000916; /* Default button color */
            
        }

        /* Dark Background Layer */
        .stButton>button::after {
            content: "";
            z-index: -1;
            position: absolute;
            width: 100%;
            height: 100%;
            background-color: #1a2129;
            left: 0;
            top: 0;
            border-radius: 40px;
        }

        /* Glow Effect */
        .stButton>button::before {
            content: "";
            background: linear-gradient(
                45deg,
                #620e9a, #00FFD5, #002BFF, #FF00C8, #000000,
                #620e9a, #00FFD5, #002BFF, #FF00C8, #ffffff
            );
            position: absolute;
            top: -2px;
            left: -2px;
            background-size: 600%;
            z-index: -1;
            width: calc(100% + 4px);
            height: calc(100% + 4px);
            filter: blur(8px);
            animation: glowing 20s linear infinite;
            transition: opacity .3s ease-in-out;
            border-radius: 40px;
            opacity: 0;
        }

        @keyframes glowing {
            0% {background-position: 0 0;}
            50% {background-position: 400% 0;}
            100% {background-position: 0 0;}
        }

        /* Hover Effect */
        .stButton>button:hover::before {
            opacity: 1;
        }

        /* Active State */
        .stButton>button:active::after {
            background: transparent;
        }

        .stButton>button:active {
            color: #000;
            border-radius: 40px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)


# Custom HTML and CSS for step-like letter-by-letter animation with a white dot cursor
st.markdown(
    """
    <style>
    @keyframes typing {
        from { width: 0; }
        to { width: 100%; }
    }
    @keyframes blink {
        from, to { opacity: 0; }
        50% { opacity: 1; }
    }
    @keyframes disappear {
        0% { opacity: 1; }
        100% { opacity: 0; visibility: hidden; }
    }
    .typing-effect {
        font-size: 45px;
        font-weight: bold;
        color: #ffffff;
        white-space: nowrap;
        overflow: hidden;
        position: relative;
        margin: left;
        text-align: left;
        animation: typing 6s steps(30, end) forwards; /* Step-like typing animation */
    }
    .typing-effect::after {
        content: '';
        position: absolute;
        top: 50%;
        right: 0; /* Place the dot at the typing position */
        transform: translateY(-50%);
        width: 1.2em; 
        height: 1.2em;
        background-color: white; /* Color of the dot */
        border-radius: 50%; /* Make it a circle */
        animation: blink 0.7s step-end infinite alternate, disappear 4s forwards; /* Blinking effect and disappearance */
        animation-delay: 6s, 15s; /* Blink starts after typing, disappearance starts after 1s */
        display: inline-block;
    }
    </style>
    <div class="container">
        <div class="typing-effect">Image Processing Webapp, Welcome........!</div>
    </div>
    """,
    unsafe_allow_html=True
)





import streamlit as st

# Custom CSS to style the sidebar with rounded corners and glow effect
st.markdown("""
    <style>
        /* Main Sidebar Container Styling */
        [data-testid="stSidebar"] {
            background-color: #1a2129; /* Dark background color */
            border-top-right-radius: 50px; /* Curve top right corner */
            border-bottom-right-radius: 50px; /* Curve bottom right corner */
            padding: 10px;
            transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
        }

        /* Glow effect on hover for the sidebar */
        [data-testid="stSidebar"]:hover {
            box-shadow: 0px 0px 15px 5px #dd840e, /* Larger spread and blur */
                        0px 0px 30px 10px #dd840e; /* Additional soft glow layer */
        }

        /* Styling for the sidebar title and links */
        [data-testid="stSidebar"] .css-1v0mbdj:hover {
            text-shadow: 0px 0px 10px #ffffff;
        }

        [data-testid="stSidebar"] a:hover {
            color: #ffffff;
            text-shadow: 0 0 10px #ffffff, 0 0 20px #ffffff;
        }

        /* Focus effect for text input fields */
        [data-testid="stSidebar"] input:focus {
            box-shadow: 0 0 10px 2px #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Content
st.sidebar.title("Image Input Options")
st.sidebar.image("logos/logo2.png")

# Predefined set of test images (URLs or local file paths)
test_images = {
    "Select a test image": None,
    "Apollo 11 Bootprint (best for contrast test)": "sample_images/Apollo 11 Bootprint.jpg",  
    "Butterfly (best for Quality test)": "sample_images/Butterfly.jpg",
    "Buzz Aldrin on the Moon (best for brightness test)": "sample_images/Buzz Aldrin on the Moon.jpg",
    "Cadilac (best for sharpness test)": "sample_images/Cadilac .jpg",
    "Cyber punk (best for contrast test)": "sample_images/Cyber punk.jpg",
    "Flames (best for sharpness test)": "sample_images/Flames.jpg",
    "Lenna (best for Quality test)": "sample_images/Lenna.png",
    "Peppers (best for Quality test)": "sample_images/Peppers.png"
}

test_image_selection = st.sidebar.selectbox("Choose a test image", list(test_images.keys()))
uploaded_file = st.sidebar.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
url_input = st.sidebar.text_input("Enter an image URL")

# Sidebar footer with contact details and icons
st.sidebar.markdown('''
---
<div style="text-align: center; color: #d1d5db;">
    Created and Copyrighted <b style="color: #fbbf24;">©</b>
    <a href="https://www.linkedin.com/in/abhishek-kk-0131-20-07-/" target="_blank" style="color: #fbbf24;">Abhishek KK</a>
</div>

<div style="text-align: center; margin-top: 10px;">
    <b style="color: #999; opacity: 40;">Connect with Me</b>
</div>
<div style="text-align: center; margin-top: 10px;">
    <a href="https://www.linkedin.com/in/abhishek-kk-0131-20-07-/" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="20" style="margin-right: 10px;">
    </a>
    <a href="https://github.com/kk-abhishek" target="_blank">
        <img src="https://img.icons8.com/sf-black-filled/64/FFFFFF/github.png" width="30" style="margin-right: 10px;">
    </a>
    <a href="mailto:kkabhishek100@gmail.com" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" width="20">
    </a>
</div>
''', unsafe_allow_html=True)

# Helper function to check if path is a URL
def is_url(path):
    return urlparse(path).scheme in ("http", "https")

# Load image from file, URL, or test selection
image = None
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
elif test_image_selection != "Select a test image":
    try:
        test_image_path = test_images[test_image_selection]
        if is_url(test_image_path):
            response = requests.get(test_image_path)
            response.raise_for_status()
            image = np.array(Image.open(BytesIO(response.content)))
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        else:
            image = cv2.imread(test_image_path)
            if image is None:
                raise ValueError("Image file not found at the specified path.")
    except Exception as e:
        st.sidebar.error(f"Failed to load test image: {e}")

# Show the main title and enhancement options only if an image is selected
if image is not None:
    st.subheader("Image Enhancement Options")

    # Enhancement buttons section above the original image preview
    col1, col2, col3, col4 = st.columns(4)
    enhanced_image = None

    with col1:
        if st.button(" ✨ Enhance Quality"):
            with st.spinner("Enhancing quality..."):
                time.sleep(1)  # Simulate processing time
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.1)
                    progress.progress(i + 1)
                st.info("⏬Scroll Down and Wait to Download Processed-Img")
                enhanced_image = high_quality_enhancement(image)

    with col2:
        if st.button(" 🌗 Adjust Contrast"):
            with st.spinner("Adjusting contrast..."):
                time.sleep(1)
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.1)
                    progress.progress(i + 1)
                st.info("⏬Scroll Down and Wait to Download Processed-Img")
                enhanced_image = adjust_contrast(image)

    with col3:
        if st.button(" 🔆 Adj Brightness"):
            with st.spinner("Adjusting brightness..."):
                time.sleep(1)
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.1)
                    progress.progress(i + 1)
                st.info("⏬Scroll Down and Wait to Download Processed-Img")
                enhanced_image = adjust_brightness_contrast(image)

    with col4:
        if st.button(" ⚔️ Sharpen Image"):
            with st.spinner("Sharpening image..."):
                time.sleep(1)
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.1)
                    progress.progress(i + 1)
                st.info("⏬Scroll Down and Wait to Download Processed-Img")
                enhanced_image = sharpen_image(image)
    
    

    # Display the original image
    st.subheader("Original Image")
    st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="Original Image", use_container_width=True)

    # Display enhanced image alone below the original image if available
    if enhanced_image is not None:
        st.subheader("Enhanced Image")
        st.image(cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB), caption="Enhanced Image", use_container_width=True)


    # Function to convert the image to bytes and ensure it's in RGB format
    def convert_to_bytes(image):
        if isinstance(image, np.ndarray):
            # Check if the image is in BGR format (as with OpenCV)
            if image.shape[-1] == 3:  # Assuming it's a color image
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # Convert numpy array to PIL Image
            image = Image.fromarray(image)
        elif isinstance(image, Image.Image):
            # If it's already a PIL Image, ensure it's in RGB
            image = image.convert("RGB")
        else:
            raise ValueError("Unsupported image format. Must be a numpy.ndarray or a PIL.Image.")

        # Save the image as PNG bytes
        buffer = BytesIO()
        image.save(buffer, format="PNG")
        buffer.seek(0)
        return buffer.getvalue()




    # Include CSS styling for the glowing effect
    st.markdown(
        """
        <style>
            /* Apply styles to the st.download_button */
            .stDownloadButton > button {
                padding: 15px 40px;
                border: none;
                outline: none;
                color: #f8f2f2;
                cursor: pointer;
                position: relative;
                z-index: 0;
                border-radius: 12px;
                background-color: #000916; /* Default button color */
            }

            /* Dark Background Layer */
            .stDownloadButton > button::after {
                content: "";
                z-index: -1;
                position: absolute;
                width: 100%;
                height: 100%;
                background-color: #1a2129;
                left: 0;
                top: 0;
                border-radius: 40px;
            }

            /* Glow Effect */
            .stDownloadButton > button::before {
                content: "";
                background: linear-gradient(
                    45deg,
                    #620e9a, #00FFD5, #002BFF, #FF00C8, #000000,
                    #620e9a, #00FFD5, #002BFF, #FF00C8, #000000
                );
                position: absolute;
                top: -2px;
                left: -2px;
                background-size: 600%;
                z-index: -1;
                width: calc(100% + 4px);
                height: calc(100% + 4px);
                filter: blur(8px);
                animation: glowing 20s linear infinite;
                transition: opacity .3s ease-in-out;
                border-radius: 40px;
                opacity: 0;
            }

            @keyframes glowing {
                0% {background-position: 0 0;}
                50% {background-position: 400% 0;}
                100% {background-position: 0 0;}
            }

            /* Hover Effect */
            .stDownloadButton > button:hover::before {
                opacity: 1;
            }

            /* Active State */
            .stDownloadButton > button:active::after {
                background: transparent;
            }

            .stDownloadButton > button:active {
                color: #000;
                border-radius: 40px;
                font-weight: bold;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

   
    # Assuming `enhanced_image` is a numpy.ndarray or a Pillow Image
    if enhanced_image is not None:
        # Convert the image to bytes ensuring RGB format
        image_bytes = convert_to_bytes(enhanced_image)

        # Use Streamlit's columns to align the button to the right
        _, _, col = st.columns(3)  # Adjust the proportions as needed

        with col:
            # Streamlit download button
            st.download_button(
                label=" 📌 Download Enhanced Image",
                data=image_bytes,
                file_name="enhanced_image.png",
                mime="image/png",
            )



        # Display a final row with both original and enhanced images side-by-side for comparison
        st.subheader("Comparison: Original vs Enhanced")
        col5, col6 = st.columns(2)
        with col5:
            st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="Original Image", use_container_width=True)
        with col6:
            st.image(cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB), caption="Enhanced Image", use_container_width=True)
else:
    st.info("Select a test image from the app's database, upload your own, or provide an image URL by clicking the arrow in the top-left corner to get started! 📸✨")


st.markdown('''
---
<div style="text-align: center; color: #d1d5db;">
    <b style="color: #ffffff;"> © 2024 </b> 
    <a href="https://www.linkedin.com/in/abhishek-kk-0131-20-07/" target="_blank" style="color: #fbbf24;"> Abhishek KK</a><b style="color: #ffffff;">. All Rights Reserved.</b> 
</div>



<div style="text-align: center; margin-top: 10px;">
    <b style="color: #999; opacity: 40;">Connect with Me</b>
</div>
<div style="text-align: center; margin-top: 10px;">
    <a href="https://www.linkedin.com/in/abhishek-kk-0131-20-07-/" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="20" style="margin-right: 10px;">
    </a>
    <a href="https://github.com/kk-abhishek" target="_blank">
        <img src="https://img.icons8.com/sf-black-filled/64/FFFFFF/github.png" width="30" style="margin-right: 10px;">
    </a>
    <a href="mailto:kkabhishek100@gmail.com" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" width="20">
    </a>
</div>
''', unsafe_allow_html=True)
