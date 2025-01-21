from flask import Blueprint, request, jsonify
from repositories.user_repository import UserRepository
from repositories.profile_repository import ProfileRepository
from services.auth_service import AuthService

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = UserRepository.get_user_by_email(data['email'])
    if user and user.check_password(data['password']):
        profile = ProfileRepository.get_profile_by_user_id(user.id)
        access_token = AuthService.generate_token(user.id)
        return jsonify({
            'message': 'Login successful',
            'access_token': access_token,
            'user': {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'profile': {
                    'id': profile.id,
                    'user_id': profile.user_id,
                    'username': profile.username,
                    'bio': profile.bio,
                    'avatar': profile.avatar
                }
            }
        }), 200
    return jsonify({'message': 'Invalid credentials'}), 401