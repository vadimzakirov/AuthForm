from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from .forms import RegistrationForm
from django.shortcuts import render

class RegistrationView(TemplateView):

    template_name = 'registration/signup.html'

    def post(self,request):
        SignUpForm = RegistrationForm(request)
        if not SignUpForm.is_valid():
            return render(request, self.template_name,
            {
            'errors': SignUpForm.errors,
            'form':SignUpForm
            })
        else:
            SignUpForm.create_user()
            return render(request, self.template_name,
            {
            'success': True,
            'form':SignUpForm
            })
