from django.urls import path

from . import views

urlpatterns = [
    path('mb', views.index, name='index'),
    path('get_twitter', views.get_twitter, name='get_twitter'),
]
