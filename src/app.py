import os
from flask import Flask, request, render_template, jsonify # Import render_template
from textblob import TextBlob
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__) # Flask will look for the 'templates' folder

# --- Core Sentiment Analysis Logic ---
# (Keep your analyze_sentiment function exactly as before)
def analyze_sentiment(text):
    """
    Analyzes the sentiment of a given text using TextBlob.

    Args:
        text (str): The input text to analyze.

    Returns:
        str: "Positive", "Negative", or "Neutral" sentiment.
    """
    if not isinstance(text, str):
        return "Invalid Input"
    try:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0.05:
            return "Positive"
        elif polarity < -0.05:
            return "Negative"
        else:
            return "Neutral"
    except Exception as e:
        app.logger.error(f"Error during sentiment analysis: {e}")
        return "Error Analyzing"


# --- Route for the Web UI ---
@app.route('/', methods=['GET', 'POST']) # Handle both GET and POST requests
def home():
    """
    Handles requests for the main page.
    GET: Displays the empty form.
    POST: Processes form data, analyzes sentiment, and displays the result.
    """
    text_input = None
    sentiment = None

    if request.method == 'POST':
        # Get the text from the form submission
        # 'text_input' matches the 'name' attribute in the HTML <textarea>
        text_input = request.form.get('text_input', '') # Use .get for safety
        app.logger.info(f"Received text for analysis: '{text_input[:50]}...'")
        if text_input:
            sentiment = analyze_sentiment(text_input)
            app.logger.info(f"Analysis result: {sentiment}")
        else:
            app.logger.warning("Received empty text input.")

    # Render the HTML template.
    # Pass the variables to the template. If it's a GET request or
    # empty POST, sentiment will be None and the result section won't show.
    return render_template('index.html', text_input=text_input, sentiment=sentiment)

# --- Optional API Endpoint (Keep if needed for programmatic access) ---
@app.route('/analyze', methods=['POST'])
def analyze_api_route():
    """
    API endpoint to analyze sentiment (from previous version).
    Expects a POST request with JSON body: {"text": "some sentence"}
    Returns JSON: {"text": "some sentence", "sentiment": "Positive/Negative/Neutral"}
    """
    app.logger.info("Received request for /analyze API")
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    data = request.get_json()
    if 'text' not in data:
        return jsonify({"error": "Missing 'text' field in JSON data"}), 400
    text_to_analyze = data['text']
    sentiment = analyze_sentiment(text_to_analyze)
    return jsonify({"text": text_to_analyze, "sentiment": sentiment})


# --- Server Startup ---
if __name__ == "__main__":
    # Ensure TextBlob corpora are downloaded (might need to run this manually once
    # or add 'RUN python -m textblob.download_corpora' to your Dockerfile)
    # try:
    #     from textblob.download_corpora import download_all
    #     download_all()
    # except Exception as e:
    #     app.logger.warning(f"Could not download TextBlob corpora automatically: {e}")

    port = int(os.environ.get("PORT", 8080))
    app.logger.info(f"Starting server on host 0.0.0.0, port {port}")
    # Set debug=True for local development ONLY (provides auto-reload and better error pages)
    # Set debug=False for production/Cloud Run
    app.run(host='0.0.0.0', port=port, debug=True) # Use debug=True locally