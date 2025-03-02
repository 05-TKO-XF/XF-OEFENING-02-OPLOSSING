from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aanhuis/', views.aanhuis, name='aanhuis'),
    path('winkel/', views.winkel, name='winkel'),
    path('contact/', views.contact, name='contact'),
]