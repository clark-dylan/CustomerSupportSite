from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, full_name, username, email, password):
        if not full_name:
            raise ValueError("Please enter your full name.")

        if not username:
            raise ValueError("Please enter a username.")

        if not email:
            raise ValueError("Please enter an email.")

        user = self.model(
            email = self.normalize_email(email)
        )

        user.set_password(password)

        user.save(using=self.db)
        return user

    def create_staffuser(self, full_name, username, email, password):
        user = self.model(
            full_name   = full_name,
            username    = username,
            email       = self.normalize_email(email),
            password    = password
        )

        user.set_password(password)
        user.staff = True
        user.save(using=self.db)
        return user

    def create_superuser(self, full_name, username, email, password):
        user = self.model(
            full_name   = full_name,
            username    = username,
            email       = self.normalize_email(email),
        )

        user.set_password(password)
        user.staff = True
        user.admin = True

        user.save(using=self.db)
        return user


class usernameValidator(UnicodeUsernameValidator):
    regex = r'^[a-zA-Z0-9_]+$'

class User(AbstractBaseUser):
    username_validator = usernameValidator()

    default_errors = {
        'blank': 'You must enter a username.',
        'invalid': 'Username is invalid. Usernames should only contain letters, numbers or underscores.',
        'max_length': 'Usernames must be less than 15 characters long.',
        'duplicate_username': 'That username already exists.'
    }

    full_name       = models.CharField(max_length=40)
    username        = models.CharField(max_length=15, unique=True, validators=[username_validator], error_messages=default_errors)
    email           = models.EmailField(max_length=100, unique=True)
    date_joined     = models.DateTimeField(auto_now_add=True, null=True)
    active          = models.BooleanField(default=True)
    staff           = models.BooleanField(default=False)
    admin           = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['full_name', 'email']

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.username

    def get_username(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_active(self):
        # Is the user active?
        return self.active

    @property
    def is_staff(self):
        # Is the user a staff member?
        return self.staff

    @property
    def is_admin(self):
        # Is the user an admin?
        return self.admin


