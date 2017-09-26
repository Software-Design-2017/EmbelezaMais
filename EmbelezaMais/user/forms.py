
import logging
# Django.
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

# Local Django.
from .models import Client, Company
from . import constants

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('EmbelezaMais')


class ClientRegisterForm(forms.ModelForm):
    # Form Fields.
    name = forms.CharField(label='NAME',
                           max_length=60)

    email = forms.EmailField(label='EMAIL')

    password = forms.CharField(widget=forms.PasswordInput,
                               label='PASSWORD')

    password_confirmation = forms.CharField(widget=forms.PasswordInput,
                                            label='PASSWORD_CONFIRMATION')

    phone_number = forms.CharField(label='PHONE',
                                   max_length=14)

    class Meta:
        model = Client
        fields = [
            'name',
            'email',
            'phone_number'
            ]

    # Front-end validation function for company register page.
    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        phone_number = self.cleaned_data.get('phone_number')

        email_from_database = Client.objects.filter(email=email)

        if email_from_database.exists():
            raise forms.ValidationError(('Email already registered'))
        elif len(password) < 8:
            raise forms.ValidationError(('Password must be between 8 and 12 characters'))
        elif len(password) > 12:
            raise forms.ValidationError(('Password must be between 8 and 12 characters'))
        elif password != password_confirmation:
            raise forms.ValidationError(('Passwords do not match.'))
        elif len(phone_number) > 14:
            raise forms.ValidationError(('Invalid phone number.'))

        return super(ClientRegisterForm, self).clean(*args, **kwargs)


class CompanyRegisterForm(forms.ModelForm):
    # Form Fields.
    password = forms.CharField(widget=forms.PasswordInput,
                               label=_('Password'))

    password_confirmation = forms.CharField(widget=forms.PasswordInput,
                                            label=_('Password Confirmation'))

    class Meta:
        model = Company
        fields = [
            'name',
            'email',
            'description',
            'target_genre',
            'location',
        ]

    # Front-end validation function for company register page.
    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        email_from_database = Company.objects.filter(email=email)

        if email_from_database.exists():
            raise ValidationError(_("This Email has been already registered"))
        elif len(password) < 8:
            raise forms.ValidationError(('Password must be 8 or more characters'))
        elif password != password_confirmation:
            raise forms.ValidationError(_("Passwords don't match."))
        return super(CompanyRegisterForm, self).clean(*args, **kwargs)


class CompanyEditForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label=_('Name'), max_length=constants.NAME_FIELD_LENGTH, required=False)

    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  label=_('Description'), max_length=100, required=False)

    target_genre = forms.ChoiceField(choices=(constants.GENRE_CHOICES),
                                     widget=forms.Select(attrs={'class': 'form-control'}),
                                     label=_('Target Genre'), required=False)

    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label=_('Location'), max_length=100, required=False)

    class Meta:
        model = Company
        fields = [
            'name',
            'description',
            'target_genre',
            'location',
        ]

    def clean(self, *args, **kwargs):

        return super(CompanyEditForm, self).clean(*args, **kwargs)


class CompanyLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, label=_(constants.PASSWORD))

    def clean(self, *args, **kwargs):
        password = self.cleaned_data.get("password")

        if len(password) < constants.PASSWORD_MIN_LENGTH:
            raise forms.ValidationError({'password': [_(constants.PASSWORD_SIZE)]})
        elif len(password) > constants.PASSWORD_MAX_LENGTH:
            raise forms.ValidationError({'password': [_(constants.PASSWORD_SIZE)]})
        else:
            pass

        return super(CompanyLoginForm, self).clean(*args, **kwargs)

    class Meta:
        model = Company
