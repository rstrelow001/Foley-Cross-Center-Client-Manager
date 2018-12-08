from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms

from ..models import PersonForm, FamilyForm, Person, Family, VisitForm, SpecialProjectForm, Family
from ..controllers import SearchController, FamilyController


def specialProjectVisit(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SpecialProjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            id = request.GET.get('familyid', '')
            form.save()
            return HttpResponseRedirect('../updateFamily/?id=' + id)
# if a GET (or any other method) we'll create a blank form
    else:
        '''person = Person.objects.get(pk=1)'''
        id= request.GET.get('familyid', '')
        results = Family.objects.filter(pk=id)
        form = SpecialProjectForm(family=forms.ModelChoiceField(queryset=results.all(), initial=1))

    return render(request, 'familyRecords/specialProjectVisit.html', {'form': form})