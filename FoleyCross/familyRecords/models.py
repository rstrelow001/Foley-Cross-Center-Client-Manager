from django.db import models

from django.db import models
from django.forms import ModelForm
from django import forms

class Family(models.Model):
    FOLEY = "Foley"
    FORESTON  = "Foreston"
    GILMAN = "Gilman"
    CITY_CHOICES =  (
        (FOLEY, "Foley"),
        (FORESTON, "Foreston"),
        (GILMAN, "Gilman")
    )
    name = models.CharField(max_length=140)
    notes = models.TextField()
    date = models.DateTimeField()
    city = models.CharField(max_length = 50,
                            choices=CITY_CHOICES)
    zip = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=140)
    birthday = models.DateTimeField()
    family = models.ForeignKey(Family, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'birthday', 'family']

    def __init__(self, *args, **kwargs):
        person_details = kwargs.pop('family', None)
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'special'})
        self.fields['birthday'].widget.attrs.update(size='20')
        if person_details:
            self.fields['family'] = person_details



class FamilyForm(ModelForm):
    class Meta:
        model = Family
        fields = ['name', 'notes', 'date', 'city', 'zip']


