from flask import Flask, request, jsonify
import random
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Firebase setup
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def home():
    return "Backend Running!"

@app.route('/detect', methods=['POST'])
def detect():
    data = request.json

    image = data.get("image")

    result = {
        "disease": "Leaf Spot",
        "confidence": "92%"
    }

    # Save to Firebase
    db.collection("detections").add({
        "image": image,
        "result": result
    })

    return jsonify(result)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json

    message = data.get("message")

    reply = "I am feeling a bit sick 😢"

    # Save chat
    db.collection("chats").add({
        "message": message,
        "reply": reply
    })

    return jsonify({"reply": reply})
@app.route('/notification', methods=['POST'])
def notification():
    alert = "Water your plant today!"

    db.collection("notifications").add({
        "alert": alert
    })

    return jsonify({"alert": alert})
@app.route('/medicine', methods=['POST'])
def medicine():
    data = request.json
    disease = data.get("disease")

    treatments = {
        "Leaf Spot": "Use neem oil spray and remove infected leaves",
        "Powdery Mildew": "Apply fungicide and avoid overwatering",
        "Root Rot": "Improve drainage and reduce watering"
    }

    treatment = treatments.get(disease, "General plant care needed")

    db.collection("medicines").add({
        "disease": disease,
        "treatment": treatment
    })

    return jsonify({
        "disease": disease,
        "treatment": treatment
    })
@app.route('/testdb')
def testdb():
    db.collection("test").add({
        "message": "Firebase working!"
    })
    return "Data added to Firebase!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)