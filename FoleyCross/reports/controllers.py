from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from familyRecords.models import Visit
from .forms import Report
import datetime


class ReportController:
    '''
    def __init__(self, month=0, year=0, total_families=0, total_active_people=0, total_0_5=0, total_6_17=0,
                 combined_total_0_17=0, total_18_24=0, total_25_44=0, total_45_64=0, combined_total_18_64=0,
                 total_65_plus=0, pounds_of_food=0, total_race_white=0, total_race_black=0, total_race_asian=0,
                 total_race_hispanic=0, total_race_nativeAm=0, total_race_hawaiian=0, total_race_two_plus=0,
                 total_race_other=0, foley=0, foreston=0, gilman=0, milaca=0, oak_park=0, princeton=0,
                 rice=0, royalton=0, sartell=0, sauk_rapids=0, st_cloud=0):
        self.month = month
        self.year = year
        self.total_families = total_families
        self.total_active_people = total_active_people
        self.total_0_5 = total_0_5
        self.total_6_17 = total_6_17
        self.combined_total_0_17 = combined_total_0_17
        self.total_18_24 = total_18_24
        self.total_25_44 = total_25_44
        self.total_45_64 = total_45_64
        self.combined_total_18_64 = combined_total_18_64
        self.total_65_plus = total_65_plus
        self.pounds_of_food = pounds_of_food
        self.total_race_white = total_race_white
        self.total_race_black = total_race_black
        self.total_race_asian = total_race_asian
        self.total_race_hispanic = total_race_hispanic
        self.total_race_nativeAm = total_race_nativeAm
        self.total_race_hawaiian = total_race_hawaiian
        self.total_race_two_plus = total_race_two_plus
        self.total_race_other = total_race_other
        self.foley = foley
        self.foreston = foreston
        self.gilman = gilman
        self.milaca = milaca
        self.oak_park = oak_park
        self.princeton = princeton
        self.rice = rice
        self.royalton = royalton
        self.sartell = sartell
        self.sauk_rapids = sauk_rapids
        self.st_cloud = st_cloud
        '''

    def run_monthly_report(self, report_month, report_year):
        visits = Visit.objects.all()
        report = Report()
        for visit in visits:
            # get month and year from datetime object
            month = int(visit.get_month())
            year = int(visit.get_year())
            print("controller:Month: {}  Year: {}".format(month, year))
            if (month == int(report_month)) and (year == int(report_year)):
                report.total_families += 1
                if visit.total_active_people is not None:
                    report.total_active_people += visit.total_active_people

                if visit.total_0_5 is not None:
                    report.total_0_5 += visit.total_0_5

                if visit.total_6_17 is not None:
                    report.total_6_17 += visit.total_6_17
                report.combined_total_0_17 += (report.total_0_5 + report.total_6_17)

                if visit.total_18_24 is not None:
                    report.total_18_24 += visit.total_18_24

                if visit.total_25_44 is not None:
                    report.total_25_44 += visit.total_25_44

                if visit.total_45_64 is not None:
                    report.total_45_64 += visit.total_45_64
                report.combined_total_18_64 += (report.total_18_24 + report.total_25_44 + report.total_45_64)

                if visit.total_65_plus is not None:
                    report.total_65_plus += visit.total_65_plus

                if visit.pounds_of_food is not None:
                    report.pounds_of_food += visit.pounds_of_food

                if visit.total_race_white is not None:
                    report.total_race_white += visit.total_race_white

                if visit.total_race_black is not None:
                    report.total_race_black += visit.total_race_black

                if visit.total_race_asian is not None:
                    report.total_race_asian += visit.total_race_asian

                if visit.total_race_hispanic is not None:
                    report.total_race_hispanic += visit.total_race_hispanic

                if visit.total_race_nativeAm is not None:
                    report.total_race_nativeAm += visit.total_race_nativeAm

                if visit.total_race_hawaiian is not None:
                    report.total_race_hawaiian += visit.total_race_hawaiian

                if visit.total_race_two_plus is not None:
                    report.total_race_two_plus += visit.total_race_two_plus

                if visit.total_race_other is not None:
                    report.total_race_other += visit.total_race_other

                if visit.city is "Foley":
                    report.foley += visit.foley
                elif visit.city is "Foreston":
                    report.foreston += visit.foreston
                elif visit.city is "Gilman":
                    report.gilman += visit.gilman
                elif visit.city is "Milaca":
                    report.milaca += visit.milaca
                elif visit.city is "Oak Park":
                    report.oak_park += visit.oak_park
                elif visit.city is "Princeton":
                    report.princeton += visit.princeton
                elif visit.city is "Rice":
                    report.rice += visit.rice
                elif visit.city is "Royalton":
                    report.royalton += visit.royalton
                elif visit.city is "Sartell":
                    report.sartell += visit.sartell
                elif visit.city is "Sauk Rapids":
                    report.sauk_rapids += visit.sauk_rapids
                elif visit.city is "St Cloud":
                    report.st_cloud += visit.st_cloud
        return report

    def run_yearly_report(self, report_year):
        visits = Visit.objects.all()
        full_report = Report()
        report_list = []
        for m in range(1, 13):
            report = Report()
            for visit in visits:
                # get month and year from datetime object
                month = int(visit.get_month())
                year = int(visit.get_year())
                if (month == int(m)) and (year == int(report_year)):
                    report.total_families += 1
                    full_report.total_families += 1
                    if visit.total_active_people is not None:
                        report.total_active_people += visit.total_active_people
                        full_report.total_active_people += visit.total_active_people

                    if visit.total_0_5 is not None:
                        report.total_0_5 += visit.total_0_5
                        full_report.total_0_5 += visit.total_0_5

                    if visit.total_6_17 is not None:
                        report.total_6_17 += visit.total_6_17
                        full_report.total_6_17 += visit.total_6_17
                    report.combined_total_0_17 += (report.total_0_5 + report.total_6_17)
                    full_report.combined_total_0_17 += (report.total_0_5 + report.total_6_17)

                    if visit.total_18_24 is not None:
                        report.total_18_24 += visit.total_18_24
                        full_report.total_18_24 += visit.total_18_24

                    if visit.total_25_44 is not None:
                        report.total_25_44 += visit.total_25_44
                        full_report.total_25_44 += visit.total_25_44

                    if visit.total_45_64 is not None:
                        report.total_45_64 += visit.total_45_64
                        full_report.total_45_64 += visit.total_45_64
                    report.combined_total_18_64 += (report.total_18_24 + report.total_25_44 + report.total_45_64)
                    full_report.combined_total_18_64 += (report.total_18_24 + report.total_25_44 + report.total_45_64)

                    if visit.total_65_plus is not None:
                        report.total_65_plus += visit.total_65_plus
                        full_report.total_65_plus += visit.total_65_plus

                    if visit.pounds_of_food is not None:
                        report.pounds_of_food += visit.pounds_of_food
                        full_report.pounds_of_food += visit.pounds_of_food

                    if visit.total_race_white is not None:
                        report.total_race_white += visit.total_race_white
                        full_report.total_race_white += visit.total_race_white

                    if visit.total_race_black is not None:
                        report.total_race_black += visit.total_race_black
                        full_report.total_race_black += visit.total_race_black

                    if visit.total_race_asian is not None:
                        report.total_race_asian += visit.total_race_asian
                        full_report.total_race_asian += visit.total_race_asian

                    if visit.total_race_hispanic is not None:
                        report.total_race_hispanic += visit.total_race_hispanic
                        full_report.total_race_hispanic += visit.total_race_hispanic

                    if visit.total_race_nativeAm is not None:
                        report.total_race_nativeAm += visit.total_race_nativeAm
                        full_report.total_race_nativeAm += visit.total_race_nativeAm

                    if visit.total_race_hawaiian is not None:
                        report.total_race_hawaiian += visit.total_race_hawaiian
                        full_report.total_race_hawaiian += visit.total_race_hawaiian

                    if visit.total_race_two_plus is not None:
                        report.total_race_two_plus += visit.total_race_two_plus
                        full_report.total_race_two_plus += visit.total_race_two_plus

                    if visit.total_race_other is not None:
                        report.total_race_other += visit.total_race_other
                        full_report.total_race_other += visit.total_race_other

                    if visit.city is "Foley":
                        report.foley += visit.foley
                        full_report.foley += visit.foley
                    elif visit.city is "Foreston":
                        report.foreston += visit.foreston
                        full_report.foreston += visit.foreston
                    elif visit.city is "Gilman":
                        report.gilman += visit.gilman
                        full_report.gilman += visit.gilman
                    elif visit.city is "Milaca":
                        report.milaca += visit.milaca
                        full_report.milaca += visit.milaca
                    elif visit.city is "Oak Park":
                        report.oak_park += visit.oak_park
                        full_report.oak_park += visit.oak_park
                    elif visit.city is "Princeton":
                        report.princeton += visit.princeton
                        full_report.princeton += visit.princeton
                    elif visit.city is "Rice":
                        report.rice += visit.rice
                        full_report.rice += visit.rice
                    elif visit.city is "Royalton":
                        report.royalton += visit.royalton
                        full_report.royalton += visit.royalton
                    elif visit.city is "Sartell":
                        report.sartell += visit.sartell
                        full_report.sartell += visit.sartell
                    elif visit.city is "Sauk Rapids":
                        report.sauk_rapids += visit.sauk_rapids
                        full_report.sauk_rapids += visit.sauk_rapids
                    elif visit.city is "St Cloud":
                        report.st_cloud += visit.st_cloud
                        full_report.st_cloud += visit.st_cloud
            report_list.append(report)
        report_list.append(full_report)
        return report_list
