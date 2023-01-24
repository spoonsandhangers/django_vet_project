from django.contrib import admin
from .models import customer, vet, pet
# Register your models here.

admin.site.register(customer)
admin.site.register(pet)
admin.site.register(vet)