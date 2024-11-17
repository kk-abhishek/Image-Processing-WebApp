
# 🌟 Image Enhancement WebApp

**Image Enhancement WebApp** is an interactive web application built using Streamlit, designed to enhance and improve the quality of uploaded images. Using advanced image enhancement techniques, the app allows users to **upload**,**use test images**, or **enter image URL** from their **desktop** or **mobile** and apply enhancement methods for better clarity and sharpness. The app also supports multiple image formats and allows for easy download of the enhanced images.

---

## 📹 Desktop view

Check out the demo of the app to see its features in action :
    
[![Loom Video](https://img.shields.io/badge/Loom-0078D4?style=for-the-badge&logo=loom&logoColor=white)](https://www.loom.com/share/28ce91ac5291450397fa5c773d078b2b?sid=9bb4c34a-41cd-4443-aafb-d9c8b58c6482)


---

## 📹 Mobile view

Check out the demo of the app to see its features in action :
    
[![Loom Video](https://img.shields.io/badge/Loom-0078D4?style=for-the-badge&logo=loom&logoColor=white)](https://www.loom.com/share/28ce91ac5291450397fa5c773d078b2b?sid=9bb4c34a-41cd-4443-aafb-d9c8b58c6482)


---

## 📹 APP Demo

Check out the demo of the app to see its features in action :
    
[![Loom Video](https://img.shields.io/badge/Loom-0078D4?style=for-the-badge&logo=loom&logoColor=white)](https://www.loom.com/share/28ce91ac5291450397fa5c773d078b2b?sid=9bb4c34a-41cd-4443-aafb-d9c8b58c6482)


---

## 🌐 Access the App Online

Access the live application here :

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-pix-enhance-by-kk.streamlit.app/)



---

## 🚀 Features
- **Image Upload:** 
    Upload images directly from your desktop or phone for enhancement.
- **Multiple Enhancement Filters:** 
    Choose from various filters to improve the clarity, sharpness, and overall quality of images.
- **Download Enhanced Image:** 
    After enhancement, download the improved image to your device.
- **Multiple Image Formats Supported:** 
    Supports multiple formats, including JPG, PNG, and more.
- **Interactive Interface:** 
    Simple, user-friendly interface to seamlessly upload and enhance images.

---
## 🔧 Project Structure

```plaintext
.
├── .streamlit              # Streamlit configuration
│   └── config.toml         # Streamlit app settings
├── logos                   # Logos and branding
│   └── logo2.png           # Logo image
├── sample_images           # Folder containing sample images
│   └── list of images      # Sample images for demonstration
├── app.py                  # Main app script
├── requirements.txt        # Python dependencies
├── package.txt             # Additional package requirements
└── README.md               # Project description and setup

```
---

## 🛠️ Setup Instructions

- **Prerequisites:**
    - Python 3.11+: Ensure Python is installed on your machine.
    - Git: Make sure Git is installed to clone the repository.

- **Clone the Repository:**
    Open your terminal and run: 
    ```bash
    git clone https://github.com/kk-abhishek/Image-Processing-WebApp.git
    ```

- **Create a Virtual Environment:** (Optional but Recommended)  
    To avoid conflicts with other Python packages, set up a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # For Windows
    source venv/bin/activate  # For macOS/Linux
    ```

- **Install Dependencies:**  
    Use the following command to install all required libraries listed in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

- **Run the Application Locally:**  
    Start the Streamlit app by running:
    ```bash
    streamlit run app.py
    ```
    After executing this command, a link (e.g., http://localhost:8501) will appear in the terminal. Click on the link or paste it into your browser to access the app locally.

---
## 🌐 Deploying on Streamlit Cloud

- **Sign Up/Login:**
    Go to Streamlit Cloud and sign in.
- **Create a New App:**
    Link your GitHub repository and select the correct repository (image-enhancement-webapp).
- **Set Entry Point:**
    Choose app.py as the main file to run.
- **Deploy:**
    Click Deploy, and your app will be live on Streamlit.
---
## 🧪 How to Use

- **Upload Image:**  
    Click on the "Upload Image" button to select an image from your device.

- **Apply Filters:**  
    Choose from the available enhancement filters to improve the image.

- **View Results:**  
    See the enhanced image on the screen and compare it with the original.

- **Download Enhanced Image:**  
    Click on the download button to save the enhanced image to your device.

---
## 📊 Technology Stack

- **Backend:** Python, OpenCV, Image Processing Libraries  
- **Frontend:** Streamlit  
- **Libraries for Image Enhancement:** OpenCV, Pillow, NumPy  
- **Utilities:** Requests, io.BytesIO, urllib.parse, time  
- **Visualization:** Streamlit for interactive UI  

<p align="left">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" alt="Python"/>
  </a>
  <a href="https://streamlit.io/">
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
  </a>
  <a href="https://opencv.org/">
    <img src="https://img.shields.io/badge/OpenCV-5C3B6F?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV"/>
  </a>
  <a href="https://pillow.readthedocs.io/">
    <img src="https://img.shields.io/badge/Pillow-003366?style=for-the-badge&logo=pillow&logoColor=white" alt="Pillow"/>
  </a>
  <a href="https://numpy.org/">
    <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/>
  </a>
  <a href="https://docs.python-requests.org/">
    <img src="https://img.shields.io/badge/Requests-FF5733?style=for-the-badge&logo=python&logoColor=white" alt="Requests"/>
  </a>
  <a href="https://docs.python.org/3/library/io.html">
    <img src="https://img.shields.io/badge/io.BytesIO-006400?style=for-the-badge&logo=python&logoColor=white" alt="io.BytesIO"/>
  </a>
  <a href="https://docs.python.org/3/library/urllib.parse.html">
    <img src="https://img.shields.io/badge/urllib.parse-800080?style=for-the-badge&logo=python&logoColor=white" alt="urllib.parse"/>
  </a>
  <a href="https://docs.python.org/3/library/time.html">
    <img src="https://img.shields.io/badge/Time-2F4F4F?style=for-the-badge&logo=python&logoColor=white" alt="Time"/>
  </a>
</p>


---
## 👤 Author
**Abhishek KK**  

<div>
  <a href="https://www.linkedin.com/in/abhishek-kk-0131-20-07-/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="https://github.com/kk-abhishek">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  <a href="kkabhishek100@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>
</div>

<div style="text-align: center; color: #d1d5db;">
    <b style="color: #ffffff;"> © 2024 </b> 
    <a href="https://www.linkedin.com/in/abhishek-kk-0131-20-07/" target="_blank" style="color: #fbbf24;"> Abhishek KK</a><b style="color: #ffffff;">. All Rights Reserved.</b> 
</div>
