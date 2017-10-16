from django.test import TestCase

from user.models import Company, User, Client
from .forms import (ClientRegisterForm, CompanyRegisterForm, ClientEditForm,
                    CompanyEditForm, CompanyLoginForm)

from geoposition.fields import Geoposition


class TestUserForms(TestCase):
    def setUp(self):
        self.phone = 1231231231
        self.has_parking_availability = True
        self.target_genre = 'Feminino'
        self.description = 'Salão de Beleza com ....'
        self.position = Geoposition(15.87732, 15.87732)
        self.email = "email@email.com"
        self.password = "password"
        self.name = "Salão de Beleza"

    def test_company_register_form(self):
        form_data = {'has_parking_availability': self.has_parking_availability,
                     'target_genre': self.target_genre,
                     'description': self.description,
                     'position': self.position,
                     'email': self.email,
                     'password': self.password,
                     'password_confirmation': self.password,
                     'name': self.name,
                     'latitude': self.position.latitude,
                     'longitude': self.position.longitude
                     }
        form = CompanyRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_client_form(self):
        form_data = {'email': self.email,
                     'password': self.password,
                     'password_confirmation': self.password,
                     'name': self.name,
                     'phone_number': self.phone
                     }
        form = ClientRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_client_edit_form(self):
        form_data = {'name': self.name,
                     'phone_number': self.phone
                     }
        form = ClientEditForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_company_edit_form(self):
        form_data = {'target_genre': self.target_genre,
                     'description': self.description,
                     'name': self.name
                     }
        form = CompanyEditForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_company_login_form(self):
        form_data = {'name': self.name,
                     'password': self.password
                     }
        form = CompanyLoginForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_company_save(self):
        company = Company.objects.create_user(email=self.email,
                                              password=self.password, name=self.name,
                                              target_genre=self.target_genre,
                                              has_parking_availability=self.has_parking_availability,
                                              description=self.description, position=self.position)

        company_database = Company.objects.get(id=company.id)
        self.assertEqual(str(company_database), str(company))

    def test_client_save(self):
        client = Client.objects.create_user(email=self.email,
                                            password=self.password, name=self.name,
                                            phone_number=self.phone)

        client_database = Client.objects.get(id=client.id)
        self.assertEqual(str(client_database.name), str(client.name))

    def test_user_save(self):
        user = User.objects.create_user(email=self.email,
                                        password=self.password, name=self.name)

        user_database = User.objects.get(id=user.id)
        self.assertEqual(str(user_database.name), str(user.name))
