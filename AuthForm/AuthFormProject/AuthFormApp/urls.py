from .import views
from django.urls import path
from .views import RegistrationView
from .views import GoogleWorkerView
from .social import GoogleWorker
from .social import OAuthCallback

urlpatterns = [
    path('test/', RegistrationView.as_view(), name ="test"),
    path('google/', GoogleWorker.as_view(), name ="Google"),
    path('oauthcallback/', OAuthCallback.as_view(), name ="Callback")
]
