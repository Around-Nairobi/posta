from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('facebook_graph_call', views.facebook_graph_call, name='facebook_graph_call'),
    path('privacy_policy', views.privacypolicy, name='privacypolicy'),
    path('terms_service', views.termsservice, name='termsservice'),
    path('email', views.read_email_from_gmail, name='read_email_from_gmail')
]
