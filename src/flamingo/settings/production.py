from .base import *

import firebase_admin

from flamingo.secrets import DJANGO_SECRET_KEY
from flamingo import secrets

# TODO: regenerate it!
SECRET_KEY = DJANGO_SECRET_KEY

cred = firebase_admin.credentials.Certificate(
    {
        "type": "service_account",
        "project_id": secrets.FIREBASE_PROJECT_ID,
        "private_key_id": secrets.FIREBASE_PRIVATE_KEY_ID,
        "private_key": secrets.FIREBASE_PRIVATE_KEY.replace("\\n", "\n"),
        "client_email": secrets.FIREBASE_CLIENT_EMAIL,
        "client_id": secrets.FIREBASE_CLIENT_ID,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://accounts.google.com/o/oauth2/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": secrets.FIREBASE_CLIENT_CERT_URL,
    }
)

default_app = firebase_admin.initialize_app(cred)
