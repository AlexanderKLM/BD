from django.shortcuts import render


def index(request):
    return render(request, 'delivery/delivery.html')


# Create your views here.
