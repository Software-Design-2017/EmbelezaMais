# Django.
from django import forms

# Local Django.
from .models import Client

class ClientRegisterForm(forms.ModelForm):
    # Form Fields.
    username = forms.CharField(label='USERNAME',
                               max_length=12)

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
            'username',
            'email',
            'phone_number'
        ]

    # Front-end validation function for register page.
    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        phone_number = self.cleaned_data.get('phone_number')

        email_from_database = User.objects.filter(email=email)
        username_from_database = User.objects.filter(username=username)

        if username_from_database.exists():
            raise forms.ValidationError(_('Nickname already registered'))
        elif email_from_database.exists():
            raise ValidationError(_('Email already registered'))
        elif len(password) < 8:
            raise forms.ValidationError(_('Password must be between 8 and 12 characters'))
        elif len(password) > 12:
            raise forms.ValidationError(_('Password must be between 8 and 12 characters'))
        elif password != password_confirmation:
            raise forms.ValidationError(_('Passwords do not match.'))

        return super(ClientRegisterForm, self).clean(*args, **kwargs)