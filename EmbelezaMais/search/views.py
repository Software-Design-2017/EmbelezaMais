# standard library
import logging
import abc

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


class SearchList(ListView):
    model = Company
    template_name = 'client_view_companies.html'
    context_object_name = 'companies'
    paginate_by = 10
    search = {}

    def get_queryset(self):

        return Company.objects.filter(**self.search)

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST or request.GET)

        if form.is_valid():
            logger.debug("Search form was valid.")
            logger.debug("Search form: " + str(form.cleaned_data))

            # latitude = float(str(form.cleaned_data.get('latitude')))
            # longitude = float(str(form.cleaned_data.get('longitude')))
            target_genre = form.cleaned_data.get('target_genre')
            has_parking_availability = form.cleaned_data.get('has_parking_availability')

            # local = SearchLocation(latitude=latitude, longitude=longitude)
            genre = SearchTargetGenre(target_genre=target_genre)
            parking = SearchParking(has_parking_availability=has_parking_availability)

            search_many = SearchMany()

            # Cleaning list of searchs to have just one of each one.
            search_many.list_search = []
            search_many.add(genre)
            search_many.add(parking)

            search_many.get_type_search()

            self.search = search_many.researches
            logger.debug("Search in Compnay DB: " + str(self.search))

        else:
            logger.debug("Search form was invalid.")
            logger.debug("Search form: " + str(form.cleaned_data))

        return render(request, self.template_name, {'companies': self.get_queryset()})


class Search():
    @abc.abstractmethod
    def __init__(self, **kwargs):
        return

    @abc.abstractmethod
    def get_type_search(self):
        return


class SearchLocation(Search):
    latitude = None
    longitude = None

    def __init__(self, **kwargs):
        self.latitude = kwargs.get('latitude')
        self.longitude = kwargs.get('longitude')

    def get_type_search(self):
        if self.longitude is not None and self.latitude is not None:
            return {'longitude': self.longitude}  # TODO(Ronyell) Change to real search.
        else:
            return {}


class SearchTargetGenre(Search):
    target_genre = None

    def __init__(self, **kwargs):
        self.target_genre = kwargs.get('target_genre')

    def get_type_search(self):
        if self.target_genre is not None:
            if self.target_genre != 'All':
                return {'target_genre': self.target_genre}
            else:
                return {}
        else:
            return {}


class SearchParking(Search):
    has_parking_availability = None

    def __init__(self, **kwargs):
        self.has_parking_availability = kwargs.get('has_parking_availability')

    def get_type_search(self):
        if self.has_parking_availability is not None:

            if self.has_parking_availability is True:
                return {'has_parking_availability': self.has_parking_availability}
            else:
                return{}
        else:
            return {}


class SearchMany(Search):
    list_search = []
    researches = {}

    def add(self, search):
        self.list_search.append(search)

    def remove(self, search):
        self.list_search.remove(search)

    def get_type_search(self):
        self.researches = {}
        for search in self.list_search:
            self.researches.update(search.get_type_search())


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
