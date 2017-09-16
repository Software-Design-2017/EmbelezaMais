from django.shortcuts import render
from .forms import CompanyRegisterForm
from .models import Company


def register_view(request):
    form = CompanyRegisterForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        name = form.cleaned_data.get('name')
        description = form.cleaned_data.get('description')
        target_genre = form.cleaned_data.get('target_genre')
        location = form.cleaned_data.get('location')
        Company.objects.create_user(email=email, password=password, name=name, target_genre=target_genre,
                                    description=description, location=location)

    else:
        pass

    return render(request, "register_form.html", {"form": form})
