from django.db import models

from django.db import models
from django.forms import ModelForm
from django import forms
import datetime
from math import floor

class Family(models.Model):
    FOLEY = "Foley"
    FORESTON  = "Foreston"
    GILMAN = "Gilman"
    MILACA = "Milaca"
    OAK_PARK = "Oak Park"
    PRINCETON = "Princeton"
    RICE = "Rice"
    ROYALTON = "Royalton"
    SARTELL = "Sartell"
    SAUK_RAPIDS = "Sauk Rapids"
    ST_CLOUD = "St Cloud"

    CITY_CHOICES =  (
        (FOLEY, "Foley"),
        (FORESTON, "Foreston"),
        (GILMAN, "Gilman"),
        (MILACA, "Milaca"),
        (OAK_PARK, "Oak Park"),
        (PRINCETON, "Princeton"),
        (RICE, "Rice"),
        (ROYALTON, "Royalton"),
        (SARTELL, "Sartell"),
        (SAUK_RAPIDS, "Sauk Rapids"),
        (ST_CLOUD, "St Cloud")
    )

    YES = "Yes"
    NO = "No"
    YES_NO_CHOICES = (
        (YES, "Yes"),
        (NO, "No")
    )

    INSURANCE = "Insurance"
    ASSISTANCE = "Assistance"
    INSURANCE_ASSISTANCE_CHOICES = (
        (INSURANCE, "Insurance"),
        (ASSISTANCE, "Assistance")
    )

    ACTIVE = "Active"
    NON_ACTIVE = "Non-Active"
    ACTIVE_NONACTIVE_CHOICES = (
        (ACTIVE, "Active"),
        (NON_ACTIVE, "Non-Active")
    )

    primary_contact_first_name = models.CharField(max_length=140)
    primary_contact_last_name = models.CharField(max_length=140)
    proof_of_address = models.CharField(max_length = 10,
                            choices=YES_NO_CHOICES)
    notes = models.TextField(default = "NA")
    address = models.CharField(max_length = 100, default="")
    date = models.DateTimeField(default = datetime.date.today())
    city = models.CharField(max_length = 50,
                            choices=CITY_CHOICES)
    zip = models.PositiveIntegerField(null=True)
    phone = models.PositiveIntegerField(null=True)

    mfip = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    wic = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    general_assist = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    workers_comp = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pension = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    social_security = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ssi = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fuel_assist = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    child_support = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    snap = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    unemployment = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    wages1 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    wages2 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monthly_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    insurance_assistance = models.CharField(max_length = 50,
                            choices=INSURANCE_ASSISTANCE_CHOICES)

    status = models.CharField(max_length = 50, choices=ACTIVE_NONACTIVE_CHOICES, default="Non-Active")
    volunteer = models.CharField(max_length = 100, default="")

    def __str__(self):
        return self.primary_contact_last_name + ", " + self.primary_contact_first_name


class FamilyForm(ModelForm):
    class Meta:
        model = Family
        fields = ['primary_contact_first_name', 'primary_contact_last_name', 'proof_of_address', 'notes', 'address',
                  'date', 'city', 'zip', 'phone', 'mfip', 'wic',
                  'general_assist', 'workers_comp', 'pension', 'social_security',
                  'ssi', 'fuel_assist', 'child_support', 'snap', 'unemployment',
                  'wages1', 'wages2', 'monthly_total', 'insurance_assistance', 'status', 'volunteer']



class Person(models.Model):
    YES = "Yes"
    NO = "No"
    YES_NO_CHOICES = (
        (YES, "Yes"),
        (NO, "No")
    )

    ACTIVE = "Active"
    NON_ACTIVE = "Non-Active"
    ACTIVE_NONACTIVE_CHOICES = (
        (ACTIVE, "Active"),
        (NON_ACTIVE, "Non-Active")
    )

    W = "W"
    B = "B"
    NA = "NA"
    A = "A"
    H = "H"
    NH = "NH"
    T = "T"
    O = "O"
    RACE_CHOICES = (
        (W, "White"),
        (B, "Black or African American"),
        (NA, "Native American or Alaska Native"),
        (A, "Asian"),
        (NH, "Native Hawaiian or Other Pacific Islander"),
        (H, "Hispanic, Latino or Spanish Origin"),
        (T, "Two or More Races"),
        (O, "Other Race")
    )

    MALE = "Male"
    FEMALE = "Female"
    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female")
    )

    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    birthday = models.DateTimeField(default=datetime.datetime.now(datetime.timezone.utc))
    race = models.CharField(max_length=140, choices = RACE_CHOICES)
    gender = models.CharField(max_length=140, choices = GENDER_CHOICES)
    service = models.CharField(max_length=140, choices = YES_NO_CHOICES)
    status = models.CharField(max_length=140, choices = ACTIVE_NONACTIVE_CHOICES, default="Active")
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    volunteer = models.CharField(max_length=100, default="None")

    def __str__(self):
        return self.first_name + " " + self.last_name

    def age(self):
            difference = datetime.datetime.now(datetime.timezone.utc)-self.birthday
            return floor(difference.days/365)

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'birthday', 'race',
                  'gender', 'service', 'status', 'family', 'volunteer']
        age = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        person_details = kwargs.pop('family', None)
        super().__init__(*args, **kwargs)
        self.age = self.instance.age()
        if person_details:
            self.fields['family'] = person_details



class Visit(models.Model):
    WHITE = "W"
    BLACK = "B"
    NATIVE_AMERICAN = "NA"
    ASIAN = "A"
    HISPANIC = "H"
    NATIVE_HAWAIIAN = "NH"
    TWO_PLUS = "T"
    OTHER = "O"
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    date = models.DateTimeField(default = datetime.date.today())
    pounds_of_food = models.DecimalField(decimal_places=2, max_digits=10)
    visit_notes = models.TextField(default="NA")
    total_active_people = models.IntegerField(default=0)
    total_0_5 = models.IntegerField(default=0)
    total_6_17 = models.IntegerField(default=0)
    total_18_24 = models.IntegerField(default=0)
    total_25_44 = models.IntegerField(default=0)
    total_45_64 = models.IntegerField(default=0)
    total_65_plus = models.IntegerField(default=0)
    total_race_white = models.IntegerField(default=0)
    total_race_black = models.IntegerField(default=0)
    total_race_asian = models.IntegerField(default=0)
    total_race_hispanic = models.IntegerField(default=0)
    total_race_nativeAm = models.IntegerField(default=0)
    total_race_hawaiian = models.IntegerField(default=0)
    total_race_two_plus = models.IntegerField(default=0)
    total_race_other = models.IntegerField(default=0)
    city = models.CharField(max_length=140, default= "Foley")
    volunteer = models.CharField(max_length=100, default="None")

    def get_year(self):
        return self.date.year

    def get_month(self):
        return self.date.month

    def __str__(self):
        return str(self.date.month) + "-" + str(self.date.day) + "-" + str(self.date.year)


class VisitForm(ModelForm):
    class Meta:
        model = Visit
        fields = ['family', 'date', 'pounds_of_food', 'visit_notes', 'total_active_people',
                  'total_0_5', 'total_6_17', 'total_18_24', 'total_25_44', 'total_45_64', 'total_65_plus',
                  'total_race_white', 'total_race_black', 'total_race_asian', 'total_race_hispanic',
                  'total_race_nativeAm', 'total_race_hawaiian', 'total_race_two_plus', 'total_race_other',
                  'city', 'volunteer']

    def __init__(self, *args, **kwargs):
        person_details = kwargs.pop('family', None)
        super().__init__(*args, **kwargs)
        # self.visited = self.instance.not_this_month()
        if person_details:
            self.fields['family'] = person_details

class BreadVisit(models.Model):
    pounds_of_bread = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.date.today())
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    visit_notes = models.TextField(default="NA")

    def get_year(self):
        return self.date.year

    def get_month(self):
        return self.date.month

    def __str__(self):
        return str(self.date)

class BreadVisitForm(ModelForm):
    class Meta:
        model= BreadVisit
        fields = ['pounds_of_bread', 'date', 'family', 'visit_notes']
        def __init__(self, *args, **kwargs):
            person_details = kwargs.pop('family', None)
            super().__init__(*args, **kwargs)
            # self.visited = self.instance.not_this_month()
            if person_details:
                self.fields['family'] = person_details

    def get_year(self):
        return self.date.year

    def get_month(self):
        return self.date.month

    def __str__(self):
        return str(self.date.month) + "-" + str(self.date.day) + "-" + str(self.date.year)


class SpecialProject(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.date.today())
    HOLIDAYFOOD1 = "Holiday Food 1"
    HOLIDAYFOOD2 = "Holiday Food 2"
    SCHOOLSUPPLIES = "School Supplies"
    GIVINGTREE = "Giving Tree"
    OTHER = "Other"
    PROJECT_CHOICES = (
        (HOLIDAYFOOD1, "Holiday Food 1"),
        (HOLIDAYFOOD2, "Holiday Food 2"),
        (SCHOOLSUPPLIES, "School Supplies"),
        (GIVINGTREE, "Giving Tree"),
        (OTHER, "Other")
    )
    project = models.CharField(max_length=140, choices=PROJECT_CHOICES)
    project_notes = models.TextField(default="NA")
    volunteer = models.CharField(max_length=100, default="None")

    def get_year(self):
        return self.date.year

    def get_month(self):
        return self.date.month

    def __str__(self):
        return self.project + ":  " + str(self.date.month) + "-" + str(self.date.day) + "-" + str(self.date.year)


class SpecialProjectForm(ModelForm):
    class Meta:
        model = SpecialProject
        fields = ['family', 'date', 'project', 'project_notes', 'volunteer']
        def _init_(self, *args, **kwargs):
            person_details = kwargs.pop('family', None)
            super().__init__(*args, **kwargs)
            if person_details:
                self.fields['family'] = person_details

