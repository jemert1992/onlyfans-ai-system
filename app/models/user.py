from app import db, bcrypt
from datetime import datetime

class User(db.Model):
    """User model for storing creator account details."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Style preferences
    flirtiness = db.Column(db.Integer, default=5)  # Scale 1-10
    friendliness = db.Column(db.Integer, default=5)  # Scale 1-10
    formality = db.Column(db.Integer, default=5)  # Scale 1-10
    
    # Automation preferences
    auto_respond_safe = db.Column(db.Boolean, default=True)
    auto_respond_low_risk = db.Column(db.Boolean, default=False)
    auto_respond_high_risk = db.Column(db.Boolean, default=False)
    
    # Relationships
    messages = db.relationship('Message', backref='user', lazy=True)
    
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat(),
            'style_preferences': {
                'flirtiness': self.flirtiness,
                'friendliness': self.friendliness,
                'formality': self.formality
            },
            'automation_preferences': {
                'auto_respond_safe': self.auto_respond_safe,
                'auto_respond_low_risk': self.auto_respond_low_risk,
                'auto_respond_high_risk': self.auto_respond_high_risk
            }
        }
