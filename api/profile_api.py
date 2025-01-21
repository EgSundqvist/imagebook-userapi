from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from repositories.profile_repository import ProfileRepository
import logging

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profiles', methods=['POST'])
@jwt_required()
def create_profile():
    data = request.get_json()
    current_user_id = get_jwt_identity()
    logging.info(f'Creating profile for user_id: {current_user_id}')
    new_profile = ProfileRepository.create_profile(
        user_id=current_user_id,
        username=data['username'],
        bio=data.get('bio'),
        avatar=data.get('avatar')
    )
    logging.info(f'Profile created successfully for user_id: {current_user_id}, profile_id: {new_profile.id}')
    return jsonify({'message': 'Profile created successfully', 'profile_id': new_profile.id}), 201

@profile_bp.route('/profiles/current-profile', methods=['PUT'])
@jwt_required()
def update_current_profile():
    data = request.get_json()
    current_user_id = get_jwt_identity()
    logging.info(f'Updating profile for user_id: {current_user_id}')
    updated_profile = ProfileRepository.update_profile_by_user_id(
        user_id=current_user_id,
        username=data.get('username'),
        bio=data.get('bio'),
        avatar=data.get('avatar')
    )
    logging.info(f'Profile updated successfully for user_id: {current_user_id}, profile_id: {updated_profile.id}')
    return jsonify({
        'message': 'Profile updated successfully',
        'profile': {
            'id': updated_profile.id,
            'user_id': updated_profile.user_id,
            'username': updated_profile.username,
            'bio': updated_profile.bio,
            'avatar': updated_profile.avatar
        }
    }), 200

@profile_bp.route('/profiles/current-profile', methods=['GET'])
@jwt_required()
def get_profile():
    current_user_id = get_jwt_identity()
    logging.info(f'Fetching profile for user_id: {current_user_id}')
    profile = ProfileRepository.get_profile_by_user_id(current_user_id)
    if profile:
        logging.info(f'Profile found for user_id: {current_user_id}, profile_id: {profile.id}')
        return jsonify({
            'user_id': profile.user_id,
            'username': profile.username,
            'bio': profile.bio,
            'avatar': profile.avatar
        }), 200
    logging.warning(f'Profile not found for user_id: {current_user_id}')
    return jsonify({'message': 'Profile not found'}), 404