from django.conf.urls import url
from .views import (
    register_employee,
)

urlpatterns = (
    url(r'^register_employee/', register_employee, name='register_employee'),

)
