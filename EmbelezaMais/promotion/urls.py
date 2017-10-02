from django.conf.urls import url
from .views import (
    PromotionRegister,
    PromotionList,
    PromotionEdit
)

urlpatterns = (
    url(r'^create/', PromotionRegister.as_view(), name='promotion_create'),
    url(r'^list/$', PromotionList.as_view(), name='promotion_list'),
    url(r'^edit/(?P<id>[0-9]+)/$', PromotionEdit.as_view(), name='promotion_edit'),
    url(r'^delete/(?P<id>[0-9]+)/$', PromotionList.delete_promotion, name='delete_promotion'),
)
