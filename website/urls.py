from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='about'),
    path('pricing.html', views.pricing, name='pricing'),
    path('services.html', views.services, name='services'),
    path('consulta.html', views.consulta, name='consulta'),
]