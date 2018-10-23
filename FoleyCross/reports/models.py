from django.db import models
from django.db import models
from django.forms import ModelForm
from django import forms


class report(models.Model):
    month = "month"
    year = "year"


class report_form(ModelForm):
    class Meta:
        model = report
        fields = ['month', 'year']



