from django import forms

from .models import (
    Promotion
)


class PromotionRegisterForm(forms.ModelForm):
    # Form Fields.
    name = forms.CharField(label='NAME',
                           max_length=60)

    description = forms.CharField(max_length=500, label='Descrição:')
    price = forms.FloatField(min_value=0,label='Preço')

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
