"""EmbelezaMais URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from landing.views import home
from companyDashboard.views import dashboardRender
from search.views import searchPageRender

from user import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register_client/', views.register_client_view, name='register_client_view'),
    url(r'^register_company/', views.register_company_view, name='register_view'),
    url(r'^confirm/(?P<activation_key>\w+)/', views.register_confirm,
        name='confirm_account'),
    url(r'^$', home, name="landing_home"),
    url(r'dashboard/', dashboardRender, name="dashboard"),
    url(r'search/', searchPageRender, name="search"),
    url(r'^delete_company/(?P<id>[0-9]+)/$', views.CompanyAction.delete_company_view, name='delete_company_view'),

]
