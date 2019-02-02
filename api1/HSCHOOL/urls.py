from django.urls import path

from . import views

urlpatterns = [
    path('hschool', views.index, name='index'),
]
