class VisitController():

    #takes a family object and returns the number of active members in the family
    def count_active_members(self, family):
        members= family.person_set.all()
        count = 0
        for member in members:
            if (member.status == member.ACTIVE):
                count += 1
        return count

    #takes a family object and counts the number of active members between the lower and upper bound
    def count_age_group(self, family, lowerBound, upperBound):
        members = family.person_set.all()
        count = 0
        for member in members:

            if (member.age() >= lowerBound and member.age() <= upperBound and member.status == member.ACTIVE):
                print(count)
                count += 1
        return count

    #takes a family object and returns the city for the family
    def get_city(self, family):
        return family.city

    #takes a family object and counts the number of active members for the speciified race
    def count_number_of_race(self, family, race):
        members = family.person_set.all()
        count = 0
        for member in members:
            if (member.race == race and member.status == member.ACTIVE):
                count += 1
        return count
