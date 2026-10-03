from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify(message="hello from platform-dev", version="0.1.0")

@app.get("/healthz")
def healthz():
    return jsonify(status="ok")
