import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>OnlyFans AI Communication System</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container mt-5">
            <h1>OnlyFans AI Communication System</h1>
            <p class="lead">A revolutionary way for OnlyFans creators to manage their communications</p>
            <div class="alert alert-success">
                <h4>Deployment Successful!</h4>
                <p>This basic version confirms that your Heroku deployment is working.</p>
            </div>
            <div class="card mt-4">
                <div class="card-header">Features</div>
                <div class="card-body">
                    <ul>
                        <li>Automated message filtering</li>
                        <li>Customizable response generation</li>
                        <li>User-friendly dashboard</li>
                        <li>Secure authentication</li>
                    </ul>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000) )
    app.run(host="0.0.0.0", port=port)
