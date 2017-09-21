# Django
from django.core.exceptions import PermissionDenied

# local Django
from .models import (
    Company
)

def user_is_company(method):
    def wrap(request, *args, **kwargs):
        is_company =  hasattr(request.user, 'company')
        print(is_company)
        if is_company:
            return method(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap
