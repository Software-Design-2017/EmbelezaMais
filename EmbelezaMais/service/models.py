# Django
from django.db import models

# Local Django
from . import (
    constants, validators
)

from user.models import (
    Company
)


class Service(models.Model):
    name = models.CharField(validators=[validators.validate_name], max_length=120)
    description = models.TextField(validators=[validators.validate_description], max_length=500)
    price = models.FloatField(validators=[validators.validate_price], blank=False, null=False)
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.name


class Combo(Service):
    specification = models.CharField(validators=[validators.validate_description], max_length=120)
    services = models.ManyToManyField(Service, through='ServicesCombo', related_name='services')


class ServicesCombo(models.Model):
    service_combo = models.ForeignKey(Combo, related_name='service_combo')
    service_in_combo = models.ForeignKey(Service, related_name='service_in_combo')

    class Meta():
        auto_created = True


class ServiceNail(Service):
    part = models.PositiveIntegerField(validators=[validators.validate_part], choices=constants.PART_CHOICES)


class ServiceMakeUp(Service):
    face_part = models.PositiveIntegerField(validators=[validators.validate_face_part],
                                            choices=constants.FACE_PART_CHOICES)


class ServiceHair(Service):
    specific_hair = models.PositiveIntegerField(validators=[validators.validate_specific_hair],
                                                choices=constants.SPECIFIC_HAIR_CHOICES)
    style = models.CharField(validators=[validators.validate_style], max_length=120)


class ServiceBeard(Service):
    style = models.CharField(validators=[validators.validate_style], max_length=120)
