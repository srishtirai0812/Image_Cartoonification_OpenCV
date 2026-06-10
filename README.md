# Image Cartoonification 
An interactive image transformation web application built using Python, OpenCV, and Streamlit that converts images into different artistic styles including Cartoon, Pencil Sketch, and Watercolor effects.

# Features
Upload JPG, JPEG, and PNG images
Cartoonify images using OpenCV image processing
Convert images into Pencil Sketch artwork
Generate Watercolor-style effects
Side-by-side Original vs Processed image comparison
Download processed images instantly
Simple and responsive Streamlit UI

# Tech Stack
Python
OpenCV
NumPy
Pillow (PIL)
Streamlit

# Project Structure
AI_Cartoon_Studio/
│
├── app.py
├── cartoonifier.py
├── requirements.txt
├── README.md
└── outputs/

# Installation
Clone Repository
git clone https://github.com/srishtirai0812/Image_Cartoonification_OpenCV.git
cd Image_Cartoonification_OpenCV
Create Virtual Environment
python -m venv venv
Activate Environment

Windows:

venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt

# Run Application
python -m streamlit run app.py

The application will be available at:

http://localhost:8501

# Available Effects

1. Cartoon Effect

Uses:

Grayscale conversion
Median Blur
Adaptive Thresholding
Bilateral Filtering
Edge Masking
Pencil Sketch

Creates hand-drawn sketch effects using image inversion and Gaussian blur techniques.

2. Watercolor Effect

Applies OpenCV stylization filters to generate watercolor-like artistic outputs.

# Sample Workflow
Upload an image
Select an effect
View transformed output
Download the processed image

# Future Enhancements
Real-time webcam cartoonification
Batch image processing
Anime-style filters
Adjustable effect intensity sliders
Cloud deployment
Face-aware cartoonification