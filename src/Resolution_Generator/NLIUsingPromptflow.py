# Facilitate natural language interactions between support engineers and the AI system 
# for intuitive querying and information retrieval.

from flask import Flask, request, jsonify
import openai
import joblib
import os

app = Flask(__name__)

# Load ML model and vectorizer
clf = joblib.load('rf_classifier.joblib')
vectorizer = joblib.load('tfidf_vectorizer.joblib')

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.json
    description = data.get('description', '')
    
    # Predict category
    X_vect = vectorizer.transform([description])
    category = clf.predict(X_vect)[0]
    
    # Generate resolution
    resolution = generate_resolution(description)
    
    return jsonify({
        'category': category,
        'resolution': resolution
    })

def generate_resolution(description, max_tokens=150):
    prompt = f"Given the following incident description, provide a detailed resolution:\n\n{description}\n\nResolution:"
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use appropriate model
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    resolution = response.choices[0].text.strip()
    return resolution

if __name__ == '__main__':
    app.run(debug=True)