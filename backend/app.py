from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "Believe in yourself!",
    "Stay consistent and keep learning.",
    "Every expert was once a beginner.",
]

@app.route("/quote")
def quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
