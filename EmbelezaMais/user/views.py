import hashlib
import datetime
import random

from django.shortcuts import render, render_to_response, get_object_or_404
from .models import Company, UserProfile
from .forms import CompanyRegisterForm
from django.core.mail import send_mail
from django.http import HttpResponse
from django.utils import timezone
from . import constants


def register_view(request):
    form = CompanyRegisterForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        name = form.cleaned_data.get('name')
        description = form.cleaned_data.get('description')
        target_genre = form.cleaned_data.get('target_genre')
        location = form.cleaned_data.get('location')
        Company.objects.create_user(email=email, password=password, name=name, target_genre=target_genre,
                                    description=description, location=location)

        user = Company.objects.get(email=email)

        return send_email_confirmation(user)

    else:
        pass

    return render(request, "company_register_form.html", {"form": form})


def send_email_confirmation(user):
    # Prepare the information needed to send the account verification
    # email.
    salt = hashlib.sha1(str(random.random()).
                        encode('utf-8')).hexdigest()[:5]

    email = user.email

    activation_key = hashlib.sha1(str(salt+email).
                                  encode('utf‌​-8')).hexdigest()
    key_expires = datetime.datetime.today() + datetime.timedelta(2)

    new_profile = UserProfile(user=user, activation_key=activation_key,
                              key_expires=key_expires)
    new_profile.save()

    # Send account confirmation email.
    email_subject = (constants.EMAIL_CONFIRMATION_SUBJECT)
    email_body = constants.EMAIL_CONFIRMATION_BODY % (activation_key)

    send_mail(email_subject, email_body, constants.EMBELEZAMAIS_EMAIL, [email],
              fail_silently=False)

    return render_to_response('company_register_success.html')


def register_confirm(request, activation_key):
    # Verify if user is already confirmed.
    if request.user.id is not None:

        HttpResponse('Conta ja confirmada')
    else:
        # Nothing to do
        pass

    # Check if activation token is valid, if not valid return an 404 error.
    user_profile = get_object_or_404(UserProfile,
                                     activation_key=activation_key)

    # Verifies if the activation token has expired and if so renders the html
    # of expired registration.
    if user_profile.key_expires < timezone.now():
        user_profile.delete()

        return HttpResponse("Tempo para confirmar conta expirou. Crie sua conta novamente")
    else:
        # Nothing to do.
        pass

    # If the token has not expired, the user is activated and the
    # confirmation html is displayed.
    user = user_profile.user
    user.is_active = True
    user.save()

    return render_to_response('company_confirmed_account.html')
