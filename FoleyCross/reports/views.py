from django.http import HttpResponseRedirect
from django.shortcuts import render
from .render import Render
from django import forms
# from .models import report, report_form
from .controllers import ReportController


def run_report(request):
    # if this is a POST request we need to process the form data
    rc = ReportController()
    month = ''
    year = ''
    makepdf = ''
    full_month = ''
    new_this_month = ''
    new_to_cross = ''
    if request.method == 'GET':
        month = request.GET.get('Month', '')
        year = request.GET.get('Year', '')
        makepdf = request.GET.get('makepdf', '')
        if month == "-1":
            yearly_report_list_tuple = rc.run_yearly_report(year)
            yearly_report = yearly_report_list_tuple[0]
            yearly_new_this_month = yearly_report_list_tuple[1]
            yearly_new_to_cross = yearly_report_list_tuple[2]

            if makepdf == "1":
                params = {
                    'yearly_report_list': yearly_report_list_tuple,
                    'year': year
                }
                return Render.render('reports/generate_year.html', params)

            return render(request, 'reports/view_yearly_report.html', {'yearly_report': yearly_report,
                                                                       'yearly_new_this_month': yearly_new_this_month,
                                                                       'yearly_new_to_cross': yearly_new_to_cross,
                                                                       'year': year
                                                                       })
        # else, just report a single month
        monthly_report_tuple = rc.run_monthly_report(month, year)
        full_month = monthly_report_tuple[0]
        new_this_month = monthly_report_tuple[1]
        new_to_cross = monthly_report_tuple[2]
        if makepdf == "1" :
            params = {'monthly_report': monthly_report_tuple,
                                                        'month': month,
                                                        'year': year
                                                        }
            return Render.render('reports/generate_month.html', params)
    return render(request, 'reports/view_report.html', {'full_month': full_month,
                                                        'new_this_month': new_this_month,
                                                        'new_to_cross': new_to_cross,
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

def report_to_pdf(request):

    report = run_report(request)

    return Render.render(report)
