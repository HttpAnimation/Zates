from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/test', methods=['GET'])
def test_endpoint():
    return jsonify({"message": "This is a test response from the backend!"})

if __name__ == '__main__':
    app.run(debug=True)
