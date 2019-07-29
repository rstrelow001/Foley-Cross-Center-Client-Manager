from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from familyRecords.models import Visit
from .forms import Report
import datetime


class ReportController:
    field_list = ['total_active_people', 'total_0_5', 'total_6_17', 'total_18_24', 'total_25_44', 'total_45_64',
                  'total_65_plus', 'pounds_of_food', 'total_race_white', 'total_race_black', 'total_race_asian', 'total_race_hispanic',
                  'total_race_nativeAm', 'total_race_hawaiian', 'total_race_two_plus', 'total_race_other'
                  ]

    city_list = ['foley', 'foreston', 'gilman', 'milaca', 'oak_park', 'princeton', 'rice', 'royalton', 'sartell', 'sauk_rapids', 'st_cloud']

    def run_monthly_report(self, report_month, report_year):
        visits = Visit.objects.all()
        # a total of all of that category of visit data for that month
        report = Report()

        # subset where first visit of the year was this month (returning from last year)
        new_this_month = Report()

        # subset where first ever visit was this month (new family group)
        new_to_cross = Report()

        for visit in visits:
            if (int(visit.get_month()) == int(report_month)) and (int(visit.get_year()) == int(report_year)):
                self.monthly_helper_fields(report, visit)

                if self.is_new_to_cross(visit.family, report_month, report_year):
                    self.monthly_helper_fields(new_to_cross, visit)
                elif self.first_visit_of_year(visit.family, report_month, report_year):
                    self.monthly_helper_fields(new_this_month, visit)

        self.monthly_helper_combined(report)
        self.monthly_helper_combined(new_this_month)
        self.monthly_helper_combined(new_to_cross)
        return report, new_this_month, new_to_cross

    def is_new_to_cross(self, family, report_month, report_year):

        #print("Checking for A NEW FAMILY________________________________________________________________________")
        family_date = family.date
        family_month = family_date.month
        family_year = family_date.year

        visit_list = family.visit_set.all().order_by('date')

        print("first visit year: {}\treport year: {}".format(visit_list[0].get_year(), report_year))
        print("first visit month: {}\treport month: {}".format(visit_list[0].get_month(), report_month))
        first_visit_year = int(visit_list[0].get_year())
        first_visit_month = int(visit_list[0].get_month())

        if (first_visit_year == int(report_year)) and first_visit_month == int(report_month):
            #print("SUCCESS!")
            return True
        else:
            #print("failed.....")
            return False


        '''
        print("Checking for A NEW FAMILY________________________________________________________________________")
        family_date = family.date
        family_month = family_date.month
        family_year = family_date.year
        print("family year: {}\t report year: {}".format(family_year, report_year))
        if (int(family_month) == int(report_month)) and (int(family_year) == int(report_year)):
            print("New FAmily??????")
            return True
        return False
        '''

    def first_visit_of_year(self, family, report_month, report_year):
        #print("Checking for a FAMILY FIRST VISIT this year___________________")

        visit_list = family.visit_set.all().order_by("date")

        previously_visited = False
        for v in visit_list:
            if int(v.get_year()) == int(report_year)-1:
                #print("Previously visited!")
                previously_visited = True
            elif (int(v.get_year()) == int(report_year)):
                if (int(v.get_month() == int(report_month))) and previously_visited:
                    #print("First Visit of Year: {}".format(v.date))
                    return True
                else:
                    return False

        return False

    def monthly_helper_fields(self, report, visit):
        report.total_families += 1
        for f in self.field_list:
            attribute = getattr(visit, f)
            if attribute is not None:
                report.set_attribute(f, attribute)

        city = str(visit.city).lower()
        city = city.replace(' ', '_')
        if city in self.city_list:
            report.set_attribute(city, 1)

    def monthly_helper_combined(self, report):
        report.set_attribute('combined_total_0_17', (report.total_0_5 + report.total_6_17))
        report.set_attribute('combined_total_18_64', (report.total_18_24 + report.total_25_44 + report.total_45_64))

    def run_yearly_report(self, report_year):
        full_report = Report()
        full_new_this_month = Report()
        full_new_to_cross = Report()

        report_list = []
        new_this_month_list = []
        new_to_cross_list = []
        for m in range(1, 13):
            report_tuple = self.run_monthly_report(m, report_year)
            report = report_tuple[0]
            report_new_this_month = report_tuple[1]
            report_new_to_cross = report_tuple[2]

            report_list.append(report)
            new_this_month_list.append(report_new_this_month)
            new_to_cross_list.append(report_new_to_cross)

            full_report.set_attribute('total_families', report.total_families)
            full_new_this_month.set_attribute('total_families', report_new_this_month.total_families)
            full_new_to_cross.set_attribute('total_families', report_new_to_cross.total_families)
            for f in self.field_list:
                attribute = getattr(report, f)
                full_report.set_attribute(f, attribute)

                attribute = getattr(report_new_this_month, f)
                full_new_this_month.set_attribute(f, attribute)

                attribute = getattr(report_new_to_cross, f)
                full_new_to_cross.set_attribute(f, attribute)
            for c in self.city_list:
                city = getattr(report, c)
                full_report.set_attribute(c, city)

                city = getattr(report_new_this_month, c)
                full_new_this_month.set_attribute(c, city)

                city = getattr(report_new_to_cross, c)
                full_new_to_cross.set_attribute(c, city)

            full_report.set_attribute('combined_total_0_17', report.combined_total_0_17)
            full_report.set_attribute('combined_total_18_64', report.combined_total_18_64)

            full_new_this_month.set_attribute('combined_total_0_17', report_new_this_month.combined_total_0_17)
            full_new_this_month.set_attribute('combined_total_18_64', report_new_this_month.combined_total_18_64)

            full_new_to_cross.set_attribute('combined_total_0_17', report_new_to_cross.combined_total_0_17)
            full_new_to_cross.set_attribute('combined_total_18_64', report_new_to_cross.combined_total_18_64)

        report_list.append(full_report)
        new_this_month_list.append(full_new_this_month)
        new_to_cross_list.append(full_new_to_cross)
        return report_list, new_this_month_list, new_to_cross_list
