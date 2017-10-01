from django.conf.urls import url
from .views import (
    PromotionRegister,
    PromotionList
)

urlpatterns = (
    url(r'^create/', PromotionRegister.as_view(), name='promotion_create'),
    url(r'^list/$', PromotionList.as_view(), name='promotion_list'),
)
