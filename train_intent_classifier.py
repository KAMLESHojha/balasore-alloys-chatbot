import joblib
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Define training data
intents = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "company_info": ["tell me about balasore alloys", "company info", "what do you do"],
    "product_inquiry": ["what products do you have", "tell me about your ferrochrome", "product details"],
    "contact_info": ["how can i contact you", "contact details", "phone number"],
    "location": ["where are you located", "address", "office location"],
    "feedback": ["i want to give feedback", "submit feedback", "complaints"],
    "goodbye": ["bye", "see you", "thank you"]
}

data = [(phrase, intent) for intent, phrases in intents.items() for phrase in phrases]
X_train = [item[0] for item in data]
y_train = [item[1] for item in data]

model = make_pipeline(TfidfVectorizer(), LogisticRegression())
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "intent_classifier.pkl")

print("Intent classifier model trained and saved successfully.")
