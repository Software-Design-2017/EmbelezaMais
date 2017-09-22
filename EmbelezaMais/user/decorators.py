# Django
from django.core.exceptions import PermissionDenied


def user_is_company(method):
    def wrap(request, *args, **kwargs):
        is_company = hasattr(request.user, 'company')
        print(is_company)
        if is_company:
            return method(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap


def user_is_client(method):
    def wrap(request, *args, **kwargs):
        is_client = hasattr(request.user, 'client')
        print(is_client)
        if is_client:
            return method(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap
