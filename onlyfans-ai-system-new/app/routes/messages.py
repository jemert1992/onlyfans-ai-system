from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User, Message, Response
from app.services import MessageFilter, ResponseGenerator
from app import db

messages_bp = Blueprint('messages', __name__)
message_filter = MessageFilter()
response_generator = ResponseGenerator()

@messages_bp.route('/', methods=['GET'])
@jwt_required()
def get_messages():
    """Get all messages for the current user."""
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    messages = Message.query.filter_by(user_id=current_user_id).order_by(Message.created_at.desc()).all()
    return jsonify({
        'messages': [message.to_dict() for message in messages]
    }), 200

@messages_bp.route('/<int:message_id>', methods=['GET'])
@jwt_required()
def get_message(message_id):
    """Get a specific message by ID."""
    current_user_id = get_jwt_identity()
    
    message = Message.query.filter_by(id=message_id, user_id=current_user_id).first()
    if not message:
        return jsonify({'error': 'Message not found'}), 404
    
    return jsonify(message.to_dict()), 200

@messages_bp.route('/', methods=['POST'])
@jwt_required()
def create_message():
    """Create a new message and generate a response."""
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.json
    if not data or 'content' not in data or 'sender_name' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Create new message
    message = Message(
        user_id=current_user_id,
        sender_name=data['sender_name'],
        content=data['content']
    )
    
    # Process message with filter
    message = message_filter.process_message(message)
    
    # Save message to database
    db.session.add(message)
    db.session.commit()
    
    # Generate automated response if appropriate
    should_auto_respond = False
    if message.risk_level == 'safe' and user.auto_respond_safe:
        should_auto_respond = True
    elif message.risk_level == 'low_risk' and user.auto_respond_low_risk:
        should_auto_respond = True
    elif message.risk_level == 'high_risk' and user.auto_respond_high_risk:
        should_auto_respond = True
    
    response_data = {}
    if should_auto_respond:
        response_text = response_generator.generate_response(message, user)
        response = Response(
            message_id=message.id,
            content=response_text,
            is_automated=True
        )
        db.session.add(response)
        db.session.commit()
        message.is_responded = True
        db.session.commit()
        response_data = response.to_dict()
    
    return jsonify({
        'message': message.to_dict(),
        'auto_response': response_data if should_auto_respond else None
    }), 201

@messages_bp.route('/<int:message_id>/respond', methods=['POST'])
@jwt_required()
def respond_to_message(message_id):
    """Create a manual response to a message."""
    current_user_id = get_jwt_identity()
    
    message = Message.query.filter_by(id=message_id, user_id=current_user_id).first()
    if not message:
        return jsonify({'error': 'Message not found'}), 404
    
    data = request.json
    if not data or 'content' not in data:
        return jsonify({'error': 'Missing response content'}), 400
    
    response = Response(
        message_id=message.id,
        content=data['content'],
        is_automated=False
    )
    
    db.session.add(response)
    message.is_responded = True
    db.session.commit()
    
    return jsonify(response.to_dict()), 201
