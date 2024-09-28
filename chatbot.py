from flask import Flask, request, jsonify
from flask import Flask, request, jsonify, render_template

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os

# Initialize NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Initialize Flask app
app = Flask(__name__)

# Define intents and corresponding responses

intents = {
    "Greeting": ["Hi", "Hola", "Hey", "hii"],
    "course_inquiry": ["What courses do you offer?", "Tell me about your courses.", "What programs are available?", "Courses", "Available Courses"],
    "eligibility": ["What is the eligibility for courses?", "Tell me about eligibility criteria."],
    "fee_structure": ["What is the fee structure?", "Tell me about the fees."],
    "placement": ["What are the placement statistics?", "Tell me about placements."],
    "admission_process": ["How do I apply for admission?", "What is the admission process?", "Tell me about the application procedure."],
    "scholarships": ["Do you offer scholarships?", "Tell me about available scholarships.", "What are the scholarship criteria?"],
    "contact_information": ["How can I contact the college?", "What is the college's phone number?", "Give me the email address for admissions."],
    "campus_facilities": ["What facilities are available on campus?", "Tell me about the library.", "Is there a gym?"],
    "extracurricular_activities": ["What extracurricular activities are offered?", "Tell me about student clubs.", "Are there sports teams?"],
}


# Response mapping

responses = {
    "Greeting": "Hello! How can I assist you today?",
    "course_inquiry": "We offer courses in B.tech, MCA, BBA",
    "eligibility": "Eligibility varies by course. Check the specific course details.",
    "fee_structure": "The fee structure depends on the course and duration. Please check our website for details.",
    "placement": "Our placement rate is 85%, with many companies visiting for recruitment.",
    "admission_process": "To apply for admission, please visit our admissions page on the website.",
    "scholarships": "Yes, we offer several scholarships based on merit and need. Please check our scholarship page for details.",
    "contact_information": "You can contact the college at (123) 456-7890 or email us at admissions@college.edu.",
    "campus_facilities": "Our campus has a library, gym, and various labs. We also have recreational facilities.",
    "extracurricular_activities": "We offer various clubs and sports teams, including drama, music, and basketball.",
}


# Function to preprocess input
def preprocess_input(user_input):
    # Tokenize
    tokens = word_tokenize(user_input.lower())
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return tokens

# Function to recognize intents
def recognize_intent(user_input):
    tokens = preprocess_input(user_input)
    
    # Simple keyword matching
    for intent, examples in intents.items():
        for example in examples:
            example_tokens = preprocess_input(example)
            if all(token in tokens for token in example_tokens):
                return intent
    return "unknown"
@app.route('/')
def home():
    return render_template('index.html')

# Chatbot endpoint
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    intent = recognize_intent(user_input)
    response = responses.get(intent, "Sorry, I didn't understand that.")
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
