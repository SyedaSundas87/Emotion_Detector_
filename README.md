# Emotion_Detector_
# Emotion Detection App

A web application that detects emotions in text using a pre-trained NLP model.

## Features
- Detects 6 emotions: joy, sadness, anger, fear, surprise, and love
- Identifies the dominant emotion
- Simple and intuitive interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/emotion-detection-app.git
cd emotion-detection-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python app.py
```

The app will launch at `http://localhost:7860` in your browser.

## Deployment

You can deploy this app on:
- Hugging Face Spaces
- Vercel
- Railway
- Any Python hosting service

## Model Information
Uses `distilbert-base-uncased-emotion` from Hugging Face Transformers.
