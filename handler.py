import runpod
from transformers import pipeline

# Initialize the sentiment analysis pipeline
# This is loaded once when the worker container starts
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def handler(event):
    """
    Main handler function for RunPod Serverless.
    Processes the input text and returns sentiment analysis results.
    """
    # Extract input data from the request event
    input_data = event.get("input", {})
    text = input_data.get("text", "")

    # Basic validation
    if not text:
        return {"error": "No input text provided."}

    # Perform model inference
    prediction = classifier(text)

    # Return structured output
    return {
        "text": text,
        "sentiment": prediction[0]["label"],
        "confidence": prediction[0]["score"]
    }

# Start the serverless worker
runpod.serverless.start({"handler": handler})
