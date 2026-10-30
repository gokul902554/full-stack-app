
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Backend is Running Successfully!"

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    return jsonify({
        "status": "success",
        "message": f"Thank you {name}! Your form submitted successfully."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
