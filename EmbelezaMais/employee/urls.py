from django.conf.urls import url
from .views import (
    register_employee,
    employee_list,
)

urlpatterns = (
    url(r'^register_employee/', register_employee, name='register_employee'),
    url(r'^employee_list/', employee_list, name='employee_list'),
)
