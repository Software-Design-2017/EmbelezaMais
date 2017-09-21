from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from user.decorators import user_is_company


@user_is_company
@login_required
def dashboardRender(request):

    return render(request, 'dashboard.html')
