import datetime
class FamilyController:

    def count_monthly_total(self, family):
        return (family.mfip + family.wic + family.general_assist + family.workers_comp + family.pension +
                family.social_security + family.ssi + family.fuel_assist + family.child_support +
                family.snap + family.unemployment + family.wages1 + family.wages2 )

    def has_visited(self, family):
        family.status = family.ACTIVE

    def has_not_visited(self, family):
        family.status = family.NON_ACTIVE