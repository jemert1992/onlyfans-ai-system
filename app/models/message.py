from app import db
from datetime import datetime
from enum import Enum

class RiskLevel(Enum):
    SAFE = 'safe'
    LOW_RISK = 'low_risk'
    HIGH_RISK = 'high_risk'

class Message(db.Model):
    """Message model for storing fan messages and responses."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sender_name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    risk_level = db.Column(db.String(20), default=RiskLevel.SAFE.value)
    is_filtered = db.Column(db.Boolean, default=False)
    is_responded = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship with responses
    responses = db.relationship('Response', backref='message', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'sender_name': self.sender_name,
            'content': self.content,
            'risk_level': self.risk_level,
            'is_filtered': self.is_filtered,
            'is_responded': self.is_responded,
            'created_at': self.created_at.isoformat(),
            'responses': [response.to_dict() for response in self.responses]
        }

class Response(db.Model):
    """Response model for storing automated or manual responses to messages."""
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    is_automated = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'message_id': self.message_id,
            'content': self.content,
            'is_automated': self.is_automated,
            'created_at': self.created_at.isoformat()
        }
