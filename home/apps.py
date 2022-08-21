from email.policy import default
from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class StoreAdminConfig(AdminConfig):
    default_site = 'home.admin.StoreAdmin'
    
class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
