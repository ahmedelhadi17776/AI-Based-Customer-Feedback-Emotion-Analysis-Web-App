"""
EmotionDetection Package

This package provides emotion detection functionality using Watson NLP library.
It analyzes text input and returns emotion scores for different emotions like
anger, disgust, fear, joy, and sadness along with the dominant emotion.

Modules:
    emotion_detection: Contains the main emotion_detector function

Functions:
    emotion_detector(text_to_analyse): Main function to detect emotions in text

Usage:
    from EmotionDetection import emotion_detector
    result = emotion_detector("I am very happy today!")
    print(result)
"""

# Import the main function to make it available at package level
from .emotion_detection import emotion_detector
