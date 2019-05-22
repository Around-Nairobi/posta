from django.urls import path

from . import views

urlpatterns = [
    path('tbtia', views.index, name='index'),
    path('post_on_tbtia_page', views.post_on_tbtia_page, name='post_on_tbtia_page'),

]
