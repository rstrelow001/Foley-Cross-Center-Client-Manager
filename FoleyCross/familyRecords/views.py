from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
import datetime

from .models import PersonForm, FamilyForm, Person, Family, VisitForm, Visit
from .controllers import SearchController, VisitController,FamilyController



def newPerson(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            id = request.GET.get('familyid', '')
            newForm = form.save(commit=False)
            newForm.save()
            return HttpResponseRedirect('../updateFamily/?id=' + id)

    # if a GET (or any other method) we'll create a blank form
    else:
        '''person = Person.objects.get(pk=1)'''
        id= request.GET.get('familyid', '')
        results = Family.objects.filter(pk=id)
        form = PersonForm(family=forms.ModelChoiceField(queryset=results.all(), initial=1))

    return render(request, 'familyRecords/personForm.html', {'form': form})



def updatePerson(request):
    # if this is a POST request we need to process the form data

    if request.method == 'POST':
        personid = request.GET.get('personid', '')
        #
        # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            person = Person.objects.get(pk=personid)
            form = PersonForm(request.POST, instance= person)
            form.save()
            #return to view the family this person is in
            return HttpResponseRedirect('../updateFamily/?id='+request.GET.get('familyid', ''))

    # if a GET (or any other method) we'll create a blank form
    else:
        #grab the current values stored for this person
        id= request.GET.get('personid', '')
        results = Person.objects.get(pk=id)
        form = PersonForm(instance=results)

    return render(request, 'familyRecords/personForm.html', {'form': form})



def newFamily(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FamilyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            newForm = form.save(commit=False)
            newForm.save()


            fam_updated = Family.objects.get(primary_contact_first_name = form.cleaned_data['primary_contact_first_name'], primary_contact_last_name = form.cleaned_data['primary_contact_last_name'])
            fc = FamilyController()
            fam_updated.monthly_total = fc.count_monthly_total(fam_updated)
            form = FamilyForm(instance=fam_updated)
            newForm = form.save(commit=False)
            newForm.save()
            return HttpResponseRedirect('..')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FamilyForm()

    return render(request, 'familyRecords/familyForm.html', {'form': form})



def updateFamily(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FamilyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            family_id = request.GET.get('id', '')
            family = Family.objects.get(pk=family_id)
            form = FamilyForm(request.POST, instance=family)
            form.save()

            fam_updated = Family.objects.get(pk=family_id)
            fc = FamilyController()
            fam_updated.monthly_total = fc.count_monthly_total(fam_updated)
            form = FamilyForm(instance=fam_updated)
            newForm = form.save(commit=False)
            newForm.save()
            return HttpResponseRedirect('..')

    # if a GET (or any other method) we'll create a blank form
    else:
        family_id = request.GET.get('id', '')
        family=Family.objects.get(pk=family_id)
        familyForm = FamilyForm(instance=family)
        members= family.person_set.all()
        visits = family.visit_set.all()

        for visit in visits:
                if datetime.date.today().month == visit.get_month():
                    error = 'This family has already visited this month'

        forms = []
        for person in members:
            newPerson = PersonForm(instance=person)
            forms.append(newPerson)

    return render(request, 'familyRecords/updateFamily.html', {'form': familyForm, 'family': family, 'members': members, 'visits': visits})



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


def searchFamily(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':

        sc = SearchController()
        first_name = request.GET.get('first_name', '')
        last_name = request.GET.get('last_name','')
        family_id = request.GET.get('family_id')

        if (len(first_name) == 0 and len(last_name) == 0 and len(family_id) == 0):
            matches = Family.objects.all().order_by("primary_contact_last_name", "primary_contact_first_name")
        elif (len(family_id) == 0):
            matches = sc.searchByName(first_name, last_name)
        else:
            matches = sc.searchByID(int(family_id))

    else:
        matches = Family.objects.all().order_by("primary_contact_last_name", "primary_contact_first_name")


    return render(request, 'familyRecords/families.html', {'object_list': matches})



'''
def enterVisit(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = VisitForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            newForm = form.save(commit=False)
            newForm.save()
            return HttpResponseRedirect('..')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = VisitForm()

    return render(request, 'visitRecords/newVisit.html', {'form': form})


def visitsByFamily(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = VisitForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            newForm = form.save(commit=False)
            newForm.save()
            return HttpResponseRedirect('..')

    # if a GET (or any other method) we'll create a blank form
    else:
        family_id = request.GET.get('id', '')
        family_name = request.GET.get('f_name', '')
        family = Family.objects.get(pk=family_id)
        visits = family.visit_set.all()
    return render(request, 'visitRecords/visitsByFamily.html', {'visits': visits, 'f_name': family_name})


def visitSummary(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = VisitForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            newForm = form.save(commit=False)
            newForm.save()
            return HttpResponseRedirect('..')

    # if a GET (or any other method) we'll create a blank form
    else:

        notes = request.GET.get('n', '')

    return render(request, 'visitRecords/visitSummary.html', {'notes': notes})
'''