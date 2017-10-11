# Django
from django.shortcuts import (
    redirect
)
from django.core.exceptions import PermissionDenied

from service.models import (
    Service
)


def define_author_service(method):
    """
    Verify if user is author service.
    """
    def wrap(request, id, *args, **kwargs):
        service = Service.objects.get(id=id)
        is_author_service = request.user.email == service.company.email
        if is_author_service:
            return method(request, id, *args, **kwargs)
        else:
            return redirect('/')

    return wrap


def user_is_company(method):
    """
    Verify if user is company.
    """
    def wrap(request, *args, **kwargs):
        is_company = hasattr(request.user, 'company')

        if is_company:
            return method(request, *args, **kwargs)
        else:
            return redirect('/')

    return wrap


def user_is_logged(method):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated():
            is_company = hasattr(request.user, 'company')
            is_client = hasattr(request.user, 'client')
            if is_company:
                return redirect('/dashboard')
            elif is_client:
                return redirect('/search')  # TODO make dashboard client
            else:
                return redirect('/search')
        else:
            return method(request, *args, **kwargs)

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
