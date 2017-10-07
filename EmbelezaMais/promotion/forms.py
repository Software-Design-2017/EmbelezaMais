from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import (
    Promotion
)


class PromotionRegisterForm(forms.ModelForm):
    # Form Fields.
    name = forms.CharField(label='NAME',
                           max_length=60)

    description = forms.CharField(max_length=500, label='Descrição:')
    price = forms.FloatField(min_value=0, label='Preço')

    class Meta:
        model = Promotion
        fields = [
            'name',
            'description',
            'price'
        ]

    # Front-end validation function for company register page.
    def clean(self, *args, **kwargs):

        return super(PromotionRegisterForm, self).clean(*args, **kwargs)


class PromotionEditForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label=_('Name'), max_length=60, required=False)

    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  label=_('Description'), max_length=500, required=False)

    price = forms.FloatField(label=_('Price'), required=False)

    class Meta:
        model = Promotion
        fields = [
            'name',
            'description',
            'price'
        ]

    # Front-end validation function for promotion edit page.
    def clean(self, *args, **kwargs):

        return super(PromotionEditForm, self).clean(*args, **kwargs)
