import gradio as gr
from transformers import pipeline

# Load the emotion detection model
emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion", return_all_scores=True)

def emotion_detector(text_to_analyze):
    try:
        if not text_to_analyze.strip():
            return {
                'error': "Please enter some text to analyze",
                'status_code': 400
            }
            
        # Get predictions
        predictions = emotion_classifier(text_to_analyze)[0]
        
        # Extract emotion scores
        emotion_scores = {item['label']: item['score'] for item in predictions}
        
        # Find dominant emotion
        dominant_emotion = max(emotion_scores.items(), key=lambda x: x[1])[0]
        
        # Return formatted output
        return {
            **emotion_scores,
            'dominant_emotion': dominant_emotion
        }
        
    except Exception as e:
        return {
            'error': str(e),
            'status_code': 500
        }

def format_output(results):
    if 'error' in results:
        return f"Error: {results['error']} (Status: {results.get('status_code', 'Unknown')})"
    
    output = []
    for emotion, score in results.items():
        if emotion != 'dominant_emotion':
            output.append(f"{emotion}: {score:.4f}")
    
    output.append(f"\nDominant Emotion: {results['dominant_emotion']}")
    return "\n".join(output)

# Create Gradio interface
def gradio_emotion_detector(text):
    result = emotion_detector(text)
    return format_output(result)

iface = gr.Interface(
    fn=gradio_emotion_detector,
    inputs=gr.Textbox(lines=3, placeholder="Enter text here...", label="Input Text"),
    outputs=gr.Textbox(label="Emotion Analysis"),
    title="Emotion Detection App",
    description="Analyze the emotions in your text using AI."
)

iface.launch()
