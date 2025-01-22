from flask import Blueprint, request, jsonify
from repositories.user_repository import UserRepository
from repositories.profile_repository import ProfileRepository
from repositories.register_repository import RegisterRepository

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['POST'])
def register_user_and_profile():
    data = request.get_json()
    email = data['email']
    username = data['username']

    if UserRepository.get_user_by_email(email):
        return jsonify({'message': 'Email address already in use'}), 400

    if ProfileRepository.get_profile_by_username(username):
        return jsonify({'message': 'Username already in use'}), 400

    try:
        new_user, new_profile = RegisterRepository.register_user_and_profile(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=email,
            password=data['password'],
            username=username,
            bio=data.get('bio'),
            avatar=data.get('avatar')
        )
        return jsonify({
            'message': 'User and profile created successfully',
            'user_id': new_user.id,
            'profile_id': new_profile.id
        }), 201
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500