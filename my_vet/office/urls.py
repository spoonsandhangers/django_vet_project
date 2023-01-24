# app level urls (office)
from django.urls import path
from . import views

app_name = 'office'

urlpatterns = [
    path('', views.home, name='home'),
    path('allcustomers/', views.allcustomers, name='allcustomers'),
    path('details/<int:id>', views.details, name='details'),
    path('<int:year>/<str:month>/', views.dates, name='dates'),
    path('add_customers', views.add_customers, name='add_customers'),
    path('search_customers_result', views.search_customers_result, name='search_customers_result'),
]