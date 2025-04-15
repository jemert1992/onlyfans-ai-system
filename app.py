import os
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>OnlyFans AI Communication System</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { padding: 20px; }
            .message { border: 1px solid #ddd; padding: 15px; margin: 15px 0; border-radius: 5px; }
            .safe { background-color: #e8f5e9; }
            .low-risk { background-color: #fff8e1; }
            .high-risk { background-color: #ffebee; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="mt-4 mb-4">OnlyFans AI Communication System</h1>
            <p class="lead">A revolutionary way for OnlyFans creators to manage their communications</p>
            
            <div class="card mb-4">
                <div class="card-header bg-primary text-white">
                    Message Filtering Demo
                </div>
                <div class="card-body">
                    <div class="message safe">
                        <h5>Safe Message</h5>
                        <p>"Thanks for the great content! Looking forward to more."</p>
                    </div>
                    <div class="message low-risk">
                        <h5>Low-Risk Message</h5>
                        <p>"Would you consider making more content like your beach photoshoot?"</p>
                    </div>
                    <div class="message high-risk">
                        <h5>High-Risk Message</h5>
                        <p>[Content filtered for inappropriate requests]</p>
                    </div>
                </div>
            </div>
            
            <div class="card mb-4">
                <div class="card-header bg-success text-white">
                    Response Customization
                </div>
                <div class="card-body">
                    <h5>Adjust your response style:</h5>
                    <div class="mb-3">
                        <label>Flirtiness:</label>
                        <input type="range" class="form-range" min="1" max="10" value="5">
                    </div>
                    <div class="mb-3">
                        <label>Friendliness:</label>
                        <input type="range" class="form-range" min="1" max="10" value="7">
                    </div>
                    <div class="mb-3">
                        <label>Formality:</label>
                        <input type="range" class="form-range" min="1" max="10" value="3">
                    </div>
                </div>
            </div>
            
            <div class="alert alert-info">
                <p>This is a demonstration of the OnlyFans AI Communication System.</p>
                <p>The full version includes:</p>
                <ul>
                    <li>Automated message filtering</li>
                    <li>Customizable response generation</li>
                    <li>User-friendly dashboard</li>
                    <li>Secure authentication</li>
                </ul>
            </div>
        </div>
        
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    ''') 

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
