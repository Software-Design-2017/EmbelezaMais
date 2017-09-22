# standard library
import logging
import hashlib
import datetime
import random
import abc

# Django

from django.shortcuts import (
    render, redirect, get_object_or_404
)
from django.core.mail import send_mail
from django.utils import timezone
from django.http import HttpResponse
from django.contrib import auth
from django.utils.decorators import method_decorator
from django.views.generic import (
    FormView, View
)

# local Django
from .forms import (
    ClientRegisterForm, CompanyRegisterForm, CompanyLoginForm
)
from .models import (
    Client, Company, UserProfile
)

from . import constants

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('EmbelezaMais')


def register_client_view(request):
    form = ClientRegisterForm(request.POST or None)

    if form.is_valid():
        logger.debug("Register form was valid.")
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        name = form.cleaned_data.get('name')
        phone_number = form.cleaned_data.get('phone_number')
        Client.objects.create_user(email=email, password=password,
                                   name=name, phone_number=phone_number)

        user = Client.objects.get(email=email)
        return send_email_confirmation(user)
    else:
        logger.debug("Register form was invalid.")

    return render(request, "client_register_form.html", {"form": form})


def register_company_view(request):
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

    logger.info("Email sended to user.")
    return redirect('/')


def register_confirm(request, activation_key):
    # Verify if user is already confirmed.
    if request.user.id is not None:

        logger.info("Logged user: " + request.user.name)

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

    return redirect('/')


class LoginView(FormView):
    form_class = None
    template_name = None

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = auth.authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                )
            if user is not None:
                return self._verify_user_is_especific_type(request, user, form)
            else:
                return redirect('/')
        else:
            return render(request, self.template_name, {'form': form})

    @abc.abstractmethod
    def _verify_user_is_especific_type(self, request, user):
        return


class LoginCompanyView(LoginView):
    form_class = CompanyLoginForm
    template_name = 'login_company.html'
    message = None

    def _verify_user_is_especific_type(self, request, user, form):
        success_url = '/dashboard'
        is_company = hasattr(user, 'company')

        if is_company:
            if user.is_active:
                auth.login(request, user)
                return redirect(str(success_url))
            else:
                return HttpResponse('User is not active')
        else:
            message = 'You are not registered with the company.'
            return render(request, self.template_name, {'form': form, 'message': message})


class LoginClientView(LoginView):
    form_class = CompanyLoginForm
    template_name = 'login_client.html'
    message = None

    def _verify_user_is_especific_type(self, request, user, form):
        success_url = '/search'
        is_client = hasattr(user, 'client')

        if is_client:
            if user.is_active:
                auth.login(request, user)
                return redirect(str(success_url))
            else:
                return HttpResponse('User is not active')
        else:
            message = 'You are not registered as a client.'
            return render(request, self.template_name, {'form': form, 'message': message})


class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return redirect('/')