from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
# from .models import report, report_form
from .controllers import ReportController


def run_report(request):
    # if this is a POST request we need to process the form data
    rc = ReportController()
    if request.method == 'GET':
        month = request.GET.get('month', '')
        year = request.GET.get('year', '')
        rc.run_report(month, year)
    return render(request, 'reports/view_report.html', {'Total Families': rc.total_families})
                  # {'total_active_people': rc.total_active_people},
                  # {'total_0_5': rc.total_0_5})
                  # {'total_6_17': rc.total_6_17},
                  # )
                  # {'combined_total_0_17': rc.combined_total_0_17},
                  # {'total_18_24': rc.total_18_24},
                  # )


def new_report(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        pass

    # if a GET (or any other method) we'll create a blank form
    else:
        pass

    return render(request, 'reports/report_home.html')
