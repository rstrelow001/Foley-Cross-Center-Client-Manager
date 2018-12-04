from django.shortcuts import render
import datetime

from ..models import PersonForm, FamilyForm, Family
from ..controllers import SearchController, FamilyController

def breadVisit(request):
    
    
    return render(request, 'familyRecords/breadVisit.html')