from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def generate_password(length, use_symbols):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/generate_password', methods=['POST'])
def handle_generate_password():
    data = request.get_json()  # Extract data from POST request
    length = data.get('length', 12)  # Default length to 12 if not specified
    use_symbols = data.get('useSymbols', False)  # Default to False if not specified

    if not isinstance(length, int) or not isinstance(use_symbols, bool):
        return jsonify({"error": "Invalid input parameters"}), 400

    password = generate_password(length, use_symbols)
    return jsonify(password=password)

if __name__ == '__main__':
    app.run(debug=True)
