from django.shortcuts import render

# local Django
from search.forms import SearchForm


def home(request):
    form = SearchForm()
    return render(request, 'landing.html', {'form': form})
