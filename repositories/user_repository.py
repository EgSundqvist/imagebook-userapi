from models.user import User
from db import db
import logging

logger = logging.getLogger(__name__)

class UserRepository:
    @staticmethod
    def create_user(first_name, last_name, email, password):
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        logger.info(f'[DB] User created: user_id={new_user.id}')
        return new_user

    @staticmethod
    def get_user_by_email(email):
        user = User.query.filter_by(email=email).first()
        logger.info(f'[DB] Fetched user by email={email}')
        return user

    @staticmethod
    def get_user_by_id(user_id):
        user = User.query.get(user_id)
        logger.info(f'[DB] Fetched user by user_id={user_id}')
        return user

    @staticmethod
    def get_all_users():
        users = User.query.all()
        logger.info(f'[DB] Fetched all users')
        return users

    @staticmethod
    def update_password(user_id, old_password, new_password):
        user = User.query.get(user_id)
        if user and user.check_password(old_password):
            user.set_password(new_password)
            db.session.commit()
            logger.info(f'[DB] Password updated for user_id={user_id}')
            return True
        logger.warning(f'[DB] Failed to update password for user_id={user_id}')
        return False