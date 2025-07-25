from flask import Flask, jsonify
import random

app = Flask(__name__)

COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]


@app.route("/get-color", methods=["GET"])
def get_color():
    return jsonify({"color": random.choice(COLORS)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
