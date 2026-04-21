from flask import Flask, jsonify
from retry import retry_request
from logger import log

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Fault-Tolerant API running"})

@app.route("/data")
def get_data():
    try:
        result = retry_request()
        return jsonify({"status": "success", "data": result})
    except Exception as e:
        log(f"Final failure: {str(e)}")
        return jsonify({"status": "error", "message": "Service unavailable"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
