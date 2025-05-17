from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/results')
def results():
    # Ye dummy data hai, aap isme real scraping code add kar sakte hain
    data = ["B", "S", "B", "B", "S"]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)