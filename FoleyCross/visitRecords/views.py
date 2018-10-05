from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from .models import VisitForm, Visit
from familyRecords.models import Family

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
