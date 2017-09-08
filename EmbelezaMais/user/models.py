# standard library
import logging

# Django.
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin,
)
from django.db.models import EmailField
from django.core import validators

# Local Django.
from . import constants

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(constants.PROJECT_NAME)


class Email(EmailField):
    validator = validators.EmailValidator(message=constants.EMAIL_FORMAT)

    default_validators = [validator]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = constants.EMAIL_FIELD_LENGTH
        kwargs['default'] = ''
        kwargs['unique'] = True
        super(EmailField, self).__init__(*args, **kwargs)


class Name(models.CharField):
    validator_max_length = validators.MaxLengthValidator(constants.
                                                         USERNAME_MAX_LENGHT,
                                                         message=constants.
                                                         NAME_SIZE)
    validator_format = validators.RegexValidator(regex=r'^[A-Za-z ]+$',
                                                 message=constants.
                                                 NAME_CHARACTERS)
    default_validators = [validator_max_length, validator_format]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = constants.NAME_FIELD_LENGTH
        kwargs['default'] = ''
        super(models.CharField, self).__init__(*args, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    email = Email()
    name = Name()
