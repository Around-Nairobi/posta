from django.urls import path

from . import views

urlpatterns = [
    path('tm', views.index, name='index'),
]
