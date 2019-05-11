from django.urls import path

from . import views

urlpatterns = [
    path('crowdie', views.index, name='index'),
    path('post_on_crowdie_page', views.post_on_crowdie_page, name='post_on_crowdie_page'),
]
