from flask import Flask, render_template, request, jsonify
import json
from chatbot import chatbot_response

app = Flask(__name__)

# Load bookings
def load_data():
    try:
        with open("bookings.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open("bookings.json", "w") as f:
        json.dump(data, f)

@app.route("/")
def home():
    return render_template("index.html")

# Chat API
@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    response = chatbot_response(user_msg)

    data = load_data()

    # If booking triggered
    if "book" in response:
        booking = response["book"]
        data.append(booking)
        save_data(data)

    return jsonify(response)

# Get bookings
@app.route("/bookings")
def bookings():
    return jsonify(load_data())

if __name__ == "__main__":
    app.run(debug=True)
