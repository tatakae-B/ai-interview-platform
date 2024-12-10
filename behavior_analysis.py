from transformers import pipeline

# Load the NLP model
analyzer = pipeline("text-classification", model="distilbert-base-uncased")

def analyze_behavior(response):
    analysis = analyzer(response)
    return {"sentiment": analysis[0]['label'], "confidence": analysis[0]['score']}
