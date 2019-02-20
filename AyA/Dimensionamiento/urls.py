"""Dimensionamiento URL Configuration

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
from django.conf.urls import url
from data.models import Homepage

urlpatterns = [
    url('^$',Homepage.as_view(),name='homepage'),
    url('user/',include('users.urls',namespace='users')),
    url('servicios/',include('servicios.urls',namespace='servicios')),
    url('servers/',include('servers.urls',namespace='servers')),
    url('utilization/',include('utilization.urls',namespace='utilization')),
]
