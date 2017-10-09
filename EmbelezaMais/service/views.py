from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, ListView, FormView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect

from .models import (
    Service, Combo, ServiceHair, ServiceNail, ServiceMakeUp, ServiceBeard
)

from .forms import (
    ComboForm, ServiceNailForm, ServiceMakeUpForm, ServiceBeardForm, ServiceHairForm
)

from . import constants
from user.decorators import (
    user_is_company, define_author_service
)


class ServiceList(ListView):
    model = Service
    template_name = 'service_list.html'
    context_object_name = 'services'
    paginate_by = 10

    def get_queryset(self):
        return Service.objects.filter(company=self.request.user.company)

    @login_required
    @user_is_company
    @define_author_service
    def delete_service(request, id):
        service = Service.objects.get(id=id)
        service.delete()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ServiceComboCreate(CreateView):
    model = Combo
    fields = ['name', 'specification', 'description', 'price']
    template_name = 'combo_service_form.html'
    success_url = reverse_lazy('service_list')

    @method_decorator(login_required)
    @method_decorator(user_is_company)
    def dispatch(self, *args, **kwargs):
        return super(ServiceComboCreate, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        data = super(ServiceComboCreate, self).get_context_data(**kwargs)
        combo_form = ComboForm(company=self.request.user.company)

        if self.request.POST:
            data['services'] = combo_form.ServiceComboFormSet(self.request.POST)
        else:
            data['services'] = combo_form.ServiceComboFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        services = context['services']

        with transaction.atomic():
            if services.is_valid():
                services_validate = self._validate_quantity(services, form)
            else:
                return super(ServiceComboCreate, self).form_invalid(form)

            # Register combo and your creator
            self.object = form.save(commit=False)
            self.object.company = self.request.user.company
            self.object.save()

            for service_in_combo in services_validate:
                    self.object.combo.add(service_in_combo)

            self.object.combo.save()
            print(self.object.services)
        return super(ServiceComboCreate, self).form_valid(form)

    def _validate_quantity(self, services, form):
        if len(services) > 1:
            services_validate = []
            number_of_filled = len(services)

            # Checks the number of forms filled
            for service_compound in services:
                get_service = service_compound.cleaned_data.get('service_in_combo')

                # Case form is filled the object is add in list of combo
                if get_service:
                    services_validate.append(service_compound.cleaned_data.get('service_in_combo'))
                else:
                    number_of_filled = number_of_filled - 1

            if number_of_filled > 1:
                return services_validate
            else:
                return super(ServiceComboCreate, self).form_invalid(form)
        else:
            return super(ServiceComboCreate, self).form_invalid(form)


class ServiceNailCreate(FormView):
    template_name = 'service_form.html'
    form_class = ServiceNailForm
    success_url = '/service/list/'

    @method_decorator(login_required)
    @method_decorator(user_is_company)
    def dispatch(self, *args, **kwargs):
        return super(ServiceNailCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        self.service = form.save(commit=False)
        self.service.company = self.request.user.company
        self.service.save()

        return super(ServiceNailCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ServiceNailCreate, self).get_context_data(**kwargs)
        context['name'] = constants.NAIL_SERVICE
        return context


class ServiceMakeUpCreate(FormView):
    template_name = 'service_form.html'
    form_class = ServiceMakeUpForm
    success_url = '/service/list/'

    @method_decorator(login_required)
    @method_decorator(user_is_company)
    def dispatch(self, *args, **kwargs):
        return super(ServiceMakeUpCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        self.service = form.save(commit=False)
        self.service.company = self.request.user.company
        self.service.save()

        return super(ServiceMakeUpCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ServiceMakeUpCreate, self).get_context_data(**kwargs)
        context['name'] = constants.MAKE_UP_SERVICE
        return context


class ServiceBeardCreate(FormView):
    template_name = 'service_form.html'
    form_class = ServiceBeardForm
    success_url = '/service/list/'

    @method_decorator(login_required)
    @method_decorator(user_is_company)
    def dispatch(self, *args, **kwargs):
        return super(ServiceBeardCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        self.service = form.save(commit=False)
        self.service.company = self.request.user.company
        self.service.save()

        return super(ServiceBeardCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ServiceBeardCreate, self).get_context_data(**kwargs)
        context['name'] = constants.BEARD_SERVICE
        return context


class ServiceHairCreate(FormView):
    template_name = 'service_form.html'
    form_class = ServiceHairForm
    success_url = '/service/list/'

    @method_decorator(login_required)
    @method_decorator(user_is_company)
    def dispatch(self, *args, **kwargs):
        return super(ServiceHairCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        self.service = form.save(commit=False)
        self.service.company = self.request.user.company
        self.service.save()

        return super(ServiceHairCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ServiceHairCreate, self).get_context_data(**kwargs)
        context['name'] = constants.HAIR_SERVICE
        return context


class ServiceComboEdit(UpdateView):
    model = Combo
    fields = ['name', 'specification', 'description', 'price']
    template_name = 'combo_service_form.html'
    success_url = reverse_lazy('service_list')

    def form_valid(self, form):
        context = self.get_context_data()
        services = context['services']

        with transaction.atomic():
            if services.is_valid():
                services_validate = self._validate_quantity(services, form)
            else:
                return super(ServiceComboCreate, self).form_invalid(form)

            # Register combo and your creator
            self.object = form.save(commit=False)
            self.object.company = self.request.user.company
            self.object.save()

            for service_in_combo in services_validate:
                    self.object.combo.add(service_in_combo)

            self.object.combo.save()
            print(self.object.services)
        return super(ServiceComboCreate, self).form_valid(form)

    def _validate_quantity(self, services, form):
        if len(services) > 1:
            services_validate = []
            number_of_filled = len(services)

            # Checks the number of forms filled
            for service_compound in services:
                get_service = service_compound.cleaned_data.get('service_in_combo')

                # Case form is filled the object is add in list of combo
                if get_service:
                    services_validate.append(service_compound.cleaned_data.get('service_in_combo'))
                else:
                    number_of_filled = number_of_filled - 1

            if number_of_filled > 1:
                return services_validate
            else:
                return super(ServiceComboCreate, self).form_invalid(form)
        else:
            return super(ServiceComboCreate, self).form_invalid(form)


class ServiceEdit(UpdateView):
    form_class = None
    model = None
    template_name = 'service_form.html'
    success_url = '/service/list/'

    def get(self, request, *args, **kwargs):
        service = Service.objects.get(pk=self.kwargs.get('pk'))
        self.model = self.type_model(service)
        self.form_class = self.type_form(service)
        return super(ServiceEdit, self).post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        service = Service.objects.get(pk=self.kwargs.get('pk'))
        self.model = self.type_model(service)
        self.form_class = self.type_form(service)
        return super(ServiceEdit, self).post(request, *args, **kwargs)

    def type_model(self, service):
        is_nail = hasattr(service, 'servicenail')
        is_combo = hasattr(service, 'combo')
        is_makeup = hasattr(service, 'servicemakeup')
        is_hair = hasattr(service, 'servicehair')
        is_beard = hasattr(service, 'servicebeard')

        if is_nail:
            return ServiceNail
        elif is_makeup:
            return ServiceMakeUp
        elif is_combo:
            # TODO Fixing model combo
            return Combo
        elif is_hair:
            return ServiceHair
        elif is_beard:
            return ServiceBeard
        else:
            pass

    def type_form(self, service):
        is_nail = hasattr(service, 'servicenail')
        is_combo = hasattr(service, 'combo')
        is_makeup = hasattr(service, 'servicemakeup')
        is_hair = hasattr(service, 'servicehair')
        is_beard = hasattr(service, 'servicebeard')

        if is_nail:
            serviceNail = ServiceNailForm
            return serviceNail
        elif is_makeup:
            serviceMakeUp = ServiceMakeUpForm
            return serviceMakeUp
        elif is_combo:
            self.template_name = "combo_service_form.html"
            return ComboForm
        elif is_hair:
            serviceHair = ServiceHairForm
            return serviceHair
        elif is_beard:
            serviceBeard = ServiceBeardForm
            return serviceBeard
        else:
            pass


class ServiceNailEdit(UpdateView):
    model = ServiceNail
    template_name = 'service_form.html'
    form_class = ServiceNailForm
    success_url = '/service/list/'


class ServiceMakeUpEdit(UpdateView):
    model = ServiceMakeUp
    template_name = 'service_form.html'
    form_class = ServiceMakeUpForm
    success_url = '/service/list/'


class ServiceBeardEdit(UpdateView):
    model = ServiceBeard
    template_name = 'service_form.html'
    form_class = ServiceBeardForm
    success_url = '/service/list/'


class ServiceHairEdit(UpdateView):
    model = ServiceHair
    template_name = 'service_form.html'
    form_class = ServiceHairForm
    success_url = '/service/list/'
