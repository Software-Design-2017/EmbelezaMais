# standard library
import logging

# Django

from django.shortcuts import (
    render, redirect
)

from django.views.generic import (
    FormView, View
)

# local Django
from .forms import (
    EmployeeRegisterForm
)
from .models import (
    Employee
)

from . import constants

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('EmbelezaMais')

def register_employee(request):
    form = EmployeeRegisterForm(request.POST or None)

    if form.is_valid():
        logger.debug("Employee form was valid.")
        name = form.cleaned_data.get('name')
        specialty = form.cleaned_data.get('specialty')
        opening_time = form.cleaned_data.get('opening_time')
        closing_time = form.cleaned_data.get('closing_time')

        Employee.objects.create_employee(name=name, specialty=specialty,
                                        opening_time=opening_time, closing_time=closing_time)

    else:
        logger.debug("Register form was invalid.")

    return render(request, "employee_register_form.html", {"form": form})
