"""
Flask Web Server for Emotion Detection Application

This module provides a web interface for the emotion detection functionality.
Users can input text and get emotion analysis results through a web browser.
"""

from flask import Flask, request, render_template_string
from EmotionDetection import emotion_detector

# Initialize the Flask application
app = Flask(__name__)


@app.route("/")
def render_index_page():
    """
    Render the main index page with the emotion detection interface

    Returns:
        str: HTML content for the main page
    """
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AI-Based Emotion Detection</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                color: #333;
            }
            .container {
                background: white;
                border-radius: 15px;
                padding: 30px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            }
            h1 {
                text-align: center;
                color: #4a5568;
                margin-bottom: 30px;
                font-size: 2.5em;
            }
            .form-group {
                margin-bottom: 20px;
            }
            label {
                display: block;
                margin-bottom: 8px;
                font-weight: bold;
                color: #2d3748;
            }
            textarea {
                width: 100%;
                min-height: 120px;
                padding: 12px;
                border: 2px solid #e2e8f0;
                border-radius: 8px;
                font-size: 16px;
                resize: vertical;
                box-sizing: border-box;
                transition: border-color 0.3s ease;
            }
            textarea:focus {
                outline: none;
                border-color: #667eea;
                box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
            }
            .btn-submit {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 12px 30px;
                border: none;
                border-radius: 25px;
                font-size: 16px;
                cursor: pointer;
                transition: transform 0.2s ease;
                display: block;
                margin: 20px auto;
            }
            .btn-submit:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            }
            .footer {
                text-align: center;
                margin-top: 30px;
                color: #718096;
                font-size: 14px;
            }
            .description {
                background: #f7fafc;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 25px;
                border-left: 4px solid #667eea;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🧠 AI-Based Emotion Detection</h1>
            
            <div class="description">
                <p><strong>Welcome to our Emotion Analysis Tool!</strong></p>
                <p>Enter any text below and our AI will analyze the emotional content, 
                   detecting emotions like joy, sadness, anger, fear, and disgust. 
                   Perfect for analyzing customer feedback, social media posts, or any text content.</p>
            </div>
            
            <form action="/emotionDetector" method="POST">
                <div class="form-group">
                    <label for="textToAnalyze">Enter text to analyze:</label>
                    <textarea 
                        name="textToAnalyze" 
                        id="textToAnalyze" 
                        placeholder="Type or paste your text here... (e.g., 'I love this new product, it makes me so happy!')"
                        required
                    ></textarea>
                </div>
                <button type="submit" class="btn-submit">🔍 Run Sentiment Analysis</button>
            </form>
            
            <div class="footer">
                <p>Powered by Watson NLP • Built with Flask</p>
            </div>
        </div>
    </body>
    </html>
    ''')


@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """
    Handle emotion detection requests from the web interface

    Returns:
        str: HTML response with emotion analysis results
    """
    # Get text to analyze from form data
    text_to_analyze = request.form.get('textToAnalyze')

    # Enhanced error handling for invalid input
    if not text_to_analyze or text_to_analyze.strip() == '' or text_to_analyze.isspace():
        return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Error - Emotion Detection</title>
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    color: #333;
                }
                .container {
                    background: white;
                    border-radius: 15px;
                    padding: 30px;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
                    text-align: center;
                }
                .error-message {
                    color: #e53e3e;
                    font-size: 1.2em;
                    margin: 20px 0;
                }
                .btn-back {
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 12px 30px;
                    text-decoration: none;
                    border-radius: 25px;
                    display: inline-block;
                    margin-top: 20px;
                    transition: transform 0.2s ease;
                }
                .btn-back:hover {
                    transform: translateY(-2px);
                    text-decoration: none;
                    color: white;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>⚠️ Invalid Input</h1>
                <div class="error-message">
                    Invalid text! Please provide some text to analyze.
                </div>
                <a href="/" class="btn-back">← Go Back</a>
            </div>
        </body>
        </html>
        ''')

    # Perform emotion detection
    emotion_result = emotion_detector(text_to_analyze)

    # Check if emotion detection failed and handle the error
    if emotion_result is None or emotion_result.get('dominant_emotion') is None:
        return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Error - Emotion Detection</title>
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    color: #333;
                }
                .container {
                    background: white;
                    border-radius: 15px;
                    padding: 30px;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
                    text-align: center;
                }
                .error-message {
                    color: #e53e3e;
                    font-size: 1.2em;
                    margin: 20px 0;
                }
                .btn-back {
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 12px 30px;
                    text-decoration: none;
                    border-radius: 25px;
                    display: inline-block;
                    margin-top: 20px;
                    transition: transform 0.2s ease;
                }
                .btn-back:hover {
                    transform: translateY(-2px);
                    text-decoration: none;
                    color: white;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>⚠️ Processing Error</h1>
                <div class="error-message">
                    Unable to process the text for emotion analysis. Please try again with different text.
                </div>
                <a href="/" class="btn-back">← Go Back</a>
            </div>
        </body>
        </html>
        ''')

    # Format the response
    response_text = f"""
    <h2>📊 Emotion Analysis Results</h2>
    <div class="analysis-input">
        <strong>Analyzed Text:</strong> "{text_to_analyze}"
    </div>
    <div class="emotion-scores">
        <h3>Emotion Scores:</h3>
        <div class="emotion-item">😠 <strong>Anger:</strong> {emotion_result['anger']}</div>
        <div class="emotion-item">🤢 <strong>Disgust:</strong> {emotion_result['disgust']}</div>
        <div class="emotion-item">😨 <strong>Fear:</strong> {emotion_result['fear']}</div>
        <div class="emotion-item">😊 <strong>Joy:</strong> {emotion_result['joy']}</div>
        <div class="emotion-item">😢 <strong>Sadness:</strong> {emotion_result['sadness']}</div>
    </div>
    <div class="dominant-emotion">
        <h3>🎯 Dominant Emotion: <span class="highlight">
        {emotion_result['dominant_emotion'].title()}</span></h3>
    </div>
    """

    return render_template_string(f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Results - Emotion Detection</title>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                color: #333;
            }}
            .container {{
                background: white;
                border-radius: 15px;
                padding: 30px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            }}
            h1 {{
                text-align: center;
                color: #4a5568;
                margin-bottom: 30px;
            }}
            .analysis-input {{
                background: #f7fafc;
                padding: 15px;
                border-radius: 8px;
                margin-bottom: 25px;
                border-left: 4px solid #48bb78;
            }}
            .emotion-scores {{
                margin: 20px 0;
            }}
            .emotion-item {{
                padding: 10px;
                margin: 8px 0;
                background: #f8f9fa;
                border-radius: 5px;
                border-left: 3px solid #667eea;
                font-size: 1.1em;
            }}
            .dominant-emotion {{
                background: linear-gradient(135deg, #48bb78, #38a169);
                color: white;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                margin: 25px 0;
            }}
            .highlight {{
                font-size: 1.3em;
                font-weight: bold;
                text-transform: uppercase;
            }}
            .btn-back {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 12px 30px;
                text-decoration: none;
                border-radius: 25px;
                display: inline-block;
                margin-top: 20px;
                transition: transform 0.2s ease;
            }}
            .btn-back:hover {{
                transform: translateY(-2px);
                text-decoration: none;
                color: white;
            }}
            .footer {{
                text-align: center;
                margin-top: 30px;
                color: #718096;
                font-size: 14px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🧠 AI-Based Emotion Detection</h1>
            {response_text}
            <div style="text-align: center;">
                <a href="/" class="btn-back">← Analyze Another Text</a>
            </div>
            <div class="footer">
                <p>Powered by Watson NLP • Built with Flask</p>
            </div>
        </div>
    </body>
    </html>
    ''')


if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000, debug=True)
