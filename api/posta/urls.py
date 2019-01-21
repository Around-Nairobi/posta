from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('facebook_graph_call', views.facebook_pages, name='facebook_graph_call'),
    path('privacy_policy', views.privacypolicy, name='privacypolicy'),
    path('terms_service', views.termsservice, name='termsservice')
]
