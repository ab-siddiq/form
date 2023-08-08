from django.urls import path
from . import views

urlpatterns = [
    path('app/',views.home),
    path('form/',views.submit_form,name='formpage'),
    path('about/',views.about,name='aboutpage'),
    path('django_form/',views.DjangoForm,name='djangoForm'),
]
