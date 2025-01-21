from models.profile import Profile
from db import db
import logging

logger = logging.getLogger(__name__)

class ProfileRepository:
    @staticmethod
    def create_profile(user_id, username, bio, avatar):
        new_profile = Profile(
            user_id=user_id,
            username=username,
            bio=bio,
            avatar=avatar
        )
        db.session.add(new_profile)
        db.session.commit()
        logger.info(f'[DB] Profile created: user_id={user_id}, profile_id={new_profile.id}')
        return new_profile

    @staticmethod
    def get_profile_by_username(username):
        profile = Profile.query.filter_by(username=username).first()
        logger.info(f'[DB] Fetched profile by username={username}')
        return profile

    @staticmethod
    def get_profile_by_user_id(user_id):
        profile = Profile.query.filter_by(user_id=user_id).first()
        logger.info(f'[DB] Fetched profile by user_id={user_id}')
        return profile

    @staticmethod
    def update_profile(profile_id, username, bio, avatar):
        profile = Profile.query.get_or_404(profile_id)
        profile.username = username
        profile.bio = bio
        profile.avatar = avatar
        db.session.commit()
        logger.info(f'[DB] Profile updated: profile_id={profile_id}')
        return profile

    @staticmethod
    def update_profile_by_user_id(user_id, username, bio, avatar):
        profile = Profile.query.filter_by(user_id=user_id).first_or_404()
        profile.username = username
        profile.bio = bio
        profile.avatar = avatar
        db.session.commit()
        logger.info(f'[DB] Profile updated by user_id={user_id}')
        return profile