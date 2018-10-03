from django.db import models
from django.db import models
from django.forms import ModelForm
from django import forms
from familyRecords.models import Family
import datetime


class Visit(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    date = models.DateTimeField()
    pounds_of_food = models.DecimalField(decimal_places=2, max_digits=10)
    visit_notes = models.TextField()

    def __str__(self):
        return self.date


class VisitForm(ModelForm):
    class Meta:
        model = Visit
        fields = ['family', 'date', 'pounds_of_food', 'visit_notes']
