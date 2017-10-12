# standard library
import logging

# Django
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.template.loader import render_to_string

# third part
# from geoposition.fields import Geoposition

# local Django
from user.models import Company
from service.models import ServiceNail, Combo, ServiceMakeUp, ServiceHair, ServiceBeard, Service
from search.forms import SearchForm
# from . import constants

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('EmbelezaMais')


# Create your views here.
def searchPageRender(request):
    form = SearchForm(request.POST or None)
    latitude = float(str(form.get('latitude')))
    longitude = float(str(form.get('longitude')))
    print(str(latitude))
    print(str(longitude))
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

    def get(self, request, *args, **kwargs):
        service = Service.objects.get(pk=self.kwargs.get('pk'))
        data = dict()
        type_service = self.verify_type(service)
        context = {'service': service,
                   'type_service': type_service}
        template_name = 'show_service.html'
        data['html_show'] = render_to_string(template_name, context, request=request)
        return JsonResponse(data)

    def verify_type(self, service):
        is_nail = hasattr(service, 'servicenail')
        is_combo = hasattr(service, 'combo')
        is_makeup = hasattr(service, 'servicemakeup')
        is_hair = hasattr(service, 'servicehair')
        is_beard = hasattr(service, 'servicebeard')

        if is_nail:
            return 'servicenail'
        elif is_combo:
            return 'combo'
        elif is_makeup:
            return 'servicemakeup'
        elif is_hair:
            return 'servicehair'
        elif is_beard:
            return 'services_beard'
        else:
            pass

#
# class Search(ListView):
#     form = SearchForm(request.POST or None)
#     latitude = constants.STANDARD_LATITUDE
#     longitude = constants.STANDARD_LONGITUDE
#     position = Geoposition(latitude, longitude)
#     model = Company
#     template_name = 'client_view_companies.html'
#     context_object_name = 'companies'
#     paginate_by = 10
#
#     def get_queryset(self):
#         return Company.objects.all()
#
#     # def get_search_location(request):
#     #     form = SearchForm(request.POST or None)
#     #
#     #     if form.is_valid():
#     #         # latitude = float(str(form.cleaned_data.get('latitude')))
#     #         # longitude = float(str(form.cleaned_data.get('longitude')))
#     #         # position = Geoposition(latitude, longitude)
#     #
#     #         return render(request, "search.html", {"form": form})
#     #
#     #     else:
#     #         pass
#     #
#     #     return render(request, "landing.html", {"form": form})
