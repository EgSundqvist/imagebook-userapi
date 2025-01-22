import requests
from flask import current_app
import logging
from services.auth_service import AuthService

def create_s3_folder_for_user(user_id):
    imageapi_url = current_app.config['IMAGEAPI_URL']
    token = AuthService.generate_token_for_image_api(user_id)
    logging.info(f'Generated JWT token: {token}')
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'user_id': str(user_id)} 
    logging.info(f'Sending request to {imageapi_url}/create-s3-folder with payload: {payload}')
    response = requests.post(f'{imageapi_url}/create-s3-folder', json=payload, headers=headers)
    logging.info(f'Response status code: {response.status_code}')
    logging.info(f'Response content: {response.content}')
    response.raise_for_status() 
    return response.json()