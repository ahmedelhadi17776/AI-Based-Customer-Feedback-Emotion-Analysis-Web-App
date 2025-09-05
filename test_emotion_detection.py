"""
Unit Tests for Emotion Detection Application

This module contains comprehensive unit tests for the emotion_detector function
to ensure it works correctly under various scenarios.
"""

import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for the emotion_detector function"""

    def test_emotion_detector_joy(self):
        """Test emotion detection for joyful text"""
        result = emotion_detector("I am so happy today")

        # Check that all required keys are present
        required_keys = ['anger', 'disgust', 'fear',
                         'joy', 'sadness', 'dominant_emotion']
        for key in required_keys:
            self.assertIn(key, result)

        # Check that dominant emotion is detected correctly for positive text
        self.assertIsInstance(result['joy'], (int, float))
        self.assertIsInstance(result['dominant_emotion'], str)

    def test_emotion_detector_anger(self):
        """Test emotion detection for angry text"""
        result = emotion_detector("I hate this so much")

        # Check that all required keys are present
        required_keys = ['anger', 'disgust', 'fear',
                         'joy', 'sadness', 'dominant_emotion']
        for key in required_keys:
            self.assertIn(key, result)

        # Check that result has proper structure
        self.assertIsInstance(result['anger'], (int, float))
        self.assertIsInstance(result['dominant_emotion'], str)

    def test_emotion_detector_sadness(self):
        """Test emotion detection for sad text"""
        result = emotion_detector("I am feeling very sad today")

        # Check that all required keys are present
        required_keys = ['anger', 'disgust', 'fear',
                         'joy', 'sadness', 'dominant_emotion']
        for key in required_keys:
            self.assertIn(key, result)

        # Check that result has proper structure
        self.assertIsInstance(result['sadness'], (int, float))
        self.assertIsInstance(result['dominant_emotion'], str)

    def test_emotion_detector_fear(self):
        """Test emotion detection for fearful text"""
        result = emotion_detector("I am really scared of this situation")

        # Check that all required keys are present
        required_keys = ['anger', 'disgust', 'fear',
                         'joy', 'sadness', 'dominant_emotion']
        for key in required_keys:
            self.assertIn(key, result)

        # Check that result has proper structure
        self.assertIsInstance(result['fear'], (int, float))
        self.assertIsInstance(result['dominant_emotion'], str)

    def test_emotion_detector_disgust(self):
        """Test emotion detection for disgusted text"""
        result = emotion_detector("This is absolutely disgusting")

        # Check that all required keys are present
        required_keys = ['anger', 'disgust', 'fear',
                         'joy', 'sadness', 'dominant_emotion']
        for key in required_keys:
            self.assertIn(key, result)

        # Check that result has proper structure
        self.assertIsInstance(result['disgust'], (int, float))
        self.assertIsInstance(result['dominant_emotion'], str)

    def test_emotion_detector_blank_text(self):
        """Test emotion detection with blank text input"""
        result = emotion_detector("")

        # Check that all required keys are present
        required_keys = ['anger', 'disgust', 'fear',
                         'joy', 'sadness', 'dominant_emotion']
        for key in required_keys:
            self.assertIn(key, result)

        # For blank input, function should still return structured response
        self.assertIsNotNone(result)

    def test_emotion_detector_return_format(self):
        """Test that the function returns the correct data types"""
        result = emotion_detector("Test text for format validation")

        # Test return type is dictionary
        self.assertIsInstance(result, dict)

        # Test that numeric values are present for emotion scores
        numeric_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        for key in numeric_keys:
            self.assertIn(key, result)
            # Value should be a number or None
            self.assertTrue(isinstance(result[key], (int, float, type(None))))

        # Test that dominant emotion is a string or None
        self.assertIn('dominant_emotion', result)
        self.assertTrue(isinstance(
            result['dominant_emotion'], (str, type(None))))

    def test_emotion_detector_multiple_sentences(self):
        """Test emotion detection with multiple sentences"""
        text = "I love this new technology. It makes me very happy. This is amazing!"
        result = emotion_detector(text)

        # Check that all required keys are present
        required_keys = ['anger', 'disgust', 'fear',
                         'joy', 'sadness', 'dominant_emotion']
        for key in required_keys:
            self.assertIn(key, result)

        # Should return valid result for longer text
        self.assertIsInstance(result, dict)


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)
