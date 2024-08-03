from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    return jsonify({'message': 'Hello World!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
