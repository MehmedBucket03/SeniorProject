from flask import Flask, jsonify

# Initialize Flask application
app = Flask(__name__)

@app.route('/')
def home():
    """Handles the root route and returns a welcome message."""
    return jsonify({"message": "Hello from Algomatics Backend!"})

if __name__ == "__main__":
    print("🔥 Running Flask API on http://127.0.0.1:5000/")
    app.run(host="0.0.0.0", port=5000, debug=True)  # Debug mode enables auto-restart
