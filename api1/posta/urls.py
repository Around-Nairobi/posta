from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('facebook_graph_call', views.facebook_graph_call, name='facebook_graph_call'),
    path('runner', views.runner, name='runner'),
    path('privacy_policy', views.privacypolicy, name='privacypolicy'),
    path('terms_service', views.termsservice, name='termsservice')
]
