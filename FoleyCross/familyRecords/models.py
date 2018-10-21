from django.db import models

from django.db import models
from django.forms import ModelForm
from django import forms

class Family(models.Model):
    FOLEY = "Foley"
    FORESTON  = "Foreston"
    GILMAN = "Gilman"
    MILACA = "Milaca"
    OAK = "Oak"
    PARK = "Park"
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
        (OAK,  "Oak"),
        (PARK, "Park"),
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

    primary_contact_first_name = models.CharField(max_length=140)
    primary_contact_last_name = models.CharField(max_length=140)
    proof_of_address = models.CharField(max_length = 10,
                            choices=YES_NO_CHOICES)
    notes = models.TextField()
    address = models.CharField(max_length = 100, default="")
    date = models.DateTimeField()
    city = models.CharField(max_length = 50,
                            choices=CITY_CHOICES)
    zip = models.PositiveIntegerField(null=True)
    phone = models.PositiveIntegerField(null=True)

    mfip = models.DecimalField(max_digits=10, decimal_places=2)
    wic = models.DecimalField(max_digits=10, decimal_places=2)
    general_assist = models.DecimalField(max_digits=10, decimal_places=2)
    workers_comp = models.DecimalField(max_digits=10, decimal_places=2)
    pension = models.DecimalField(max_digits=10, decimal_places=2)
    social_security = models.DecimalField(max_digits=10, decimal_places=2)
    ssi = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_assist = models.DecimalField(max_digits=10, decimal_places=2)
    child_support = models.DecimalField(max_digits=10, decimal_places=2)
    snap = models.DecimalField(max_digits=10, decimal_places=2)
    unemployment = models.DecimalField(max_digits=10, decimal_places=2)
    wages1 = models.DecimalField(max_digits=10, decimal_places=2)
    wages2 = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_total = models.DecimalField(max_digits=10, decimal_places=2)

    insurance_assistance = models.CharField(max_length = 50,
                            choices=INSURANCE_ASSISTANCE_CHOICES)

    def __str__(self):
        return self.primary_contact_last_name + ", " + self.primary_contact_first_name


class FamilyForm(ModelForm):
    class Meta:
        model = Family
        fields = ['primary_contact_first_name', 'primary_contact_last_name', 'proof_of_address', 'notes', 'address',
                  'date', 'city', 'zip', 'phone', 'mfip', 'wic',
                  'general_assist', 'workers_comp', 'pension', 'social_security',
                  'ssi', 'fuel_assist', 'child_support', 'snap', 'unemployment',
                  'wages1', 'wages2', 'monthly_total', 'insurance_assistance']



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
    birthday = models.DateTimeField()
    race = models.CharField(max_length=140, choices = RACE_CHOICES)
    gender = models.CharField(max_length=140, choices = GENDER_CHOICES)
    service = models.CharField(max_length=140, choices = YES_NO_CHOICES)
    status = models.CharField(max_length=140, choices = ACTIVE_NONACTIVE_CHOICES)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name + " " + self.last_name

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'birthday', 'race',
                  'gender', 'service', 'status', 'family']

    def __init__(self, *args, **kwargs):
        person_details = kwargs.pop('family', None)
        super().__init__(*args, **kwargs)
        self.fields['birthday'].widget.attrs.update(size='20')
        if person_details:
            self.fields['family'] = person_details



