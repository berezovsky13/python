from flask import Flask, request
# AWS password - 123456789
# Daniel Token to his bank account - hljaldskfhaio9902&^*
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/echo")
def echo():
    text = request.args.get("q", "no input")
    return f"You said: {text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
