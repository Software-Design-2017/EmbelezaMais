from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect

from user.models import Company

from service.models import Service


# Create your views here.
def searchPageRender(request):

    return render(request, 'search.html')


class CompaniesList(ListView):
    model = Company
    template_name = 'client_view_companies.html'
    context_object_name = 'companies'
    paginate_by = 10

    def get_queryset(self):
        return Company.objects.all()


class CompanyDetail(DetailView):
    model = Company
    template_name = 'company_detail.html'
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super(CompanyDetail, self).get_context_data(**kwargs)
        context['company'] = Company.objects.get(pk=self.kwargs.get('pk'))
        context['services'] = Service.objects.filter(company=context['company'])
        return context
