# Django.
import logging
from django import forms

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('EmbelezaMais')


class SearchForm(forms.ModelForm):
    # Form Fields.
    latitude = forms.CharField(label='Latitude')

    longitude = forms.CharField(label='Longitude')
