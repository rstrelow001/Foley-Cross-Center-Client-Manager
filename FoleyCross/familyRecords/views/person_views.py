from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
import datetime

from ..models import PersonForm, FamilyForm, Person, Family, VisitForm, Visit
from ..controllers import SearchController, VisitController,FamilyController




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

    return render(request, 'familyRecords/personForm_update.html', {'form': form})
