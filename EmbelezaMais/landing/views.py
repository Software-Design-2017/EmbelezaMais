from django.shortcuts import render

# local Django
from user.decorators import user_is_logged
from search.forms import SearchForm


@user_is_logged
def home(request):
    form = SearchForm()
    return render(request, 'landing.html', {'form': form})
