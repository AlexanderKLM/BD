import webbrowser

from django.shortcuts import render
from django.http import HttpRequest, request
# Create your views here.
import time
import string
import pywebio.output
from django.shortcuts import render
from . models import Shoplist
from pywebio.input import *
from pywebio.output import *
import psycopg2
import requests
from django.http import HttpResponseRedirect
from tkinter import *
"""
def tablecheck():
    conn = psycopg2.connect(dbname='postgres', user='postgres',
                            password='Torus5', host='localhost')
    login = "Vasys"
    cursor = conn.cursor()
    datainp = []
    i = 0
    while i < 25:
        cursor.execute('SELECT * FROM contracts')
        r = cursor.fetchone()
        put_table([["The"],[r ]])
        i = i + 1

def callback(url):
   webbrowser.open_new_tab(url)


#put_button('Просмотреть доставку', onclick=callback("http://127.0.0.1:8000/delivery/"))
"""
def showd(request):
    res = Shoplist.objects.all()
    return render(request, 'ordsys.html',{"data":res})