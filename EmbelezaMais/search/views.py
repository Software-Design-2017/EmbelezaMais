from django.shortcuts import render


# Create your views here.
def searchPageRender(request):

    return render(request, 'search.html')
