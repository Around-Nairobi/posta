from django.urls import path

from . import views

urlpatterns = [
    path('crowdie', views.index, name='index'),
]
