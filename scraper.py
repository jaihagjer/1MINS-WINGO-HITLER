
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    latest_result = "Big"  # Dummy result for now
    prediction = "Small"   # Dummy prediction
    return jsonify({
        "latest": latest_result,
        "prediction": prediction
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
