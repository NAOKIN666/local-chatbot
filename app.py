from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_input = request.form["text"]
        if user_input.strip():
            bot_reply = f"（ダミー応答）あなたの入力：{user_input}"
            return redirect(url_for("chat", reply=bot_reply))
    bot_reply = request.args.get("reply", "")
    return render_template("index.html", bot_reply=bot_reply)