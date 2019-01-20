from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pages', views.facebook_pages, name='facebook_pages'),
    path('privacy_policy', views.privacypolicy, name='privacypolicy'),
    path('terms_service', views.termsservice, name='termsservice')
]
