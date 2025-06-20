from flask import Flask, request, render_template
from transformers import pipeline
import os

app = Flask(__name__)
generator = pipeline("text-generation", model="rinna/japanese-gpt2-small")

@app.route("/", methods=["GET", "POST"])
def chat():
    bot_reply = ""
    if request.method == "POST":
        user_input = request.form["text"]
        if user_input.strip():
            response = generator(user_input, max_new_tokens=50)
            bot_reply = response[0]["generated_text"][len(user_input):].strip()
    return render_template("index.html", bot_reply=bot_reply)

@app.route("/healthz")
def healthz():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)