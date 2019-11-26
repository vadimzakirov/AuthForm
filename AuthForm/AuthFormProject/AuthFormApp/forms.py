""" Form's Validators and Constructors """

from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import validate_email
from django.core.validators import validate_slug
from django.contrib.auth.models import  User


class RegistrationForm(object):

    def __init__(self, request):
        self.request = request.POST

    def is_valid(self):
        self.errors = {}
        self.email = self.request.get('email')
        self.password = self.request.get('password1')
        self.confirmated_password = self.request.get('password2')
        self.first_name = self.request.get('first_name')
        self.last_name = self.request.get('last_name')
        if self.email:
            try:
                validate_email(self.email)
                valid_email = True
                try:
                    user_to_check = User.objects.get(email = self.email)
                    valid_email = False
                    self.errors['user'] = f'User {self.email} already exist'
                except ObjectDoesNotExist:
                    valid_email = True
            except ValidationError:
                valid_email = False
                self.errors['email'] = 'Please enter valid e-mail address'
        if (self.password == self.confirmated_password) and self.password:
            try:
                validate_slug(self.password)
                valid_password = True
            except ValidationError:
                valid_password = False
                self.errors['password'] = 'Please enter valid password'
        if (self.password != self.confirmated_password) and self.password :
                valid_password = False
                self.errors['confirm'] = 'Your password and confirmed password must match.'
        if self.first_name and self.last_name:
            try:
                validate_slug(self.first_name)
                validate_slug(self.last_name)
                valid_name = True
            except ValidationError:
                valid_name = False
                self.errors['name'] = 'Please enter valid First/Last name'

        if valid_name and valid_email and valid_password:
            return True
        else:
            return False

    def create_user(self):
        new_user = User(username = self.email, password = self.password)
        new_user.email = self.email
        new_user.first_name = self.first_name
        new_user.last_name = self.last_name
        new_user.save()
