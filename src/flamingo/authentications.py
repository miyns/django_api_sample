import logging

from django.utils import timezone
from firebase_admin import auth

from rest_framework.authentication import BaseAuthentication

from flamingo.models import User
from flamingo.exceptions import FirebaseError
from flamingo.exceptions import InvalidAuthToken
from flamingo.exceptions import NoAuthToken

import logging

logger = logging.getLogger(__name__)


class FirebaseAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            # raise NoAuthToken("No auth token provided")
            logger.debug("No auth token provided")
            return None

        id_token = auth_header.split(" ").pop()
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise InvalidAuthToken("Invalid auth token")

        if not id_token or not decoded_token:
            return None

        try:
            uid = decoded_token.get("uid")
        except Exception:
            raise FirebaseError()

        user, created = User.objects.get_or_create(username=uid)
        user.profile.last_activity = timezone.localtime()

        return user, None
