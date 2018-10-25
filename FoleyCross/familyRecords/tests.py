from django.test import TestCase
from .models import Person, Family
from .controllers import SearchController, VisitController

class SearchTestCase(TestCase):
    def setUp(self):

        Family.objects.create(primary_contact_first_name = "Ryan", primary_contact_last_name = "Strelow", date = '2018-10-20',
                              child_support = 0.0, fuel_assist = 0.0, general_assist = 0.0, mfip = 0.0, monthly_total = 0.0,
                              pension = 0.0, snap = 0.0, social_security = 0.0, ssi = 0.0, unemployment = 0.0, wages1 = 0.0,
                              wages2 = 0.0, wic = 0.0, workers_comp = 0.0
                              )

        Person.objects.create(first_name = "Ryan", last_name = "Strelow", birthday = '2018-10-20', family_id=1)
        Person.objects.create(first_name="Marlyn", last_name="Strelow", birthday='2018-10-20', family_id=1)

        Family.objects.create(primary_contact_first_name = "Carl", primary_contact_last_name = "Johnson", date = '2018-10-20',
                              child_support = 0.0, fuel_assist = 0.0, general_assist = 0.0, mfip = 0.0, monthly_total = 0.0,
                              pension = 0.0, snap = 0.0, social_security = 0.0, ssi = 0.0, unemployment = 0.0, wages1 = 0.0,
                              wages2 = 0.0, wic = 0.0, workers_comp = 0.0
                              )

        Person.objects.create(first_name="Carl", last_name="Johnson", birthday = '2018-10-20', family_id=2)
        Person.objects.create(first_name="Bob", last_name="Johnson", birthday = '2018-10-20', family_id=2)
        Person.objects.create(first_name="Sam", last_name="Larson", birthday = '2018-10-20', family_id=2)

    def test_searchByName_with_first_name_and_last_name(self):
        sc = SearchController()
        family = Family.objects.get(pk = 1)
        matches = sc.searchByName("Ryan", "Strelow")
        self.assertEqual(family, matches[0])

    def test_searchByName_with_first_name_and_last_name_returns_nothing(self):
        sc = SearchController()
        matches = sc.searchByName("Adam", "Strelow")
        self.assertEquals(0, len(matches))

    def test_searchByName_with_first_name_only(self):
        sc = SearchController()
        family = Family.objects.get(pk=1)
        matches = sc.searchByName("Ryan", "")
        self.assertEqual(family, matches[0])

    def test_searchByName_with_first_name_only_returns_nothing(self):
        sc = SearchController()
        matches = sc.searchByName("Adam", "")
        self.assertEqual(0, len(matches))

    def test_searchByName_with_last_name_only(self):
        sc = SearchController()
        family = Family.objects.get(pk=1)
        matches = sc.searchByName("", "Strelow")
        self.assertEqual(family, matches[0])

    def test_searchByName_with_last_name_only_returns_nothing(self):
        sc = SearchController()
        matches = sc.searchByName("", "Konsors")
        self.assertEqual(0, len(matches))

    def test_searchByID(self):
        sc = SearchController()
        family = Family.objects.get(pk=1)
        matches = sc.searchByID(1)
        self.assertEqual(family, matches[0])

    def test_searchByID_returns_nothing(self):
        sc = SearchController()
        matches = sc.searchByID(0)
        self.assertEqual(0, len(matches))


class VisitControllerTestCase(TestCase):

    def setUp(self):

        Family.objects.create(primary_contact_first_name = "Ryan", primary_contact_last_name = "Strelow", date = '2018-10-20',
                              child_support = 0.0, fuel_assist = 0.0, general_assist = 0.0, mfip = 0.0, monthly_total = 0.0,
                              pension = 0.0, snap = 0.0, social_security = 0.0, ssi = 0.0, unemployment = 0.0, wages1 = 0.0,
                              wages2 = 0.0, wic = 0.0, workers_comp = 0.0
                              )

        Person.objects.create(first_name = "Ryan", last_name = "Strelow", birthday = '2010-10-20', family_id=1, status = "Active", race = "W")
        Person.objects.create(first_name="Marlyn", last_name="Strelow", birthday='2008-10-20', family_id=1, status = "Active")
        Person.objects.create(first_name="Sam", last_name="Larson", birthday = '1984-01-20', family_id=1, status = "Active", race = "B")


    def test_count_active_members_returns_2(self):
        vc = VisitController()
        count = vc.count_active_members(Family.objects.get(pk=1))
        self.assertEqual(count, 3)

    def test_count_number_of_race_returns_1(self):
        vc = VisitController()
        count = vc.count_number_of_race(Family.objects.get(pk=1), "W")
        self.assertEqual(count, 1)

    #for sure needs more test cases, same with others
    def test_count_age_group_returns_2(self):
        vc = VisitController()
        count = vc.count_age_group(Family.objects.get(pk=1), 6, 17)
        self.assertEqual(count, 2)