# standard library
import logging

# Django

from django.shortcuts import (
    render
)


# local Django
from .forms import (
    ClientRegisterForm
)
from .models import (
    Client
)

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
        Client.objects.create_client(email=email, password=password,
                                     name=name, phone_number=phone_number)

    else:
        logger.debug("Register form was invalid.")

    return render(request, "client_register_form.html", {"form": form})
