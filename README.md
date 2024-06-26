# VPN Connection App
### This Python application provides a user-friendly GUI interface to connect to a Virtual Private Network (VPN) using a Flask API backend. Users can enter their VPN server address, username, and password through the GUI, and the app sends a secure POST request to the Flask API to establish the VPN connection. The app also handles error cases, such as missing information or failed connection attempts, and displays relevant messages to the user using tkinter messagebox.

## Installation

1. Clone the repository:



2. Install the required Python packages:


## Usage

1. Run the Flask API:


2. Run the VPN connection app:


3. Enter the VPN server address, username, and password in the respective fields.
4. Click on the "Connect" button to establish the VPN connection.


## Flask API Code

3. Enter the VPN server address, username, and password in the respective fields.
4. Click on the "Connect" button to establish the VPN connection.

## Features

- GUI interface using tkinter for user interaction.
- Sends a POST request to the Flask API with VPN credentials.
- Displays connection status and messages using tkinter messagebox.

## Dependencies

- tkinter: Python's standard GUI library.
- requests: HTTP library for making API requests.
- Flask: Web framework for creating the VPN API.
- flask_cors: Flask extension for handling Cross-Origin Resource Sharing (CORS).

## Configuration

You can configure the Flask API endpoint in the `vpn_app.py` file by modifying the `API_ENDPOINT` variable.

## Flask API Code

```python
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/connect_to_vpn', methods=['POST'])
def connect_to_vpn():
 server_address = request.json.get('server_address')
 username = request.json.get('username')
 password = request.json.get('password')

 if server_address and username and password:
     # Your VPN connection logic here
     # Example: Connect to VPN using server_address, username, and password
     # VPNConnection.connect(server_address, username, password)

     return jsonify({"message": "Successfully connected to VPN"}), 200
 else:
     return jsonify({"error": "Please provide all the required information"}), 400

if __name__ == '__main__':
 app.run(debug=True)


```


## Contributing

Fork the repository.
Create a new branch (git checkout -b feature/your_feature).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/your_feature).
Create a new Pull Request.
## License

This project is licensed under the MIT License - see the LICENSE file for details.



