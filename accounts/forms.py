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
            'Mobile': forms.TextInput(attrs={'type': 'tel', 'class': 'form-control', 'id': 'phone',
                                             'placeholder': "081234 56789"}),
            'City': forms.TextInput(attrs={'class': 'form-control', 'id': 'city'}),
            'College': forms.TextInput(attrs={'class': 'form-control', 'id': 'college'}),
            'Degree': forms.TextInput(attrs={'class': 'form-control', 'id': 'degree'}),
            'Major': forms.TextInput(attrs={'class': 'form-control', 'id': 'majorCon'}),
            'StartDate': forms.TextInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'sdate'}),
            'EndDate': forms.TextInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'eDate'}),
        }

    class Media:
        js = ('accounts/js/intlTelInput.js', 'accounts/js/intlTelInput.min.js', 'accounts/js/utils.js')

class ProfileForm2(forms.ModelForm):
    class Meta:
        model = detail
        fields = ('accounting', 'consulting', 'creativeDesign', 'engineering', 'finance', 'legal', 'marketing',
                  'nursing', 'operations', 'research', 'SalesDevelopment', 'SoftwareEngg', 'roles',
                  'skills', 'professional', 'fresher', 'student', 'linkdin', 'github', 'weChat', 'lineID', 'dribble',
                  'portfolio', 'sharecom', 'opportunity')
        widgets = {
            'accounting': forms.CheckboxInput(attrs={'type': "checkbox", 'name': "tag1", 'id': "checkboxOne"}),
            'consulting': forms.CheckboxInput(attrs={'type': "checkbox", 'name': "tag2", 'id': "checkboxTwo"}),
            'creativeDesign': forms.CheckboxInput(attrs={'type': "checkbox", 'name': "tag3", 'id': "checkboxThree"}),
            'engineering': forms.CheckboxInput(attrs={'type': "checkbox", 'name': "tag4", 'id': "checkboxFour"}),
            'finance': forms.CheckboxInput(attrs={'type': "checkbox", 'name': "tag5", 'id': "checkboxFive"}),
            'legal': forms.CheckboxInput(attrs={'type': "checkbox", 'name': "tag6", 'id': "checkboxSix"}),
            'marketing': forms.CheckboxInput(attrs={'type': "checkbox", 'name': "tag7", 'id': "checkboxSeven"}),
            'nursing': forms.CheckboxInput(attrs={'type': "checkbox", 'name': "tag8", 'id': "checkboxEight"}),
            'operations': forms.CheckboxInput(attrs={'type': "checkbox", 'name': "tag9", 'id': "checkboxNine"}),
            'research': forms.CheckboxInput(attrs={'type': "checkbox", 'name': "tag10", 'id': "checkboxTen"}),
            'SalesDevelopment': forms.CheckboxInput(attrs={'type': "checkbox", 'name': "tag11", 'id': "checkboxEleven"}),
            'SoftwareEngg': forms.CheckboxInput(attrs={'type': 'checkbox', 'name': 'tag12', 'id': 'checkboxTwelve'}),
            'roles': forms.TextInput(attrs={'id': 'form-tags-1', 'name': 'tags-1'}),
            'skills': forms.TextInput(attrs={'id': "form-tags-3", 'name': "tags-3"}),
            'professional': forms.CheckboxInput(attrs={'type': "radio", 'id': "fresher", 'name': 'work-type'}),
            'fresher': forms.CheckboxInput(attrs={'type': "radio", 'id': "fresher", 'name': 'work-type'}),
            'student': forms.CheckboxInput(attrs={'type': "radio", 'id': "fresher", 'name': 'work-type'}),
            'linkdin': forms.TextInput(attrs={'type': "url", 'class': "social-input form-control", 'name': "linkedin",
                                              'placeholder': "LinkedIn URL.."}),
            'github': forms.TextInput(attrs={'type': "url", 'class': "social-input form-control", 'name': "github",
                                             'placeholder': "GitHub URL.."}),
            'weChat': forms.TextInput(attrs={'type': "url", 'class': "social-input form-control", 'name': "wechat",
                                             'placeholder': "WeChat ID.."}),
            'lineID': forms.TextInput(attrs={'type': "url", 'class': "social-input form-control", 'name': "line",
                                             'placeholder': "Line ID.."}),
            'dribble': forms.TextInput(attrs={'type': "url", 'class': "social-input form-control", 'name': "dribbble",
                                              'placeholder': "Dribbble URL.."}),
            'portfolio': forms.TextInput(attrs={'type': "url", 'class': "social-input form-control",
                                                'name': "portfolio", 'placeholder': "Portfolio URL.."}),
            'sharecom': forms.CheckboxInput(attrs={'type': "checkbox", 'name': "ShareCom"}),
            'opportunity': forms.CheckboxInput(attrs={'type': "checkbox", 'name': "opportunities"}),
        }
