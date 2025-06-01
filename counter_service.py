from flask import Flask, jsonify

app = Flask(__name__)

# Initialize counter
counter = 0

@app.route('/counter', methods=['GET'])
def get_counter():
    """Get the current counter value"""
    return jsonify({'value': counter})

@app.route('/counter/increment', methods=['POST'])
def increment_counter():
    """Increment the counter value"""
    global counter
    counter += 1
    return jsonify({'value': counter})

if __name__ == '__main__':
    app.run(debug=True)