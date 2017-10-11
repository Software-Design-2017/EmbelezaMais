from django import forms

from .models import (
    Service, Combo, ServicesCombo, ServiceNail, ServiceMakeUp, ServiceBeard, ServiceHair
)


class ServiceForm(forms.ModelForm):
    company_create = None

    def __init__(self, **kw):
        super(ServiceForm, self).__init__(**kw)
        self.fields['service_in_combo'].queryset = Service.objects.filter(company=self.company_create,
                                                                          combo__isnull=True)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    @staticmethod
    def __create_service_form__(company):
        ServiceForm.company_create = company
        return ServiceForm

    class Meta:
        model = ServicesCombo
        fields = ['service_in_combo']


class ComboForm():
    company = None
    ServiceComboFormSet = forms.inlineformset_factory(Combo, ServicesCombo,
                                                      form=ServiceForm, extra=0,
                                                      fk_name='service_combo',
                                                      min_num=2, validate_min=True)

    def __init__(self, company):
        self.ServiceComboFormSet.form = ServiceForm.__create_service_form__(company=company)


class FormService(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FormService, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Service
        exclude = ['company']


class ServiceNailForm(FormService):

    class Meta:
        model = ServiceNail
        exclude = ['company']


class ServiceMakeUpForm(FormService):
    class Meta:
        model = ServiceMakeUp
        exclude = ['company']


class ServiceBeardForm(FormService):
    class Meta:
        model = ServiceBeard
        exclude = ['company']


class ServiceHairForm(FormService):
    class Meta:
        model = ServiceHair
        exclude = ['company']
