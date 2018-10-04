from django.urls import path, include
from . import views
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .models import Visit
from django.http import HttpResponseRedirect
from django.http import HttpRequest

urlpatterns = [path('', ListView.as_view(queryset=Visit.objects.all().order_by("-date")[:25], template_name="visitRecords/visitRecords.html")),

               path('enterVisit/', views.enterVisit, name='enterVisit'),
]
