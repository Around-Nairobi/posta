from django.urls import path

from . import views

urlpatterns = [
    path('hschool', views.index, name='index'),
    path('post_on_hschool_page', views.post_on_hschool_page, name='post_on_hschool_page'),

]
