from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient


class TokenAuthAPITestCase(APITestCase):
    """Helper to test views that need Token Authorization"""

    def token_auth(self):
        """Call this function when a Token Authorization is required"""
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='test@test.com', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

