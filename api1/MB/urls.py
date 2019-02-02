from django.urls import path

from . import views

urlpatterns = [
    path('mb', views.index, name='index'),
]
