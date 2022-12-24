from django.shortcuts import render
from . models import Orderlist

def showdep1(request):
    reso = Orderlist.objects.all()
    return render(request, 'cart.html',{"dataep1":reso})