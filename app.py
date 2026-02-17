from flask import Flask, render_template, request, jsonify
from database import init_db, save_chat, get_chat_history
from nlp import get_response

app = Flask(__name__)

init_db()

@app.route("/")
def index():
    history = get_chat_history()
    return render_template("index.html", history=history)

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message")

        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400

        bot_response = get_response(user_message)
        save_chat(user_message, bot_response)

        return jsonify({"response": bot_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
