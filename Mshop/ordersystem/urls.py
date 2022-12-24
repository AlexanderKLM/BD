from django.urls import path, include
from . import views
from pywebio.platform.django import webio_view
from django.contrib import admin

#webio_view_func = webio_view(views.tablecheck)
urlpatterns = [
    path('', views.showd),

]