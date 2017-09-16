# Django.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models import EmailField
from django.contrib.auth.models import PermissionsMixin
from django.core import validators
# from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_client(self, email, password, name, phone_number, **kwargs):

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email,
                          name=name,
                          is_active=True,
                          phone_number=phone_number,
                          **kwargs)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password, name, **kwargs):

        email = self.normalize_email(email)
        user = self.model(email=email,
                          name=name,
                          is_staff=True,
                          is_active=True,
                          is_superuser=True,
                          **kwargs)

        user.set_password(password)
        user.save(using=self.db)

        return user


class Email(EmailField):
    validator = validators.EmailValidator(message='Enter a valid email address')

    default_validators = [validator]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 30
        kwargs['default'] = ''
        kwargs['unique'] = True
        super(EmailField, self).__init__(*args, **kwargs)


class Name(models.CharField):
    validator_max_length = validators.MaxLengthValidator(60,
                                                         message='Your name exceeds 30 characteres')
    validator_format = validators.RegexValidator(regex=r'^[A-Za-z ]+$',
                                                 message='Your name can\'t have special characters')
    default_validators = [validator_max_length, validator_format]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 60
        kwargs['default'] = ''
        super(models.CharField, self).__init__(*args, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    email = Email()
    name = Name()
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


class Client(User):
    phone_number = models.CharField(max_length=100)

    objects = UserManager()

    def __str__(self):
        return self.phone_number
