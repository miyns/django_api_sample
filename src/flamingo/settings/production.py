import firebase_admin

import configparser
config = configparser.ConfigParser()
config.read("secrets.ini")
config_section = "production"

# TODO: regenerate it!
SECRET_KEY = config.get(config_section, 'DJANGO_SECRET_KEY')

cred = firebase_admin.credentials.Certificate(
    {
        "type": "service_account",
        "project_id": config.get(config_section, 'FIREBASE_PROJECT_ID'),
        "private_key_id": config.get(config_section, 'FIREBASE_PRIVATE_KEY_ID'),
        "private_key": config.get(config_section, 'FIREBASE_PRIVATE_KEY').replace("\\n", "\n"),
        "client_email": config.get(config_section, 'FIREBASE_CLIENT_EMAIL'),
        "client_id": config.get(config_section, 'FIREBASE_CLIENT_ID'),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://accounts.google.com/o/oauth2/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": config.get(config_section, 'FIREBASE_CLIENT_CERT_URL'),
    }
)

default_app = firebase_admin.initialize_app(cred)
