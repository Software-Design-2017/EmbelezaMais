from django.shortcuts import render
from django.views.generic import ListView, DetailView

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
        services = Service.objects.filter(company=context['company'])
        self.get_services(context, services)

        return context

    def get_services(self, context, services):
        context['services_nail'] = []
        context['services_combo'] = []
        context['services_makeup'] = []
        context['services_hair'] = []
        context['services_beard'] = []

        for service in services:
            if hasattr(service, 'servicenail'):
                context['services_nail'].append(service)
            elif hasattr(service, 'combo'):
                context['services_combo'].append(service)
            elif hasattr(service, 'servicemakeup'):
                context['services_makeup'].append(service)
            elif hasattr(service, 'servicehair'):
                context['services_hair'].append(service)
            elif hasattr(service, 'servicebeard'):
                context['services_beard'].append(service)
            else:
                # Nothing to do.
                pass
