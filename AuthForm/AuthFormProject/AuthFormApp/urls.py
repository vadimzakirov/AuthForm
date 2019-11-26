from .import views
from django.urls import path
from .views import RegistrationView

urlpatterns = [
    path('test/', RegistrationView.as_view(), name ="test")
]
