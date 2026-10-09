import re

from django import forms

from .models import Pet


class PetForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('', 'Select gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Pet
        # date_registered is auto_now_add, so it is not editable in a form
        fields = [
            'pet_name',
            'species',
            'breed',
            'age',
            'gender',
            'owner_name',
            'owner_contact_number',
            'health_vaccination_notes',
        ]
        labels = {
            'pet_name': 'Pet Name',
            'species': 'Species',
            'breed': 'Breed',
            'age': 'Age (years)',
            'gender': 'Gender',
            'owner_name': 'Owner Name',
            'owner_contact_number': 'Owner Contact Number',
            'health_vaccination_notes': 'Health / Vaccination Notes',
        }
        widgets = {
            'pet_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Max'}),
            'species': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Dog'}),
            'breed': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Labrador'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control'}),
            'owner_contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '09XXXXXXXXX'}),
            'health_vaccination_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 0:
            raise forms.ValidationError("Age cannot be negative.")
        if age > 50:
            raise forms.ValidationError("Please enter a realistic age.")
        return age

    def clean_owner_contact_number(self):
        number = self.cleaned_data['owner_contact_number'].strip()
        if not re.fullmatch(r'[0-9+\-\s()]{7,20}', number):
            raise forms.ValidationError("Enter a valid contact number.")
        return number