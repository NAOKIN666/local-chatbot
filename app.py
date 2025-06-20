from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/healthz")
def healthz():
    return "OK", 200

@app.route("/", methods=["GET", "POST"])
def chat():
    bot_reply = ""
    if request.method == "POST":
        user_input = request.form["text"]
        if user_input.strip():
            bot_reply = f"（ダミー応答）あなたの入力：{user_input}"
    return render_template("index.html", bot_reply=bot_reply)