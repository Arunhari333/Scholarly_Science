from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import register, detail

class ProfileForm1(forms.ModelForm):
    class Meta:
        model = register
        fields = ('FirstName', 'LastName', 'Email', 'Mobile', 'City',
                  'College', 'Degree', 'Major', 'StartDate', 'EndDate')
        widgets = {
            'FirstName': forms.TextInput(attrs={'class': 'form-control', 'id': 'firstname'}),
            'LastName': forms.TextInput(attrs={'class': 'form-control', 'id': 'lastname'}),
            'Email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control', 'id': 'email'}),
            'Mobile': forms.TextInput(attrs={'type': 'tel', 'class': 'form-control', 'id': 'phone'}),
            'City': forms.TextInput(attrs={'class': 'form-control', 'id': 'city'}),
            'College': forms.TextInput(attrs={'class': 'form-control', 'id': 'college'}),
            'Degree': forms.TextInput(attrs={'class': 'form-control', 'id': 'degree'}),
            'Major': forms.TextInput(attrs={'class': 'form-control', 'id': 'majorCon'}),
            'StartDate': forms.TextInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'sdate'}),
            'EndDate': forms.TextInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'eDate'}),
        }

class ProfileForm2(forms.ModelForm):
    class Meta:
        model = detail
        fields = ('accounting', 'consulting', 'creativeDesign', 'engineering', 'finance', 'legal', 'marketing',
                  'nursing', 'operations', 'research', 'SalesDevelopment', 'SoftwareEngg', 'engineering', 'roles',
                  'skills', 'experience', 'linkdin', 'github', 'weChat', 'lineID', 'dribble', 'portfolio',
                  'sharecom', 'opportunity')