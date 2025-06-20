# 今のapp.py の generator の部分をコメントアウト
# generator = pipeline("text-generation", model="rinna/japanese-gpt2-small")

@app.route("/", methods=["GET", "POST"])
def chat():
    bot_reply = ""
    if request.method == "POST":
        user_input = request.form["text"]
        if user_input.strip():
            # bot_reply = 実際の推論の代わりに固定返答
            bot_reply = f"（ダミー応答）あなたの入力：{user_input}"
    return render_template("index.html", bot_reply=bot_reply)
