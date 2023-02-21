# urls in myapi app
from django.urls import path

from . import views

app_name = 'myapi'

urlpatterns = [
    path('', views.users, name = 'users'),
]

