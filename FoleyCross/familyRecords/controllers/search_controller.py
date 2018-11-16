from ..models import PersonForm, FamilyForm, Person, Family


class SearchController():

    def searchByName(self, firstName, lastName):
        results = []
        if len(firstName) == 0 and len(lastName) == 0:
            return []
        elif len(firstName) == 0:
            results = Family.objects.filter(primary_contact_last_name__contains = lastName).order_by("primary_contact_last_name", "primary_contact_first_name")
        elif len(lastName) == 0:
            results = Family.objects.filter(primary_contact_first_name__contains = firstName).order_by("primary_contact_last_name", "primary_contact_first_name")
        else:
            results = Family.objects.filter(primary_contact_first_name__contains = firstName, primary_contact_last_name__contains = lastName).order_by("primary_contact_last_name", "primary_contact_first_name")
        return results

    def searchByID(self, family_id):

        results = Family.objects.filter(pk=family_id)
        return results