import os
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Sample messages for demonstration
sample_messages = [
    {"id": 1, "content": "Hey, I really loved your latest photoshoot! The lighting was amazing.", "risk_level": "safe"},
    {"id": 2, "content": "Would you consider doing more beach content? Those are my favorites!", "risk_level": "low-risk"},
    {"id": 3, "content": "Can we meet up privately? I'll pay extra...", "risk_level": "high-risk"},
    {"id": 4, "content": "Just renewed my subscription. Your content is worth every penny!", "risk_level": "safe"},
    {"id": 5, "content": "Do you offer custom content? I have some ideas I'd like to discuss.", "risk_level": "low-risk"}
]

# Sample response styles
response_styles = {
    "professional": {
        "flirtiness": 3,
        "friendliness": 7,
        "formality": 8,
        "sample": "Thank you for your support! I appreciate your feedback on my content."
    },
    "casual": {
        "flirtiness": 5,
        "friendliness": 8,
        "formality": 4,
        "sample": "Thanks so much! 😊 I'm really happy you're enjoying my content!"
    },
    "flirty": {
        "flirtiness": 8,
        "friendliness": 7,
        "formality": 3,
        "sample": "Aww you're so sweet! 💕 I love knowing you enjoy my content... stay tuned for more soon! 😘"
    }
}

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
            body { padding-top: 20px; padding-bottom: 40px; }
            .message { border: 1px solid #ddd; padding: 15px; margin: 15px 0; border-radius: 5px; }
            .safe { background-color: #e8f5e9; border-left: 5px solid #4caf50; }
            .low-risk { background-color: #fff8e1; border-left: 5px solid #ffc107; }
            .high-risk { background-color: #ffebee; border-left: 5px solid #f44336; }
            .slider-container { margin-bottom: 20px; }
            .nav-pills .nav-link.active { background-color: #6c757d; }
            .response-preview { border: 1px solid #ddd; padding: 15px; border-radius: 5px; margin-top: 15px; }
            .stats-card { text-align: center; padding: 20px; border-radius: 5px; margin-bottom: 20px; }
            .stats-card h3 { margin-bottom: 0; }
            .stats-card p { margin-top: 5px; opacity: 0.7; }
            .tab-content { display: none; }
            .tab-content.active { display: block; }
        </style>
    </head>
    <body>
        <div class="container">
            <header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
                <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
                    <span class="fs-4">OnlyFans AI Communication System</span>
                </a>
                <ul class="nav nav-pills" id="main-nav">
                    <li class="nav-item"><a href="#dashboard" class="nav-link active" data-tab="dashboard">Dashboard</a></li>
                    <li class="nav-item"><a href="#messages" class="nav-link" data-tab="messages">Messages</a></li>
                    <li class="nav-item"><a href="#settings" class="nav-link" data-tab="settings">Settings</a></li>
                    <li class="nav-item"><a href="#help" class="nav-link" data-tab="help">Help</a></li>
                </ul>
            </header>

            <div id="dashboard" class="tab-content active">
                <h2 class="mb-4">Dashboard</h2>
                
                <div class="row mb-4">
                    <div class="col-md-4">
                        <div class="stats-card bg-primary text-white">
                            <h3>42</h3>
                            <p>New Messages</p>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="stats-card bg-success text-white">
                            <h3>85%</h3>
                            <p>Safe Messages</p>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="stats-card bg-warning text-dark">
                            <h3>15%</h3>
                            <p>Flagged Messages</p>
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-md-6">
                        <div class="card mb-4">
                            <div class="card-header bg-dark text-white">
                                Message Filtering Demo
                            </div>
                            <div class="card-body">
                                <p>The system automatically categorizes incoming messages based on content analysis:</p>
                                
                                <div class="message safe">
                                    <h5>Safe Message</h5>
                                    <p>"Hey, I really loved your latest photoshoot! The lighting was amazing."</p>
                                </div>
                                
                                <div class="message low-risk">
                                    <h5>Low-Risk Message</h5>
                                    <p>"Would you consider doing more beach content? Those are my favorites!"</p>
                                </div>
                                
                                <div class="message high-risk">
                                    <h5>High-Risk Message</h5>
                                    <p>"Can we meet up privately? I'll pay extra..."</p>
                                    <div class="alert alert-danger mt-2 mb-0">
                                        <small>This message has been flagged for review due to potential safety concerns.</small>
                                    </div>
                                </div>

                                <div class="mt-4">
                                    <h5>Try it yourself:</h5>
                                    <div class="input-group mb-3">
                                        <input type="text" id="message-input" class="form-control" placeholder="Type a message to test filtering...">
                                        <button class="btn btn-outline-secondary" type="button" id="filter-button">Filter</button>
                                    </div>
                                    <div id="filter-result" class="d-none message">
                                        <h5>Result:</h5>
                                        <p id="filter-message"></p>
                                        <div id="filter-alert" class="alert mt-2 mb-0">
                                            <small id="filter-explanation"></small>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-6">
                        <div class="card mb-4">
                            <div class="card-header bg-dark text-white">
                                Response Style Customization
                            </div>
                            <div class="card-body">
                                <p>Adjust these parameters to customize your automated response style:</p>
                                
                                <div class="slider-container">
                                    <label for="flirtiness" class="form-label">Flirtiness: <span id="flirtiness-value">5</span></label>
                                    <input type="range" class="form-range style-slider" min="1" max="10" value="5" id="flirtiness">
                                </div>
                                
                                <div class="slider-container">
                                    <label for="friendliness" class="form-label">Friendliness: <span id="friendliness-value">7</span></label>
                                    <input type="range" class="form-range style-slider" min="1" max="10" value="7" id="friendliness">
                                </div>
                                
                                <div class="slider-container">
                                    <label for="formality" class="form-label">Formality: <span id="formality-value">4</span></label>
                                    <input type="range" class="form-range style-slider" min="1" max="10" value="4" id="formality">
                                </div>

                                <div class="mt-4">
                                    <h5>Response Preview:</h5>
                                    <div class="response-preview" id="response-preview">
                                        Thanks so much! 😊 I'm really happy you're enjoying my content!
                                    </div>
                                </div>

                                <div class="mt-4">
                                    <h5>Preset Styles:</h5>
                                    <div class="btn-group w-100" role="group">
                                        <button type="button" class="btn btn-outline-secondary preset-button" data-preset="professional">Professional</button>
                                        <button type="button" class="btn btn-outline-secondary preset-button active" data-preset="casual">Casual</button>
                                        <button type="button" class="btn btn-outline-secondary preset-button" data-preset="flirty">Flirty</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div id="messages" class="tab-content">
                <h2 class="mb-4">Messages</h2>
                <div class="card mb-4">
                    <div class="card-header bg-dark text-white">
                        Recent Messages
                    </div>
                    <div class="card-body p-0">
                        <div class="list-group list-group-flush">
                            <a href="#" class="list-group-item list-group-item-action">
                                <div class="d-flex w-100 justify-content-between">
                                    <h5 class="mb-1">Subscriber #1042</h5>
                                    <small class="text-muted">3 days ago</small>
                                </div>
                                <p class="mb-1">Just renewed my subscription. Your content is worth every penny!</p>
                                <small class="text-success">Safe</small>
                            </a>
                            <a href="#" class="list-group-item list-group-item-action">
                                <div class="d-flex w-100 justify-content-between">
                                    <h5 class="mb-1">Subscriber #836</h5>
                                    <small class="text-muted">1 week ago</small>
                                </div>
                                <p class="mb-1">Do you offer custom content? I have some ideas I'd like to discuss.</p>
                                <small class="text-warning">Low-Risk</small>
                            </a>
                            <a href="#" class="list-group-item list-group-item-action">
                                <div class="d-flex w-100 justify-content-between">
                                    <h5 class="mb-1">Subscriber #1204</h5>
                                    <small class="text-muted">2 weeks ago</small>
                                </div>
                                <p class="mb-1">Hey, I really loved your latest photoshoot! The lighting was amazing.</p>
                                <small class="text-success">Safe</small>
                            </a>
                        </div>
                    </div>
                </div>
            </div>

            <div id="settings" class="tab-content">
                <h2 class="mb-4">Settings</h2>
                <div class="card mb-4">
                    <div class="card-header bg-dark text-white">
                        Account Settings
                    </div>
                    <div class="card-body">
                        <form>
                            <div class="mb-3">
                                <label for="username" class="form-label">Username</label>
                                <input type="text" class="form-control" id="username" value="creator123">
                            </div>
                            <div class="mb-3">
                                <label for="email" class="form-label">Email</label>
                                <input type="email" class="form-control" id="email" value="creator@example.com">
                            </div>
                            <div class="mb-3">
                                <label for="password" class="form-label">Password</label>
                                <input type="password" class="form-control" id="password" value="********">
                            </div>
                            <button type="button" class="btn btn-primary">Save Changes</button>
                        </form>
                    </div>
                </div>
            </div>

            <div id="help" class="tab-content">
                <h2 class="mb-4">Help & Support</h2>
                <div class="card mb-4">
                    <div class="card-header bg-dark text-white">
                        Frequently Asked Questions
                    </div>
                    <div class="card-body">
                        <div class="accordion" id="faqAccordion">
                            <div class="accordion-item">
                                <h2 class="accordion-header">
                                    <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#faq1">
                                        How does the message filtering work?
                                    </button>
                                </h2>
                                <div id="faq1" class="accordion-collapse collapse show" data-bs-parent="#faqAccordion">
                                    <div class="accordion-body">
                                        Our AI system analyzes incoming messages for content, tone, and intent. It categorizes messages as safe, low-risk, or high-risk based on this analysis, helping you prioritize which messages need your personal attention.
                                    </div>
                                </div>
                            </div>
                            <div class="accordion-item">
                                <h2 class="accordion-header">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq2">
                                        Can I customize the response style?
                                    </button>
                                </h2>
                                <div id="faq2" class="accordion-collapse collapse" data-bs-parent="#faqAccordion">
                                    <div class="accordion-body">
                                        Yes! You can adjust parameters like flirtiness, friendliness, and formality to match your personal communication style. These settings affect how automated responses are generated.
                                    </div>
                                </div>
                            </div>
                            <div class="accordion-item">
                                <h2 class="accordion-header">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq3">
                                        Is my data secure?
                                    </button>
                                </h2>
                                <div id="faq3" class="accordion-collapse collapse" data-bs-parent="#faqAccordion">
                                    <div class="accordion-body">
                                        Absolutely. We use industry-standard encryption and security practices to protect your data. Your messages and subscriber information are never shared with third parties.
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <footer class="pt-4 my-md-5 pt-md-5 border-top">
                <div class="row">
                    <div class="col-12 col-md">
                        <small class="d-block mb-3 text-muted">© 2025 OnlyFans AI Communication System</small>
                    </div>
                    <div class="col-6 col-md">
                        <h5>Features</h5>
                        <ul class="list-unstyled text-small">
                            <li><a class="text-muted" href="#">Message Filtering</a></li>
                            <li><a class="text-muted" href="#">Response Generation</a></li>
                            <li><a class="text-muted" href="#">Voice Training</a></li>
                        </ul>
                    </div>
                    <div class="col-6 col-md">
                        <h5>Resources</h5>
                        <ul class="list-unstyled text-small">
                            <li><a class="text-muted" href="#">Documentation</a></li>
                            <li><a class="text-muted" href="#">Tutorials</a></li>
                            <li><a class="text-muted" href="#">Support</a></li>
                        </ul>
                    </div>
                    <div class="col-6 col-md">
                        <h5>About</h5>
                        <ul class="list-unstyled text-small">
                            <li><a class="text-muted" href="#">Team</a></li>
                            <li><a class="text-muted" href="#">Privacy</a></li>
                            <li><a class="text-muted" href="#">Terms</a></li>
                        </ul>
                    </div>
                </div>
            </footer>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
        <script>
            // Tab navigation functionality
            document.addEventListener('DOMContentLoaded', function() {
                const navLinks = document.querySelectorAll('#main-nav .nav-link');
                const tabContents = document.querySelectorAll('.tab-content');
                
                navLinks.forEach(link => {
                    link.addEventListener('click', function(e) {
                        e.preventDefault();
                        
                        // Remove active class from all links and tabs
                        navLinks.forEach(l => l.classList.remove('active'));
                        tabContents.forEach(t => t.classList.remove('active'));
                        
                        // Add active class to clicked link and corresponding tab
                        this.classList.add('active');
                        const tabId = this.getAttribute('data-tab');
                        document.getElementById(tabId).classList.add('active');
                    });
                });
                
                // Message filtering functionality
                const filterButton = document.getElementById('filter-button');
                if (filterButton) {
                    filterButton.addEventListener('click', function() {
                        const messageInput = document.getElementById('message-input');
                        const message = messageInput.value.trim();
                        
                        if (message) {
                            const filterResult = document.getElementById('filter-result');
                            const filterMessage = document.getElementById('filter-message');
                            const filterAlert = document.getElementById('filter-alert');
                            const filterExplanation = document.getElementById('filter-explanation');
                            
                            filterMessage.textContent = message;
                            filterResult.classList.remove('d-none', 'safe', 'low-risk', 'high-risk');
                            filterAlert.classList.remove('alert-success', 'alert-warning', 'alert-danger');
                            
                            // Simple filtering logic
                            const lowRiskWords = ['custom', 'private', 'special', 'request', 'personal'];
                            const highRiskWords = ['meet', 'hotel', 'address', 'location', 'phone', 'number', 'extra'];
                            
                            let riskLevel = 'safe';
                            if (lowRiskWords.some(word => message.toLowerCase().includes(word))) {
                                riskLevel = 'low-risk';
                            }
                            if (highRiskWords.some(word => message.toLowerCase().includes(word))) {
                                riskLevel = 'high-risk';
                            }
                            
                            filterResult.classList.add(riskLevel);
                            
                            if (riskLevel === 'safe') {
                                filterAlert.classList.add('alert-success');
                                filterExplanation.textContent = 'This message is safe and can be automatically responded to.';
                            } else if (riskLevel === 'low-risk') {
                                filterAlert.classList.add('alert-warning');
                                filterExplanation.textContent = 'This message has been flagged as low-risk. Review recommended before responding.';
                            } else {
                                filterAlert.classList.add('alert-danger');
                                filterExplanation.textContent = 'This message has been flagged for review due to potential safety concerns.';
                            }
                            
                            filterResult.classList.remove('d-none');
                        }
                    });
                }
                
                // Response style customization
                const styleSliders = document.querySelectorAll('.style-slider');
                if (styleSliders.length > 0) {
                    styleSliders.forEach(slider => {
                        slider.addEventListener('input', updateResponsePreview);
                    });
                }
                
                function updateResponsePreview() {
                    const flirtiness = parseInt(document.getElementById('flirtiness').value);
                    const friendliness = parseInt(document.getElementById('friendliness').value);
                    const formality = parseInt(document.getElementById('formality').value);
                    
                    document.getElementById('flirtiness-value').textContent = flirtiness;
                    document.getElementById('friendliness-value').textContent = friendliness;
                    document.getElementById('formality-value').textContent = formality;
                    
                    let response = '';
                    
                    if (flirtiness >= 7 && friendliness >= 6) {
                        response = 'Aww you\'re so sweet! 💕 I love knowing you enjoy my content... stay tuned for more soon! 😘';
                    } else if (flirtiness >= 5 && friendliness >= 5) {
                        response = 'Thanks so much! 😊 I\'m really happy you\'re enjoying my content!';
                    } else if (formality >= 7) {
                        response = 'Thank you for your support! I appreciate your feedback on my content.';
                    } else {
                        response = 'Thanks! Glad you\'re enjoying the content.';
                    }
                    
                    document.getElementById('response-preview').textContent = response;
                }
                
                // Preset styles
                const presetButtons = document.querySelectorAll('.preset-button');
                if (presetButtons.length > 0) {
                    presetButtons.forEach(button => {
                        button.addEventListener('click', function() {
                            presetButtons.forEach(btn => btn.classList.remove('active'));
                            this.classList.add('active');
                            
                            const preset = this.getAttribute('data-preset');
                            if (preset === 'professional') {
                                document.getElementById('flirtiness').value = 3;
                                document.getElementById('friendliness').value = 7;
                                document.getElementById('formality').value = 8;
                            } else if (preset === 'casual') {
                                document.getElementById('flirtiness').value = 5;
                                document.getElementById('friendliness').value = 7;
                                document.getElementById('formality').value = 4;
                            } else if (preset === 'flirty') {
                                document.getElementById('flirtiness').value = 8;
                                document.getElementById('friendliness').value = 7;
                                document.getElementById('formality').value = 3;
                            }
                            
                            updateResponsePreview();
                        });
                    });
                }
            });
        </script>
    </body>
    </html>
    ''')

@app.route('/api/filter', methods=['POST'])
def filter_message():
    data = request.json
    message = data.get('message', '')
    
    # Simple filtering logic
    low_risk_words = ['custom', 'private', 'special', 'request', 'personal']
    high_risk_words = ['meet', 'hotel', 'address', 'location', 'phone', 'number', 'extra']
    
    risk_level = "safe"
    if any(word in message.lower() for word in low_risk_words):
        risk_level = "low-risk"
    if any(word in message.lower() for word in high_risk_words):
        risk_level = "high-risk"
        
    return jsonify({
        "message": message,
        "risk_level": risk_level
    })

@app.route('/api/generate-response', methods=['POST'])
def generate_response():
    data = request.json
    flirtiness = data.get('flirtiness', 5)
    friendliness = data.get('friendliness', 7)
    formality = data.get('formality', 4)
    
    response = ""
    if flirtiness >= 7 and friendliness >= 6:
        response = "Aww you're so sweet! 💕 I love knowing you enjoy my content... stay tuned for more soon! 😘"
    elif flirtiness >= 5 and friendliness >= 5:
        response = "Thanks so much! 😊 I'm really happy you're enjoying my content!"
    elif formality >= 7:
        response = "Thank you for your support! I appreciate your feedback on my content."
    else:
        response = "Thanks! Glad you're enjoying the content."
    
    return jsonify({
        "response": response
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
