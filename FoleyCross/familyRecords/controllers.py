from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms

from .models import PersonForm, FamilyForm, Person, Family


class SearchController():

    def searchByName(self, firstName, lastName):
        results = []
        if len(firstName) == 0 and len(lastName) == 0:
            return []
        elif len(firstName) == 0:
            results = Family.objects.filter(primary_contact_last_name__contains = lastName)
        elif len(lastName) == 0:
            results = Family.objects.filter(primary_contact_first_name__contains = firstName)
        else:
            results = Family.objects.filter(primary_contact_first_name__contains = firstName, primary_contact_last_name__contains = lastName)
        return results
