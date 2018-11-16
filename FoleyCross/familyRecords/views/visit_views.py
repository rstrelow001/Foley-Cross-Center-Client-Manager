from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
import datetime

from ..models import PersonForm, FamilyForm, Person, Family, VisitForm, Visit
from ..controllers import SearchController, VisitController,FamilyController


def newVisit(request):
    # if this is a POST request we need to process the form data
    error = ""
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = VisitForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            id = request.GET.get('familyid', '')
            family = Family.objects.get(pk=id)
            tempVisit = Visit.objects.filter(family=family, date=form.cleaned_data['date'])
            if (tempVisit.exists()):
                error = "There is already a visit for this date"

            else:
                form.save()

                vc = VisitController()
                visit = Visit.objects.get(family=family, date=form.cleaned_data['date'])
                visit.total_active_people = vc.count_active_members(family)
                visit.total_0_5 = vc.count_age_group(family, 0, 5)
                visit.total_6_17 = vc.count_age_group(family, 6, 17)
                visit.total_18_24 = vc.count_age_group(family, 18, 24)
                visit.total_25_44 = vc.count_age_group(family, 25, 44)
                visit.total_45_64 = vc.count_age_group(family, 45, 64)
                visit.total_65_plus = vc.count_age_group(family, 65, 130)
                visit.total_race_white = vc.count_number_of_race(family, visit.WHITE)
                visit.total_race_black = vc.count_number_of_race(family, visit.BLACK)
                visit.total_race_nativeAm = vc.count_number_of_race(family, visit.NATIVE_AMERICAN)
                visit.total_race_asian = vc.count_number_of_race(family, visit.ASIAN)
                visit.total_race_hispanic = vc.count_number_of_race(family, visit.HISPANIC)
                visit.total_race_hawaiian = vc.count_number_of_race(family, visit.NATIVE_HAWAIIAN)
                visit.total_race_two_plus = vc.count_number_of_race(family, visit.TWO_PLUS)
                visit.total_race_other = vc.count_number_of_race(family, visit.OTHER)
                visit.city = vc.get_city(family)
                form = VisitForm(instance=visit)
                new_form = form.save(commit=False)
                new_form.save()

                return HttpResponseRedirect('../updateFamily/?id=' + id)


    # if a GET (or any other method) we'll create a blank form
    else:
        '''person = Person.objects.get(pk=1)'''
        id= request.GET.get('familyid', '')
        results = Family.objects.filter(pk=id)
        form = VisitForm(family=forms.ModelChoiceField(queryset=results.all(), initial=1))

    return render(request, 'familyRecords/newVisit.html', {'form': form, 'error': error})
