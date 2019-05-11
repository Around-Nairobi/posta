from django.urls import path

from . import views

urlpatterns = [
    path('mb', views.index, name='index'),
    path('post_on_mb_page', views.post_on_mb_page, name='post_on_mb_page'),
    path('sample', views.sample_request, name='sample'),

]
