from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime

from ..models import PersonForm, FamilyForm, Family
from ..controllers import SearchController, FamilyController


def newFamily(request):
    # if this is a POST request we need to process the form data
    error = ""
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FamilyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            temp_fam = Family.objects.filter(primary_contact_first_name = form.cleaned_data['primary_contact_first_name'], primary_contact_last_name = form.cleaned_data['primary_contact_last_name'])
            if (temp_fam.exists()):
                error = "There is already a primary contact with this name"
            else:
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

    return render(request, 'familyRecords/familyForm.html', {'form': form, 'error': error})


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
            visits = fam_updated.visit_set.all()
            visited = False
            for visit in visits:
                if int(visit.get_year()) == int(datetime.datetime.today().year):
                    visited = True
            if visited:
                fc.has_visited(fam_updated)
            else:
                fc.has_not_visited(fam_updated)
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
        error = ""

        visits = family.visit_set.all().order_by("date")
        visit_years = []
        for visit in visits:
                if datetime.date.today().month == visit.get_month():
                    error = 'This family has already visited this month'
                if not visit_years.__contains__(visit.get_year()):
                    visit_years.append(visit.get_year())
        visit_years.sort(reverse=True)


        special_projects = family.specialproject_set.all().order_by("date")
        special_projects_years = []
        for project in special_projects:
            if not special_projects_years.__contains__(project.get_year()):
                special_projects_years.append(project.get_year())
        special_projects_years.sort(reverse=True)


        bread_visits = family.breadvisit_set.all().order_by("date")
        bread_visit_years = []
        for visit in bread_visits:
            if not bread_visit_years.__contains__(visit.get_year()):
                bread_visit_years.append(visit.get_year())
        bread_visit_years.sort(reverse=True)

        forms = []
        for person in members:
            newPerson = PersonForm(instance=person)
            forms.append(newPerson)

    return render(request, 'familyRecords/updateFamily.html', {'form': familyForm, 'family': family, 'members': members, 'visits': visits, 'visit_years': visit_years,
                                                               'special_projects': special_projects, 'special_projects_years': special_projects_years,
                                                               'bread_visits': bread_visits, 'bread_visit_years': bread_visit_years, 'status': family.status, 'error': error})

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


    return render(request, 'familyRecords/familySearch.html', {'object_list': matches})

def searchPage(request):
    return render(request, 'familyRecords/familySearch.html')

