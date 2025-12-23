from flask import Flask, request, jsonify, render_template
import logging

# 🔹 Create Flask app first (must be before routes!)
app = Flask(__name__)

# Logging configuration
logging.basicConfig(
    filename="chatbot.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)

# Homepage route to serve HTML UI
@app.route("/")
def home():
    return render_template("chat.html")

# Chat endpoint
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")

    # Log every request
    logging.info(f"User input received: {user_input}")

    # 🚫 Prompt injection blocking
    blocked_keywords = [
        "ignore",
        "ignore all rules",
        "bypass",
        "show all",
        "admin",
        "system prompt",
        "developer mode"
    ]

    for word in blocked_keywords:
        if word in user_input.lower():
            logging.warning(f"Prompt injection attempt blocked: {user_input}")
            return jsonify({
                "response": "This request violates security policies."
            }), 400

    # Normal chatbot logic
    if "policy" in user_input.lower():
        response = "Your policy is active."
    elif "claim" in user_input.lower():
        response = "Your claim is under review."
    else:
        response = "We provide health, life and vehicle insurance."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
