"""Mshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views
from django.urls import path, include
from pywebio.platform.django import webio_view
from .views import *

webio_view_func = webio_view(views.login)

urlpatterns = [
    path('ordersystem/', include('ordersystem.urls')),
 #   path('', LoginUser.as_view(), name='login'),
   # path('', views.index, name='index'),
    path('', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),

]