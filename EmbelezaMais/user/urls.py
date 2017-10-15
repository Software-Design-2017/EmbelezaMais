from django.conf.urls import url
from .views import (
    ClientRegisterView,
    CompanyResgisterView,
    CountConfirmation,
    CompanyAction,
    LoginCompanyView,
    LogoutView,
    LoginClientView,
    ClientProfile,
)

urlpatterns = (
    url(r'^login_company/', LoginCompanyView.as_view(), name='login_view'),
    url(r'^login_client/', LoginClientView.as_view(), name='login_client'),
    url(r'^logout_company/', LogoutView.as_view(), name='logout_view'),
    url(r'^register_client/', ClientRegisterView.register_client,
        name='register_client_view'),
    url(r'^register_company/', CompanyResgisterView.register_company, name='register_view'),
    url(r'^confirm/(?P<activation_key>\w+)/', CountConfirmation.register_confirm, name='confirm_account'),
    url(r'^profile/(?P<email>[\w|\W]+)/', CompanyAction.company_profile, name='profile'),
    url(r'^edit/(?P<email>[\w|\W]+)/', CompanyAction.company_edit_profile_view, name='edit'),
    url(r'^client_profile/(?P<email>[\w|\W]+)/', ClientProfile.client_profile, name='client_profile'),
    url(r'^edit_client/(?P<email>[\w|\W]+)/', ClientProfile.client_edit_profile_view, name='edit_client'),
    url(r'^delete_company/(?P<email>[\w|\W]+)/$', CompanyAction.delete_company_view, name='delete_company_view'),
)
