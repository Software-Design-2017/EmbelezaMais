from django.db import models
from . import (
    validators
)

# Create your models here.
from user.models import (
    Company
)


class Promotion(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=500)
    price = models.FloatField(
        validators=[validators.validate_price], blank=False, null=False)
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.name
