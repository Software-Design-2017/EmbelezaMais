from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from user.models import Company

from service.models import ServiceNail, Combo, ServiceMakeUp, ServiceHair, ServiceBeard, Service


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
        self.get_services(context)

        return context

    def get_services(self, context):
        context['services_nail'] = ServiceNail.objects.filter(company=context['company'])
        context['services_combo'] = Combo.objects.filter(company=context['company'])
        context['services_makeup'] = ServiceMakeUp.objects.filter(company=context['company'])
        context['services_hair'] = ServiceHair.objects.filter(company=context['company'])
        context['services_beard'] = ServiceBeard.objects.filter(company=context['company'])


class ServiceDetail(DetailView):
    model = Service
    template_name = 'show_service.html'
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super(ServiceDetail, self).get_context_data(**kwargs)
        context['service'] = Service.objects.get(pk=self.kwargs.get('pk'))
