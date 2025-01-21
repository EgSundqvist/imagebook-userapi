from models.user import User
from models.profile import Profile
from db import db
from services.go_service import create_s3_folder_for_user
import requests
import logging

logger = logging.getLogger(__name__)

class RegisterRepository:
    @staticmethod
    def register_user_and_profile(first_name, last_name, email, password, username, bio, avatar):
        try:
            # Starta en databastransaktion
            new_user = User(
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.flush()  # Flush för att få new_user.id innan commit

            new_profile = Profile(
                user_id=new_user.id,
                username=username,
                bio=bio,
                avatar=avatar
            )
            db.session.add(new_profile)

            # Skapa S3-mapp för användaren
            try:
                logger.info(f'[DB] Creating S3 folder for user_id: {new_user.id}')
                create_s3_folder_for_user(new_user.id)
            except requests.RequestException as e:
                db.session.rollback()
                logger.error(f'[DB] Failed to create S3 folder: {str(e)}')
                raise Exception(f'Failed to create S3 folder: {str(e)}')

            # Commit transaktionen
            db.session.commit()
            logger.info(f'[DB] User and profile registered: user_id={new_user.id}, profile_id={new_profile.id}')

            return new_user, new_profile
        except Exception as e:
            db.session.rollback()
            logger.error(f'[DB] Error during user registration: {str(e)}')
            raise e