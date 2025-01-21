import requests
from flask import current_app
import logging
from services.auth_service import AuthService  # Lägg till denna import

def create_s3_folder_for_user(user_id):
    imageapi_url = current_app.config['IMAGEAPI_URL']
    token = AuthService.generate_token_for_image_api(user_id)  # Generera token med den nya metoden
    logging.info(f'Generated JWT token: {token}')  # Logga tokenen
    headers = {'Authorization': f'Bearer {token}'}  # Inkludera tokenen i Authorization-headern
    payload = {'user_id': str(user_id)}  # Konvertera user_id till sträng
    logging.info(f'Sending request to {imageapi_url}/create-s3-folder with payload: {payload}')
    response = requests.post(f'{imageapi_url}/create-s3-folder', json=payload, headers=headers)  # Lägg till headers
    logging.info(f'Response status code: {response.status_code}')
    logging.info(f'Response content: {response.content}')
    response.raise_for_status()  # Kasta ett undantag om förfrågan misslyckas
    return response.json()