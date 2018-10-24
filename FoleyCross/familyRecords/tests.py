from django.test import TestCase, Client
from .models import Person, Family, PersonForm
from .controllers import SearchController

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


class FamilyTestCase(TestCase):
    def setUp(self):
        client = Client()
        Family.objects.create(primary_contact_first_name = "Ryan", primary_contact_last_name = "Strelow", date = '2018-10-20',
                              child_support = 0.0, fuel_assist = 0.0, general_assist = 0.0, mfip = 0.0, monthly_total = 0.0,
                              pension = 0.0, snap = 0.0, social_security = 0.0, ssi = 0.0, unemployment = 0.0, wages1 = 0.0,
                              wages2 = 0.0, wic = 0.0, workers_comp = 0.0
                              )

        Person.objects.create(first_name = "Ryan", last_name = "Strelow", birthday = '2015-10-20', race= 'White', gender = 'Male', status = 'Active', service = 'No', family_id=1)
        Person.objects.create(first_name="Marlyn", last_name="Strelow", birthday='2015-10-20', family_id=1)

    def test_get_updateFamily(self):
        response = self.client.get('/familyRecords/updateFamily/?id=1')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.resolver_match.func, newPerson)
        self.assertEqual(len(response.context['members']), 2)
        self.assertEqual(response.templates[0].name, "familyRecords/updateFamily.html")

        # = self.client.post('/familyRecords/updateFamily/?id=1')

    def test_get_updatePerson(self):
        response = self.client.get('/familyRecords/updatePerson/?personid=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].instance, Person.objects.get(pk=1))
        self.assertEqual(response.templates[0].name, "familyRecords/personForm.html")

        person = Person.objects.get(pk=1)
        #person.first_name = "bob"
        #r2= self.client.post('/familyRecords/updatePerson/?personid=1', data={'first_name' :person.first_name, 'last_name' : person.last_name,
        #                                                                 'birthday' :person.birthday, 'race': person.race, 'status': person.status, 'service': person.service,
        #                                                                      'gender': person.gender, 'family': person.family})

        #form = PersonForm({'first_name' :person.first_name, 'last_name' : person.last_name,
        #                                                                 'birthday' :person.birthday, 'race': person.race, 'status': person.status, 'service': person.service,
        #                                                                       'family': person.family})
        #self.assertTrue(form.is_valid)
        #self.assertEqual(r2.templates[0].name, "familyRecords/updateFamily.html")
        # = sresults = Person.objects.get(pk=id)
        #         form = PersonForm(instance=results)