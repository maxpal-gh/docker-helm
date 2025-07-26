from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]


@app.route("/get-color", methods=["GET"])
def get_color():
    app_ver = "0"
    if os.path.exist('app_ver.txt'):
        with open('app_ver.txt', 'r') as f:
            app_ver = f.read().strip()

    return jsonify({
        "color": random.choice(COLORS),
        "app_ver": app_ver
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
