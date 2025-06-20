from flask import Flask, request, render_template_string
from transformers import pipeline

app = Flask(__name__)
generator = pipeline("text-generation", model="rinna/japanese-gpt2-small")

HTML = """
<!doctype html>
<title>ローカルチャットボット</title>
<h1>ローカルチャットボット</h1>
<form method=post>
    あなた：<input name=text>
    <input type=submit value=送信>
</form>
<p>ボット：{{ bot_reply}}</p>
"""
@app.route("/", methods=["GET", "POST"])
def chat():
    bot_reply = ""
    if request.method == "POST":
        user_input = request.form["text"]
        response = generator(user_input, max_new_tokens=50)
        bot_reply = response[0]["generated_text"][len(user_input):].strip()
    return render_template_string(HTML, bot_reply=bot_reply)

if __name__ == "__main__":
    app.run(debug=True)