import secrets

# Generera en stark hemlig nyckel
secret_key = secrets.token_hex(32)
print(secret_key)