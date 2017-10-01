# standard library
import logging

from django.db import models
from . import constants

from django.contrib.auth.models import BaseUserManager
from django.core import validators
from django.db.models import TimeField

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('EmbelezaMais')


class Name(models.CharField):
    validator_max_length = validators.MaxLengthValidator(constants.NAME_FIELD_LENGTH,
                                                         message=constants.NAME_SIZE)
    validator_format = validators.RegexValidator(regex=r'^[a-zA-Zá-úÀ-Úã-õ-Ã-Õ ]+$',
                                                 message=constants.NAME_CHARACTERS)

    default_validators = [validator_max_length, validator_format]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 60
        kwargs['default'] = ''
        super(models.CharField, self).__init__(*args, **kwargs)


class Specialty(models.CharField):
    validator_max_length = validators.MaxLengthValidator(constants.SPECIALTY_FIELD_LENGTH,
                                                         message=constants.SPECIALTY_SIZE)
    validator_format = validators.RegexValidator(regex=r'^[a-zA-Zá-úÀ-Úã-õ-Ã-Õ ]+$',
                                                 message=constants.SPECIALTY_CHARACTERS)

    default_validators = [validator_max_length, validator_format]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 60
        kwargs['default'] = ''
        super(models.CharField, self).__init__(*args, **kwargs)


class OperatingHours(models.Model):
    opening_time = models.CharField(max_length=100)
    closing_time = models.CharField(max_length=100)

    # TODO change "/" to constant
    def __str__(self):
        return str(self.opening_time) + " / " + str(self.closing_time)

    def __init__(self, opening_time, closing_time):
        self.opening_time=opening_time
        self.closing_time=closing_time


class EmployeeManager(BaseUserManager):
    def create_employee(self, name, specialty, opening_time, closing_time, **kwargs):

        if not name:
            raise ValueError('The given name must be set')

        name = self.name
        operating_hours = OperatingHours(opening_time, closing_time)
        employee = Employee(name=name, specialty=specialty, opening_time=opening_time, closing_time=closing_time)
        employee.save()

        return employee


class Employee(models.Model):
    name = Name()
    specialty = Specialty()

    opening_time = models.CharField(max_length=5)
    closing_time = models.CharField(max_length=5)

    operating_hours = OperatingHours(opening_time, closing_time)

    objects = EmployeeManager()

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.name
