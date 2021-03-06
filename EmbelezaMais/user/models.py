import datetime
from geoposition.fields import GeopositionField

# Django.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models import EmailField
from django.core import validators
from . import constants


class UserManager(BaseUserManager):
    def create_user(self, email, password, name, **kwargs):

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email,
                          name=name,
                          is_active=False,
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
    validator = validators.EmailValidator(message=constants.EMAIL_FORMAT)

    default_validators = [validator]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = constants.EMAIL_FIELD_LENGTH
        kwargs['default'] = ''
        kwargs['unique'] = True
        super(EmailField, self).__init__(*args, **kwargs)


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


class TargetGenre(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = u'Perfil de Usuario'


class Client(User):
    phone_number = models.CharField(max_length=100)

    objects = UserManager()

    def __str__(self):
        return self.phone_number


class Company(User):
    description = models.CharField(max_length=100)

    target_genre = models.CharField(choices=constants.GENRE_CHOICES, max_length=100)

    position = GeopositionField(verbose_name=u'Geolocalização',
                                help_text="Não altere os valores calculados automaticamente de latitude e longitude")

    has_parking_availability = models.BooleanField(default=False)

    objects = UserManager()

    class Meta:
        verbose_name = ('company')
        verbose_name_plural = ('companies')


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
