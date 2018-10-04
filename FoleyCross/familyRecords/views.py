from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms

from .models import PersonForm, FamilyForm, Person, Family



def enterPerson(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            newForm = form.save(commit=False)
            newForm.save()
            return HttpResponseRedirect('../..')

    # if a GET (or any other method) we'll create a blank form
    else:
        '''person = Person.objects.get(pk=1)'''
        id= request.GET.get('id', '')
        results = Family.objects.filter(pk=id)
        form = PersonForm(family=forms.ModelChoiceField(queryset=results.all(), initial=1))

    return render(request, 'familyRecords/newPerson.html', {'form': form})



def editPerson(request):
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
            return HttpResponseRedirect('../'+request.GET.get('familyid', ''))

    # if a GET (or any other method) we'll create a blank form
    else:
        '''person = Person.objects.get(pk=1)'''
        id= request.GET.get('personid', '')
        results = Person.objects.get(pk=id)
        form = PersonForm(instance=results)

    return render(request, 'familyRecords/newPerson.html', {'form': form})








def enterFamily(request):
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

    return render(request, 'familyRecords/newFamily.html', {'form': form})
