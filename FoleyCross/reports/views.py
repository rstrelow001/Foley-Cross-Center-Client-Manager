from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from .models import report, report_form


def run_report(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = report_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #id = request.GET.get('familyid', '')
            newForm = form.save(commit=False)
            newForm.save()
            return HttpResponseRedirect('../view_report/') #?id=' + id)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = report_form()

    return render(request, 'reports/view_report.html', {'form': form})
