from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import UserProfile

class ProfileForm1(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('FirstName', 'LastName', 'Email', 'Mobile', 'City',
                  'College', 'Degree', 'Major', 'StartDate', 'EndDate')

class ProfileForm2(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('accounting', 'consulting', 'creativeDesign', 'engineering', 'finance', 'legal', 'marketing',
                  'nursing', 'operations', 'research', 'SalesDevelopment', 'SoftwareEngg', 'engineering', 'roles',
                  'skills', 'experience', 'linkdin', 'github', 'weChat', 'lineID', 'dribble', 'portfolio',
                  'sharecom', 'opportunity')