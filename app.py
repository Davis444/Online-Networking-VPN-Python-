from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Your route definitions and other app code here

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/connect_to_vpn', methods=['POST'])
def connect_to_vpn():
    # Your VPN connection logic here
    return jsonify({"message": "Successfully connected to VPN"}), 200

if __name__ == '__main__':
    app.run(debug=True)
