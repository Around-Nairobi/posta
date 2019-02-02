from django.urls import path

from . import views

urlpatterns = [
    path('msafiri', views.index, name='index'),
]
