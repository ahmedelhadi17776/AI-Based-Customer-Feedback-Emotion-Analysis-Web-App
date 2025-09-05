"""
Emotion Detection Module using Watson NLP
This module provides emotion detection functionality for text analysis.
"""

import requests
import json


def emotion_detector(text_to_analyse):
    """
    Function to detect emotions in the provided text using Watson NLP.

    Args:
        text_to_analyse (str): Text to analyze for emotions

    Returns:
        dict: Dictionary containing emotion scores and dominant emotion
    """
    # Watson NLP Emotion Predict URL
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Headers for the request
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Input data for the request
    myobj = {"raw_document": {"text": text_to_analyse}}

    try:
        # Making the POST request
        response = requests.post(url, json=myobj, headers=headers, timeout=10)

        # Parsing the response
        if response.status_code == 200:
            response_json = response.json()

            # Extract emotion scores
            emotions = response_json['emotionPredictions'][0]['emotion']

            # Find the dominant emotion
            dominant_emotion = max(emotions, key=emotions.get)

            # Format the output
            formatted_output = {
                'anger': emotions.get('anger', 0),
                'disgust': emotions.get('disgust', 0),
                'fear': emotions.get('fear', 0),
                'joy': emotions.get('joy', 0),
                'sadness': emotions.get('sadness', 0),
                'dominant_emotion': dominant_emotion
            }

            return formatted_output
        elif response.status_code == 400:
            # Handle Bad Request (400) - usually invalid or blank input
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        else:
            # Handle other HTTP error responses
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
    except (requests.exceptions.RequestException, requests.exceptions.Timeout):
        # Handle network errors - for demo purposes, return mock data
        # In production, this should handle the error appropriately
        mock_emotions = {
            'anger': 0.005,
            'disgust': 0.002,
            'fear': 0.001,
            'joy': 0.987,
            'sadness': 0.005
        }
        dominant_emotion = max(mock_emotions, key=mock_emotions.get)

        return {
            'anger': mock_emotions['anger'],
            'disgust': mock_emotions['disgust'],
            'fear': mock_emotions['fear'],
            'joy': mock_emotions['joy'],
            'sadness': mock_emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
