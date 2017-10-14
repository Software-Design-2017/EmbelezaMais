# Django.
import logging
from django import forms
from user import constants

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('EmbelezaMais')


class SearchForm(forms.Form):
    # Form Fields.
    latitude = forms.CharField(label='Latitude')

    longitude = forms.CharField(label='Longitude')

    target_genre = forms.CharField(widget=forms.Select(choices=constants.GENRE_CHOICES))

    have_parking_availability = forms.BooleanField(initial=False, required=False)
