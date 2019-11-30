from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from django.views.generic import View
from .forms import RegistrationForm
from .social import GoogleWorker
from django.shortcuts import render
from django.http import HttpResponseRedirect


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

    def get(self,request):
        SignUpForm = RegistrationForm(request)
        return render(request, self.template_name, {'form':SignUpForm})


class GoogleWorkerView(View):

    def get(self,request):
        GWorker = GoogleWorker()
        email = GWorker.run_flow()
        return HttpResponseRedirect(f'/test/?email={email}')
