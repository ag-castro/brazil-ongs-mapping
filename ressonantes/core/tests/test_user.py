from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.validators import ValidationError

User = get_user_model()


class CustomUserModelTests(TestCase):

    email = 'newuser@webappsagency.com.br'
    password = 'pwdtest2020testing'
    extra_fields = {
        'first_name': 'Morpheus',
        'last_name': 'Dream Guardian',
        'mobile': '62985291951'
    }

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""

        user = User.objects.create_user(
            self.email, self.password,
            **self.extra_fields
        )
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""

        user = User.objects.create_user(
            self.email, self.password,
            **self.extra_fields
        )
        self.assertEqual(user.email, self.email.lower())

    def test_new_user_with_no_email(self):
        """Test creating user with no email raises error"""

        with self.assertRaises(ValueError):
            User.objects.create_user(None, self.password)

    def test_new_user_invalid_email(self):
        """Test creating user with invalid email raises error"""

        email = 'invalid_email'
        with self.assertRaises(ValidationError):
            User.objects.create_user(email, self.password)

    def test_new_user_with_no_first_name(self):
        """Test creating user with no given first name required field."""

        with self.assertRaises(ValueError):
            User.objects.create_user(
                self.email, self.password, first_name=None,
                last_name=self.extra_fields['last_name'],
                mobile=self.extra_fields['mobile']
            )

    def test_new_user_with_no_last_name(self):
        """Test creating user with no given last name required field."""

        with self.assertRaises(ValueError):
            User.objects.create_user(
                self.email, self.password, last_name=None,
                first_name=self.extra_fields['first_name'],
                mobile=self.extra_fields['mobile']
            )

    def test_new_user_with_no_mobile(self):
        """Test creating user with no given mobile number required field."""

        with self.assertRaises(ValueError):
            User.objects.create_user(
                self.email, self.password, mobile=None,
                first_name=self.extra_fields['first_name'],
                last_name=self.extra_fields['last_name']
            )

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            self.email, self.password,
            **self.extra_fields
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
