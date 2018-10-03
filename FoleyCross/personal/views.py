from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'moreContent': ['If you would like to contact, please email:', 'ntawil001@csbsju.edu'],
                                                   'urls': [{'url': '/', 'name': 'Home'}]
                                                   })