from django.urls import path, include
from . import views
from django.conf.urls import url
from django.views.generic import ListView, DetailView
#from .models import Visit
#from familyRecords.models import Family
from django.http import HttpResponseRedirect
from django.http import HttpRequest

urlpatterns = [path('',views.new_report, name="new_report"),
               path('run_report', views.run_report, name="run_report")
]
