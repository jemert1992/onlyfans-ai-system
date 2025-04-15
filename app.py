import os
import sys

# Print debugging information
print(f"Current directory: {os.getcwd()}")
print(f"Directory contents: {os.listdir('.')}")

# Create a simple Flask app for testing
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World! This is a test page for the OnlyFans AI Communication System."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
