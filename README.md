# AI-Based Customer Feedback Emotion Analysis Web App

This is an AI-based web application that performs emotion analysis on customer feedback text. It uses Watson NLP library to detect emotions like joy, sadness, anger, fear, and disgust from customer feedback.

## Features

- Emotion detection using Watson NLP
- Web interface built with Flask
- Error handling for invalid inputs
- Unit tests for reliability
- Static code analysis compliance

## Project Structure

```
AI-Based-Customer-Feedback-Emotion-Analysis-Web-App/
├── emotion_detection.py          # Main emotion detection module
├── server.py                     # Flask web server
├── test_emotion_detection.py     # Unit tests
├── requirements.txt              # Project dependencies
├── README.md                     # Project documentation
└── EmotionDetection/            # Package directory
    └── __init__.py              # Package initialization
```

## Installation

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:

   ```bash
   python server.py
   ```

3. Open your web browser and navigate to `http://localhost:5000`

## Usage

Enter customer feedback text in the web interface and click "Run Sentiment Analysis" to get emotion analysis results.

## Testing

Run unit tests:

```bash
python -m unittest test_emotion_detection.py
```

## Static Code Analysis

Run pylint for code quality check:

```bash
pylint server.py
```
