from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from repositories.user_repository import UserRepository
import logging

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['POST'])
@jwt_required()
def create_user():
    data = request.get_json()
    current_user_id = get_jwt_identity()
    new_user = UserRepository.create_user(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        password=data['password']
    )
    logging.info(f'User created successfully: user_id={new_user.id}')
    return jsonify({'message': 'User created successfully', 'user_id': new_user.id}), 201

@user_bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    current_user_id = get_jwt_identity()
    users = UserRepository.get_all_users()
    logging.info(f'Fetched all users by user_id={current_user_id}')
    return jsonify([user.email for user in users]), 200

@user_bp.route('/users/current_user', methods=['GET'])
@jwt_required()
def get_current_user():
    current_user_id = get_jwt_identity()
    user = UserRepository.get_user_by_id(current_user_id)
    if user:
        logging.info(f'Fetched current user: user_id={current_user_id}')
        return jsonify({
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }), 200
    logging.warning(f'User not found: user_id={current_user_id}')
    return jsonify({'message': 'User not found'}), 404

@user_bp.route('/users/change_password', methods=['PUT'])
@jwt_required()
def change_password():
    data = request.get_json()
    current_user_id = get_jwt_identity()
    old_password = data['old_password']
    new_password = data['new_password']
    if UserRepository.update_password(current_user_id, old_password, new_password):
        logging.info(f'Password updated successfully for user_id={current_user_id}')
        return jsonify({'message': 'Password updated successfully'}), 200
    logging.warning(f'Failed to update password for user_id={current_user_id}')
    return jsonify({'message': 'Invalid old password'}), 400