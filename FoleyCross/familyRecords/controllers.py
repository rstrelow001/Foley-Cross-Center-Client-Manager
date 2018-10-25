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
    def count_active_members(self, family):
        members= family.person_set.all()
        count = 0
        for member in members:
            if (member.status == member.ACTIVE):
                count += 1
        return count

    #takes a family object and counts the number of active members between the lower and upper bound
    def count_age_group(self, family, lowerBound, upperBound):
        members = family.person_set.all()
        count = 0
        for member in members:

            if (member.age() >= lowerBound and member.age() <= upperBound and member.status == member.ACTIVE):
                print(count)
                count += 1
        return count

    #takes a family object and returns the city for the family
    def get_city(self, family):
        return family.city

    #takes a family object and counts the number of active members for the speciified race
    def count_number_of_race(self, family, race):
        members = family.person_set.all()
        count = 0
        for member in members:
            if (member.race == race and member.status == member.ACTIVE):
                count += 1
        return count


class FamilyController:

    def count_monthly_total(self, family):
        return (family.mfip + family.wic + family.general_assist + family.workers_comp + family.pension +
                family.social_security + family.ssi + family.fuel_assist + family.child_support +
                family.snap + family.unemployment + family.wages1 + family.wages2 )

