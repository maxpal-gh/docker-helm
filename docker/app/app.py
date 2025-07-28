from flask import Flask, jsonify, request
import random
import os
import logging
import socket

app = Flask(__name__)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]


@app.route("/get-color", methods=["GET"])
def get_color():
    app_ver = "0"
    if os.path.exists('app_ver.txt'):
        with open('app_ver.txt', 'r') as f:
            app_ver = f.read().strip()

    chosen_color = random.choice(COLORS)
    hostname = socket.gethostname()  # <-- Get the hostname

    logger.info(f"Received request from {request.remote_addr}, returning color '{chosen_color}', app_ver '{app_ver}', hostname '{hostname}'")

    return jsonify({
        "color": chosen_color,
        "app_ver": app_ver,
        "hostname": hostname  # <-- Add it to response
    })


if __name__ == "__main__":
    logger.info("Starting Flask server on port 5000")
    app.run(host="0.0.0.0", port=5000)
