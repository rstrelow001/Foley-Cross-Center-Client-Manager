from django.urls import path, include
from . import views
from django.conf.urls import url
from django.views.generic import ListView, DetailView
#from .models import Visit
from familyRecords.models import Family
from django.http import HttpResponseRedirect
from django.http import HttpRequest

urlpatterns = [path('', ListView.as_view(queryset=Family.objects.all().order_by("-date")[:25], template_name="reports/report_home.html")),
               path('run_report/', views.run_report)
]
