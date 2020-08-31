from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class UserRessonanteManager(BaseUserManager):
    """User Ressonante Objects Manager"""

    def is_valid_email(self, new_email):
        """Check if the new given email is valid."""
        try:
            validate_email(new_email)
            return True
        except ValidationError:
            return False

    def _create_user(self, email, password, **extra_fields):
        """Creates a new user with the given information"""

        if not email:
            raise ValueError(_("A email must be set."))

        if not self.is_valid_email(email):
            raise ValidationError(_('A valid email must be given.'))

        if not extra_fields.get('first_name'):
            raise ValueError(_('A first name must be given.'))

        if not extra_fields.get('last_name'):
            raise ValueError(_('A first name must be given.'))

        if not extra_fields.get('mobile'):
            raise ValueError(_('A mobile number must be given.'))

        if not password:
            raise ValueError(_("A password must be set."))

        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Creates a SuperUser on the application"""

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                _("Superuser must be a staff member. Set is_staff=True"))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        if extra_fields.get('is_active') is not True:
            raise ValueError(_('Superuser must have is_active=True.'))

        return self._create_user(email, password, **extra_fields)

    def create_user(self, email=None, password=None, **extra_fields):
        """Creates a Default User on the application"""

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
