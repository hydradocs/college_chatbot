import json
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Load the intents file
with open('intents.json') as file:
    intents = json.load(file)

# Function to get a response based on the intent
def get_response(intent_tag):
    for intent in intents['intents']:
        if intent['tag'] == intent_tag:
            return random.choice(intent['responses'])

# Sample logic to match user input to intent (this can be extended)
def match_intent(user_input):
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input.lower():
                return intent['tag']
    return "unknown"

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get("message")
    matched_intent = match_intent(user_input)
    
    if matched_intent != "unknown":
        response = get_response(matched_intent)
    else:
        response = "Sorry, I didn't understand that. Can you try rephrasing?"

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
