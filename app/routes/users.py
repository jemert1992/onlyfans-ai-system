from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User
from app import db

users_bp = Blueprint('users', __name__)

@users_bp.route('/', methods=['GET'])
@jwt_required()
def get_current_user():
    """Get the current user's profile."""
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify(user.to_dict()), 200

@users_bp.route('/style', methods=['PUT'])
@jwt_required()
def update_style_preferences():
    """Update the current user's style preferences."""
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # Update style preferences
    if 'flirtiness' in data:
        user.flirtiness = data['flirtiness']
    if 'friendliness' in data:
        user.friendliness = data['friendliness']
    if 'formality' in data:
        user.formality = data['formality']
    
    db.session.commit()
    
    return jsonify({
        'message': 'Style preferences updated successfully',
        'user': user.to_dict()
    }), 200

@users_bp.route('/automation', methods=['PUT'])
@jwt_required()
def update_automation_preferences():
    """Update the current user's automation preferences."""
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # Update automation preferences
    if 'auto_respond_safe' in data:
        user.auto_respond_safe = data['auto_respond_safe']
    if 'auto_respond_low_risk' in data:
        user.auto_respond_low_risk = data['auto_respond_low_risk']
    if 'auto_respond_high_risk' in data:
        user.auto_respond_high_risk = data['auto_respond_high_risk']
    
    db.session.commit()
    
    return jsonify({
        'message': 'Automation preferences updated successfully',
        'user': user.to_dict()
    }), 200

@users_bp.route('/password', methods=['PUT'])
@jwt_required()
def update_password():
    """Update the current user's password."""
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.json
    if not data or 'current_password' not in data or 'new_password' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Verify current password
    if not user.check_password(data['current_password']):
        return jsonify({'error': 'Current password is incorrect'}), 401
    
    # Update password
    user.set_password(data['new_password'])
    db.session.commit()
    
    return jsonify({'message': 'Password updated successfully'}), 200
