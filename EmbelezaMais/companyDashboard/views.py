from django.shortcuts import render


# Create your views here.
def dashboardRender(request):

    return render(request, 'dashboard.html')
