from django.contrib import admin
from .models import product, contact, Catogery
# Register your models here.

class StoreAdmin(admin.AdminSite):
    site_header='Admin Area'

store_site =StoreAdmin(name='StoreAdmin')
store_site.register(product),
store_site.register(contact),
store_site.register(Catogery),

