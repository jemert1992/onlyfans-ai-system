import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>OnlyFans AI Communication System</h1><p>Deployment successful!</p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
