from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

# Load your previously trained model
model = joblib.load('intent_classifier.pkl')

responses = {
    "greeting": "Hello! Welcome to Balasore Alloys. How can I assist you today?",
    "company_info": "Balasore Alloys is India's leading producer of ferrochrome. Learn more on our website.",
    "product_inquiry": "We manufacture high-quality Ferro Chrome and Silico Manganese products.",
    "contact_info": "You can contact us at +91-674-1234567 or email info@balasorealloys.com.",
    "location": "Our registered office and plant are located in Balasore, Odisha, India.",
    "feedback": "We welcome your feedback. Please submit it through our feedback form on the website.",
    "goodbye": "Thank you for visiting. Have a great day!"
}

@app.route('/', methods=['GET'])
def home():
    return "Chatbot server is running. Use POST /chat to interact."

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    # Convert prediction to str to avoid numpy array hash bug
    intent = str(model.predict([user_message])[0])
    response = responses.get(intent, "Sorry, I did not understand that. Can you please rephrase?")
    return jsonify({"response": response, "intent": intent})

if __name__ == '__main__':
    app.run(port=5000)
