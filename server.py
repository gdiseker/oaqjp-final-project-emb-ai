from flask import Flask, render_template, request
import requests
from emotion_detection import analyze_emotions

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector():
    # Get the text input from the query parameters
    text_to_analyze = request.args.get('textToAnalyze', '')  # Extract text from the query string

    if not text_to_analyze:
        return "No text provided.", 400

    # Call the emotion detection API (or your logic to analyze emotions)
    url = "http://127.0.0.1:5000"  # Ensure this matches the base URL of your emotion detection API
    headers = {"Content-Type": "application/json"}
    payload = {"text": text_to_analyze}

    try:
        response = requests.post(url, json=payload, headers=headers)  # Send the POST request to the API
        if response.status_code == 200:
            data = response.json()
            response_string = (
                f"For the given statement, the system response is "
                f"'anger': {data['anger']}, 'disgust': {data['disgust']}, 'fear': {data['fear']}, "
                f"'joy': {data['joy']} and 'sadness': {data['sadness']}. "
                f"The dominant emotion is {data['dominant_emotion']}."
            )
            return response_string
        else:
            return f"Error: {response.status_code} - {response.text}", 500
    except requests.exceptions.RequestException as e:
        return f"Failed to connect to the Emotion Detection API: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)