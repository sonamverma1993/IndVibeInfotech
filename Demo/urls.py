from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('Contact', views.contact,name='Contact'),
]