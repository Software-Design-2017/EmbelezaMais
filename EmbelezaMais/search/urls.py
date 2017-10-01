from django.conf.urls import url
from .views import (
    searchPageRender,
    CompaniesList,
    CompanyDetail,
)

urlpatterns = (
    url(r'^companies_list/', CompaniesList.as_view(), name='companies_list'),
    url(r'^company/(?P<pk>[0-9]*)/$', CompanyDetail.as_view(), name='show_company'),
    url(r'^$', searchPageRender, name="search"),
)
