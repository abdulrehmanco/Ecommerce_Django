from django.db import models
from webstore.utils import unique_slug_generator
from django.db.models.signals import pre_save
from PIL import Image
from django.contrib.auth.models import User

# Create your models here.

class Catogery(models.Model):
    name =models.CharField(max_length=30, null=True)
    @staticmethod
    def get_all_catogeries():
        return Catogery.objects.all()
    def __str__(self):
         return self.name


class product(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    slug = models.SlugField(max_length=130, blank=True, null=True)
    catogery = models.ForeignKey(Catogery, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="media/images")
    price = models.IntegerField()
    @staticmethod
    def get_all_products_by_ID(catogery_id):
        if catogery_id:
            return product.objects.filter(catogery=catogery_id)
        else:
            return product.objects.all()
    def __str__(self):
         return self.title
def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_generator, sender=product)     



  
class contact(models.Model):
    name = models.CharField(max_length=100)
    email =models.EmailField(max_length=200)
    message =models.TextField(max_length=1000)
    def __str__(self):
         return self.name
     
