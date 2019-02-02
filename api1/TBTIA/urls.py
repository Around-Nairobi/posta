from django.urls import path

from . import views

urlpatterns = [
    path('tbtia', views.index, name='index'),
]
