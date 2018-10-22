from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms

from .models import PersonForm, FamilyForm, Person, Family, VisitForm, Visit
from .controllers import SearchController



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
        forms = []
        for person in members:
            newPerson = PersonForm(instance=person)
            forms.append(newPerson)

    return render(request, 'familyRecords/updateFamily.html', {'form': familyForm, 'family': family, 'members': members, 'visits': visits})



def newVisit(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = VisitForm(request.POST)
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
        form = VisitForm(family=forms.ModelChoiceField(queryset=results.all(), initial=1))

    return render(request, 'familyRecords/newVisit.html', {'form': form})


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
