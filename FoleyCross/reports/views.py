from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
# from .models import report, report_form
from .controllers import ReportController


def run_report(request):
    # if this is a POST request we need to process the form data
    rc = ReportController()
    month = ''
    year = ''
    if request.method == 'GET':
        month = request.GET.get('Month', '')
        year = request.GET.get('Year', '')
        print("The year from views is: {}".format(year))
        if month == "-1":
            yearly_report_list = rc.run_yearly_report(year)
            return render(request, 'reports/view_yearly_report.html', {'yearly_report_list': yearly_report_list,
                                                                       'year': year
                                                                       })
        # else, just report a single month
        monthly_report = rc.run_monthly_report(month, year)
    return render(request, 'reports/view_report.html', {'monthly_report': monthly_report,
                                                        'month': month,
                                                        'year': year
                                                        })


def new_report(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        pass

    # if a GET (or any other method) we'll create a blank form
    else:
        pass

    return render(request, 'reports/report_home.html')
