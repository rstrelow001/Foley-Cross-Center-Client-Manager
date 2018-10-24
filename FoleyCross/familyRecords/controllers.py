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
            results = Family.objects.filter(primary_contact_last_name__contains = lastName).order_by("primary_contact_last_name", "primary_contact_first_name")
        elif len(lastName) == 0:
            results = Family.objects.filter(primary_contact_first_name__contains = firstName).order_by("primary_contact_last_name", "primary_contact_first_name")
        else:
            results = Family.objects.filter(primary_contact_first_name__contains = firstName, primary_contact_last_name__contains = lastName).order_by("primary_contact_last_name", "primary_contact_first_name")
        return results

    def searchByID(self, family_id):

        results = Family.objects.filter(pk=family_id)
        return results


class VisitController():

    #takes a family object and returns the number of active members in the family
    def countActiveMembers(self, family):
        return 0

    #takes a family object and counts the number of active members between the lower and upper bound
    def countAgeGroup(self, family, lowerBound, upperBound):
       return 0

    #takes a family object and returns the city for the family
    def getCity(self, family):
        return "Foley"

    #takes a family object and counts the number of active members for the speciified race
    def countNumberOfRace(self, family, race):
        return 0


class FamilyController:

    def count_monthly_total(self, family):
        return (family.mfip + family.wic + family.general_assist + family.workers_comp + family.pension +
                family.social_security + family.ssi + family.fuel_assist + family.child_support +
                family.snap + family.unemployment + family.wages1 + family.wages2 )

