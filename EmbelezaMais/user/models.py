# standard library
import logging

# Django.
from django.db import models
# from django.contrib.auth.models import (
#     AbstractBaseUser, PermissionsMixin,
# )
# from django.db.models import EmailField
# from django.core import validators

# Local Django.
from . import constants

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(constants.PROJECT_NAME)

#
# class Email(EmailField):
#     validator = validators.EmailValidator(message=constants.EMAIL_FORMAT)
#
#     default_validators = [validator]
#
#     def __init__(self, *args, **kwargs):
#         kwargs['max_length'] = constants.EMAIL_FIELD_LENGTH
#         kwargs['default'] = ''
#         kwargs['unique'] = True
#         super(EmailField, self).__init__(*args, **kwargs)
#
#
# class Name(models.CharField):
#     validator_max_length = validators.MaxLengthValidator(constants.
#                                                          USERNAME_MAX_LENGHT,
#                                                          message=constants.
#                                                          NAME_SIZE)
#     validator_format = validators.RegexValidator(regex=r'^[A-Za-z ]+$',
#                                                  message=constants.
#                                                  NAME_CHARACTERS)
#     default_validators = [validator_max_length, validator_format]
#
#     def __init__(self, *args, **kwargs):
#         kwargs['max_length'] = constants.NAME_FIELD_LENGTH
#         kwargs['default'] = ''
#         kwargs['unique'] = True
#         super(models.CharField, self).__init__(*args, **kwargs)
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     USERNAME_FIELD = 'email'
#     email = Email()
#     name = Name()


class TargetGenre(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Company(models.Model):
    description = models.CharField(max_length=100)
    target_genre = models.ManyToManyField(TargetGenre)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class PhoneCompany(models.Model):
    number_phone = models.CharField(max_length=100)
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.number_phone


class PicturesCompany(models.Model):
    picture = models.ImageField(default=None, editable=True)
    company = models.ForeignKey(Company)


class OperatingHours(models.Model):
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    day_of_week = models.CharField(max_length=100)
    company = models.ForeignKey(Company)

    # TODO change "/" to constant
    def __str__(self):
        return str(self.opening_time) + " / " + str(self.closing_time)
