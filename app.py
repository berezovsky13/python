# app.py
from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/cmd")
def cmd():
    # ⚠️ SECURITY ISSUE: This executes any shell command passed in query param
    command = request.args.get("q", "echo no input")
    return os.popen(command).read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
