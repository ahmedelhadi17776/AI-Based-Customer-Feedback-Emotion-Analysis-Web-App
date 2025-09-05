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

## Tasks Completed

- [x] Task 1: Project repository structure ✅
- [x] Task 2: Emotion detection application using Watson NLP ✅
- [x] Task 3: Format output of the application ✅
- [x] Task 4: Package the application ✅
- [x] Task 5: Unit tests ✅
- [x] Task 6: Flask web deployment ✅
- [x] Task 7: Error handling ✅
- [x] Task 8: Static code analysis (10/10 score) ✅

## Screenshots Required for Submission

For peer review, capture the following screenshots:

1. **Task 1**: `1_folder_structure.png` - Project folder structure
2. **Task 2a**: `2a_emotion_detection.png` - Emotion detection function code
3. **Task 2b**: `2b_application_creation.png` - Successful import test
4. **Task 3a**: `3a_output_formatting.png` - Modified emotion_predictor function
5. **Task 3b**: `3b_formatted_output_test.png` - Output format validation
6. **Task 4a**: `4a_packaging.png` - Package structure and **init**.py
7. **Task 4b**: `4b_packaging_test.png` - Package import validation
8. **Task 5a**: `5a_unit_testing.png` - Unit test code
9. **Task 5b**: `5b_unit_testing_result.png` - All tests passing
10. **Task 6a**: `6a_server.png` - Flask server.py code
11. **Task 6b**: `6b_deployment_test.png` - Web application running
12. **Task 7a**: `7a_error_handling_function.png` - Enhanced error handling
13. **Task 7b**: `7b_error_handling_server.png` - Server error handling
14. **Task 7c**: `7c_error_handling_interface.png` - Error handling validation
15. **Task 8a**: `8a_server_modified.png` - Server.py improvements
16. **Task 8b**: `8b_static_code_analysis.png` - Perfect 10/10 pylint score
