# Django.
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

# Local Django.
from .models import Employee
from . import constants


class EmployeeRegisterForm(forms.ModelForm):
    # Form Fields.
    name = forms.CharField(label='NAME',
                           max_length=60)

    specialty = forms.CharField(label='NAME',
                           max_length=30)

    opening_time = forms.TimeField()
    closing_time = forms.TimeField()

    class Meta:
        model = Employee
        fields = [
            'name',
            'specialty',
            'opening_time',
            'closing_time'
            ]

    # Front-end validation function for company register page.
    def clean(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        specialty = self.cleaned_data.get('specialty')
        opening_time = self.cleaned_data.get('opening_time')
        closing_time = self.cleaned_data.get('closing_time')

        return super(EmployeeRegisterForm, self).clean(*args, **kwargs)
