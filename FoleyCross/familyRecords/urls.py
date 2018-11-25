"""mySite URL Configuration

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
from django.urls import path, include
from . import views
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .models import Person, Family
from django.http import HttpResponseRedirect
from django.http import HttpRequest

urlpatterns = [path('', ListView.as_view(queryset=Family.objects.all().order_by("primary_contact_last_name", "primary_contact_first_name")[:25], template_name="familyRecords/families.html")),
               url(r'^updateFamily', views.updateFamily),
               url(r'^newPerson/', views.newPerson, name='newPerson'),
               path('newFamily/', views.newFamily, name='newFamily'),
               path('updatePerson/', views.updatePerson),
               path('newVisit/', views.newVisit),
               path('searchAction', views.searchFamily),
               path('search/', views.searchPage)
]

'''               path('editFamily/', views.editFamily),'''

''' url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Family,
                                          template_name='familyRecords/viewFamily.html')),'''