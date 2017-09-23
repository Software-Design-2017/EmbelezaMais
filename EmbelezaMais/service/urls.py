from django.conf.urls import url
from .views import (
    ServiceComboCreate,
    ServiceList,
    ServiceNailCreate,
    ServiceBeardCreate,
    ServiceMakeUpCreate,
    ServiceHairCreate,
)

urlpatterns = (
        url(r'^create/nail/$', ServiceNailCreate.as_view(), name='nail_service_create'),
        url(r'^create/combo/$', ServiceComboCreate.as_view(), name='combo_service_create'),
        url(r'^create/beard/$', ServiceBeardCreate.as_view(), name='beard_service_create'),
        url(r'^create/makeup/$', ServiceMakeUpCreate.as_view(), name='makeup_service_create'),
        url(r'^create/hair/$', ServiceHairCreate.as_view(), name='hair_service_create'),
        url(r'^list/$', ServiceList.as_view(), name='service_list'),
)
