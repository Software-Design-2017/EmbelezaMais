from django.db import models
from . import constants

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
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    # TODO change "/" to constant
    def __str__(self):
        return str(self.opening_time) + " / " + str(self.closing_time)

    def __init__(self, opening_time, closing_time):
        self.opening_time=opening_time
        self.closing_time=closing_time

class EmployeeManager(BaseUserManager):
    def create_user(self, name, specialty,
                    opening_time, closing_time, **kwargs):

        if not name:
            raise ValueError('The given name must be set')

        name = self.normalize_name(name)
        operatingHours = OperatingHours(opening_time, closing_time)
        employee = self.model(name, specialty, operatingHours, **kwargs)
        employee.save(using=self.db)

        return employee


class Employee(models.Model):
    name = Name()
    specialty = Specialty()
    operatingHours = OperatingHours()

    objects = EmployeeManager()

    def get_short_name(self):
        return self.name
