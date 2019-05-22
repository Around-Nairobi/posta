from django.urls import path

from . import views

urlpatterns = [
    path('tm', views.index, name='index'),
    path('post_on_tm_page', views.post_on_tm_page, name='post_on_tm_page'),

]
