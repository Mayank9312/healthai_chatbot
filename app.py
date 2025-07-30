from flask import Flask, render_template, request, jsonify, session
import requests

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # required for using session

@app.route("/")
def home():
    session["chat_history"] = []  # reset conversation on home page load
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").strip()

    if not user_input:
        return jsonify(response="❌ Please enter a valid message.")

    # 🧠 Get previous conversation or start new
    chat_history = session.get("chat_history", [])

    # Add current user message
    chat_history.append(f"User: {user_input}")

    # Combine all messages into one prompt
    prompt = "You are a smart AI health assistant. Help the user based on the conversation.\n\n"
    prompt += "\n".join(chat_history)
    prompt += "\nAI:"

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama2",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()
        reply = data["response"].strip()

        # Save bot reply in memory
        chat_history.append(f"AI: {reply}")
        session["chat_history"] = chat_history  # update session

        return jsonify(response=reply)

    except Exception as e:
        print("❌ Ollama API Exception:", str(e))
        return jsonify(response="❌ Local AI error. Please make sure Ollama is running.")

if __name__ == "__main__":
    app.run(debug=True)
