from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)
generator = pipeline("text-generation", model="rinna/japanese-gpt2-small")

@app.route("/healthz")
def healthz():
    return "OK", 200

@app.route("/", methods=["GET", "POST"])
def chat():
    bot_reply = ""
    if request.method == "POST":
        user_input = request.form["text"]
        if user_input.strip():
            response = generator(user_input, max_new_tokens=50)
            bot_reply = response[0]["generated_text"][len(user_input):].strip()
    return render_template("index.html", bot_reply=bot_reply)
