from django.shortcuts import render

# local Django
from user.decorators import user_is_logged


@user_is_logged
def home(request):

    return render(request, 'landing.html')
