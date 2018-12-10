from django.contrib import admin
from familyRecords.models import Family, Person, Visit, SpecialProject, BreadVisit

admin.site.register(Family)
admin.site.register(Person)
admin.site.register(Visit)
admin.site.register(SpecialProject)
admin.site.register(BreadVisit)