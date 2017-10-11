# Django
from django.contrib import admin

# Local Django
from .models import (
    Service, Combo, ServicesCombo, ServiceNail, ServiceMakeUp, ServiceBeard, ServiceHair
)

admin.site.register(Service)
admin.site.register(Combo)
admin.site.register(ServicesCombo)
admin.site.register(ServiceNail)
admin.site.register(ServiceMakeUp)
admin.site.register(ServiceBeard)
admin.site.register(ServiceHair)
