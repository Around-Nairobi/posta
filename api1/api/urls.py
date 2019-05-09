"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('posta/admin/', admin.site.urls),
    path('', include('posta.urls')),
    path('posta/crowdie/', include('CROWDIE.urls')),
    path('posta/hschool/', include('HSCHOOL.urls')),
    path('posta/mb/', include('MB.urls')),
    path('posta/msafiri/', include('MSAFIRI.urls')),
    path('posta/tbtia/', include('TBTIA.urls')),
    path('posta/tm/', include('TM.urls')),
]
