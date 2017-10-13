from django.conf.urls import url
from .views import (
    CompaniesList,
    CompanyDetail,
    ServiceDetail,
    SearchList,
)

urlpatterns = (
    url(r'^companies_list/', CompaniesList.as_view(), name='companies_list'),
    url(r'^company/(?P<pk>[0-9]*)/$', CompanyDetail.as_view(), name='show_company'),
    url(r'^service/(?P<pk>[0-9]*)/$', ServiceDetail.as_view(), name='show_service'),
    url(r'^$', SearchList.as_view(), name="search"),
)
