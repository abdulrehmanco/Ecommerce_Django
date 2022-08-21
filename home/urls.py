from django.urls import path
from . import views
from.views import *


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact',views.contacts,name='contacts'),
    path('home',views.homepage,name='home'),
    path('about',views.about,name='about'),
    path('product',views.products,name='product'),
    path('add-product',views.addprod,name='addprod'),
    path('blog-list',views.blog,name='blog-list'),
    path('admin-dash',views.admindash,name='admin-dash'),
    path('delete-prod/<str:pk>',views.deleteprod,name='delete-prod'),
    path('<slug:slug>', views.detail, name='detail'),

]

