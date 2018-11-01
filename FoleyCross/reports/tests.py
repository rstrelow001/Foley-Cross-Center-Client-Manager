from django.test import TestCase
from familyRecords.models import Person, Family
from familyRecords.controllers import SearchController, VisitController
from .forms import Report
from .controllers import ReportController

#
# class ReportTestCase(TestCase):
#     def setUp(self):
#         Family.objects.create()
