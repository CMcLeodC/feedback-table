from flask import Flask

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return "Test route is working!"

@app.route('/feedback', methods=['GET'])
def feedback():
    return "Feedback route is working!"

if __name__ == '__main__':
    app.run(debug=True)
