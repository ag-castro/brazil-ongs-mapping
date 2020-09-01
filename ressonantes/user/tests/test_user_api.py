from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')
ME_URL = reverse('user:me')
CHANGE_PASSWORD_URL = reverse('user:change_password')
TOKEN_URL = reverse('token_obtain')

payload = {
    'email': 'newpub@webappsagency.com.br',
    'password': 'pwdtest2020testing',
    'first_name': 'Morpheus',
    'last_name': 'Dream Guardian',
    'mobile': '62985291951'
}


def create_user(**payload):
    """Creates a default user to run tests"""
    return get_user_model().objects.create_user(**payload)


class PublicUserApiTest(TestCase):
    """Test the users API - public"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating user with valid payload is successful"""

        response = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**response.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', response.data)

    def test_user_exists(self):
        """Test creating a user that already exists fails"""

        create_user(**payload)
        response = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that the given password must be more than 9 characters"""

        payload['password'] = 'pwd'
        response = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email'])
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """Test creating token fot the user authentication"""

        create_user(**payload)
        payload_ = {
            'email': payload['email'],
            'password': payload['password']
        }
        response = self.client.post(TOKEN_URL, payload_)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """Test creating user token with invalid given credentials"""

        create_user(**payload)
        payload_ = {
            'email': payload['email'],
            'password': 'nopwd'
        }
        response = self.client.post(TOKEN_URL, payload_)
        self.assertNotIn('refresh', response.data)
        self.assertNotIn('access', response.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_token_no_user(self):
        """Test creating token with no given user credentials"""

        payload_ = {
            'email': payload['email'],
            'password': payload['password']
        }
        response = self.client.post(TOKEN_URL, payload_)
        self.assertNotIn('refresh', response.data)
        self.assertNotIn('access', response.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_token_missing_field(self):
        """Test creating token with no given required fields"""

        response = self.client.post(
            TOKEN_URL, {'email': 'noone', 'password': ''})
        self.assertNotIn('refresh', response.data)
        self.assertNotIn('access', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_user_unauthorized(self):
        """Test required authentication user"""

        response = self.client.post(ME_URL)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUserApiTest(TestCase):
    """Test the users API - private"""

    def setUp(self):
        self.user = create_user(**payload)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_profile_success(self):
        """Test retrieving profile of authenticated user"""

        response = self.client.get(ME_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'email': self.user.email,
            'mobile': self.user.mobile,
            'is_whatsapp_mobile': self.user.is_whatsapp_mobile,
            'is_ong': self.user.is_ong,
            'created_at': response.data['created_at']
        })

    def test_post_me_not_allowed(self):
        """Test POST method is not allowed on the ME url"""

        response = self.client.post(ME_URL, {})
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_user_profile(self):
        """Test updating user profile for authenticated user"""

        payload_ = {
            'first_name': 'Bob Marley',
            'mobile': '62985299889'
        }
        response = self.client.patch(ME_URL, payload_)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, payload_['first_name'])
        self.assertEqual(self.user.mobile, payload_['mobile'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_change_user_password_successful(self):
        """Test changing authenticated user password"""

        payload_ = {
            'old_password': payload['password'],
            'new_password1': 'newpwdchanged123',
            'new_password2': 'newpwdchanged123',
        }

        response = self.client.patch(CHANGE_PASSWORD_URL, payload_)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password(payload_['new_password1']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_change_user_password_fails(self):
        """Test changing  that user password with wrong data fields fails."""

        payload_ = {
            'old_password': 'wrongpassword',
            'new_password1': 'newpwdchanged123',
            'new_password2': 'newpwdchanged123',
        }

        response = self.client.patch(CHANGE_PASSWORD_URL, payload_)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_change_user_password_no_match_fails_(self):
        """Test changing  that user password with wrong data fields fails."""

        payload_ = {
            'old_password': payload['password'],
            'new_password1': 'newpassword123132',
            'new_password2': '123132newpassword',
        }

        response = self.client.patch(CHANGE_PASSWORD_URL, payload_)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
