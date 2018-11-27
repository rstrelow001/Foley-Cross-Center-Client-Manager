from django.test import TestCase
from familyRecords.models import Person, Family, Visit
from familyRecords.controllers import SearchController, VisitController
from .forms import Report
from .controllers import ReportController


class MonthlyReportTestCase(TestCase):
    def setUp(self):
        Family.objects.create(primary_contact_first_name = "Test", primary_contact_last_name = "Family", date = '3000-01-01',
                              child_support=0.0, fuel_assist=0.0, general_assist=0.0, mfip=0.0, monthly_total=0.0,
                              pension = 0.0, snap = 0.0, social_security = 0.0, ssi = 0.0, unemployment = 0.0, wages1 = 0.0,
                              wages2 = 0.0, wic = 0.0, workers_comp = 0.0
                              )
        Person.objects.create(first_name="Ryan", last_name="Strelow", birthday='1998-04-01', family_id=1)
        Person.objects.create(first_name="Nicholas", last_name="Strelow", birthday='1998-04-01', family_id=1)

        family = Family.objects.get(pk=1)
        Visit.objects.create(family, date='3000-01-01', pounds_of_food=20, visit_notes='', total_active_people=2,
                             total_0_5=0, total_6_17=0, total_18_24=2, total_25_44=0, total_45_64=0, total_65_plus=0,
                             total_race_white=2, city=family.city)
        # ############################################### new family ####################################################
        Family.objects.create(primary_contact_first_name = "Test2", primary_contact_last_name = "Family2", date = '2999-09-09',
                              child_support=0.0, fuel_assist=0.0, general_assist=0.0, mfip=0.0, monthly_total=0.0,
                              pension = 0.0, snap = 0.0, social_security = 0.0, ssi = 0.0, unemployment = 0.0, wages1 = 0.0,
                              wages2 = 0.0, wic = 0.0, workers_comp = 0.0
                              )
        Person.objects.create(first_name="Bill", last_name="Nye", birthday='1998-04-01', family_id=2)
        Person.objects.create(first_name="Science", last_name="Guy", birthday='1998-04-01', family_id=2)

        family2 = Family.objects.get(pk=2)
        # new this month
        Visit.objects.create(family2, date='3000-01-01', pounds_of_food=10, visit_notes='', total_active_people=2,
                             total_0_5=0, total_6_17=0, total_18_24=2, total_25_44=0, total_45_64=0, total_65_plus=0,
                             total_race_white=2, city=family.city)

    def test_monthly_report_total_families(self):
        rc = ReportController()
        reports = rc.run_monthly_report(1, 3000)
        report = reports(0)
        self.assertEqual(2, report.total_families)

    def test_monthly_report_pounds_of_food(self):
        rc = ReportController()
        reports = rc.run_monthly_report(1, 3000)
        report = reports(0)
        self.assertEqual(30, report.pounds_of_food)

    def test_monthly_report_combined_total_18_64(self):
        rc = ReportController()
        reports = rc.run_monthly_report(1, 3000)
        report = reports(0)
        self.assertEqual(4, report.combined_total_18_64)

    def test_monthly_report_no_visits(self):
        rc = ReportController()
        reports = rc.run_monthly_report(4, 3000)
        report = reports(0)
        self.assertEqual(0, report.total_families)

    # new this month
    def test_monthly_report_new_this_month_total_families(self):
        rc = ReportController()
        reports = rc.run_monthly_report(1, 3000)
        report = reports(1)
        self.assertEqual(1, report.total_families)

    def test_monthly_new_this_month_pounds(self):
        rc = ReportController()
        reports = rc.run_monthly_report(1, 3000)
        report = reports(1)
        self.assertEqual(10, report.total_families)

    # new to cross
    def test_monthly_report_new_to_cross_total_families(self):
        rc = ReportController()
        reports = rc.run_monthly_report(1, 3000)
        report = reports(2)
        self.assertEqual(1, report.total_families)

    def test_monthly_new_to_cross_pounds(self):
        rc = ReportController()
        reports = rc.run_monthly_report(1, 3000)
        report = reports(2)
        self.assertEqual(20, report.total_families)


class YearlyReportTestCase(TestCase):
    def setUp(self):
        Family.objects.create(primary_contact_first_name = "Test", primary_contact_last_name = "Family", date = '3000-01-01',
                              child_support=0.0, fuel_assist=0.0, general_assist=0.0, mfip=0.0, monthly_total=0.0,
                              pension = 0.0, snap = 0.0, social_security = 0.0, ssi = 0.0, unemployment = 0.0, wages1 = 0.0,
                              wages2 = 0.0, wic = 0.0, workers_comp = 0.0
                              )
        Person.objects.create(first_name="Ryan", last_name="Strelow", birthday='1998-04-01', family_id=1)
        Person.objects.create(first_name="Nicholas", last_name="Strelow", birthday='1998-04-01', family_id=1)

        family = Family.objects.get(pk=1)
        Visit.objects.create(family, date='3000-01-01', pounds_of_food=20, visit_notes='', total_active_people=2,
                             total_0_5=0, total_6_17=0, total_18_24=2, total_25_44=0, total_45_64=0, total_65_plus=0,
                             total_race_white=2, city=family.city)
        Visit.objects.create(family, date='3000-05-01', pounds_of_food=20, visit_notes='', total_active_people=2,
                             total_0_5=0, total_6_17=0, total_18_24=2, total_25_44=0, total_45_64=0, total_65_plus=0,
                             total_race_white=2, city=family.city)
        # ############################################### new family ####################################################
        Family.objects.create(primary_contact_first_name = "Test2", primary_contact_last_name = "Family2", date = '2999-09-09',
                              child_support=0.0, fuel_assist=0.0, general_assist=0.0, mfip=0.0, monthly_total=0.0,
                              pension = 0.0, snap = 0.0, social_security = 0.0, ssi = 0.0, unemployment = 0.0, wages1 = 0.0,
                              wages2 = 0.0, wic = 0.0, workers_comp = 0.0
                              )
        Person.objects.create(first_name="Bill", last_name="Nye", birthday='1998-04-01', family_id=2)
        Person.objects.create(first_name="Science", last_name="Guy", birthday='1998-04-01', family_id=2)

        family2 = Family.objects.get(pk=2)
        # new this month
        Visit.objects.create(family2, date='3000-02-01', pounds_of_food=10, visit_notes='', total_active_people=2,
                             total_0_5=0, total_6_17=0, total_18_24=2, total_25_44=0, total_45_64=0, total_65_plus=0,
                             total_race_white=2, city=family.city)
        Visit.objects.create(family2, date='3000-03-01', pounds_of_food=10, visit_notes='', total_active_people=2,
                             total_0_5=0, total_6_17=0, total_18_24=2, total_25_44=0, total_45_64=0, total_65_plus=0,
                             total_race_white=2, city=family.city)

    def test_yearly_pounds(self):
        rc = ReportController()
        reports = rc.run_yearly_report(3000)
        report_list = reports(0)
        r = report_list(12)
        self.assertEqual(60, r.pounds_of_food)
