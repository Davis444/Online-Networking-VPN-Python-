import tkinter as tk
from tkinter import messagebox
import requests
import json  # Import JSON library for parsing

def connect_to_vpn():
    server_address = entry_server.get()
    username = entry_username.get()
    password = entry_password.get()

    if server_address and username and password:
        # Prepare data payload
        payload = {
            'server_address': server_address,
            'username': username,
            'password': password
        }

        # Send POST request to Flask API
        response = requests.post('http://127.0.0.1:5000/connect_to_vpn', json=payload)

        if response.status_code == 200:
            # Parse JSON response to extract message
            response_data = json.loads(response.text)
            message = response_data.get('message', 'Unknown response')
            messagebox.showinfo("VPN Connection", message)
        else:
            messagebox.showerror("Error", "Failed to connect to VPN.")
    else:
        messagebox.showerror("Error", "Please enter all the required information.")

# Create the main window
root = tk.Tk
