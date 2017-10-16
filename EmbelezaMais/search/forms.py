# Django.
import logging
from django import forms
from search import constants

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('EmbelezaMais')


class SearchForm(forms.Form):
    # Form Fields.
    latitude = forms.CharField(label='Latitude', initial=constants.STANDARD_LATITUDE_STRING, required=False)

    longitude = forms.CharField(label='Longitude', initial=constants.STANDARD_LONGITUDE_STRING, required=False)

    target_genre = forms.CharField(initial='All', widget=forms.Select(choices=constants.GENRE_CHOICES), required=False)

    has_parking_availability = forms.BooleanField(initial=False, required=False)
