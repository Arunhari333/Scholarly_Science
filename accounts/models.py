from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        models.CASCADE(),
        blank=True,
        null=True,
    )
    FirstName = models.CharField(max_length=100, default='')
    LastName = models.CharField(max_length=100, default='')
    Email = models.EmailField(blank=False)
    Mobile = models.IntegerField(default=0)
    City = models.CharField(max_length=100, default='')
    College = models.CharField(max_length=100, default='')
    Degree = models.CharField(max_length=100, default='')
    Major = models.CharField(max_length=100, default='')
    StartDate = models.DateField()
    EndDate = models.DateField()
 
    # deatail page
    accounting = models.BooleanField()
    consulting = models.BooleanField(default=True)
    creativeDesign = models.BooleanField(default=True)
    Engineering = models.BooleanField()
    finance = models.BooleanField()
    legal = models.BooleanField(default=True)
    marketing = models.BooleanField() 
    nursing = models.BooleanField()
    operations = models.BooleanField()
    research = models.BooleanField()
    SalesDevlopment = models.BooleanField()
    SoftwereEngg = models.BooleanField()
    
    # preffered roles
    PrefferRoles= models.CharField(max_length=100)
    # 10 skills
    skills=models.CharField(max_length=100)

    # radio filed

    proffessional= models.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    fresher=models.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    student=models.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())

    # on the web
    linkdin = models.CharField(max_length=30)
    github=models.CharField(max_length=30)
    weChat= models.CharField(max_length=30)
    lineID=models.CharField(max_length=30)
    Dribble=models.CharField(max_length=30)
    portfolio=models.CharField(max_length=30)
   
    # share profile
    Sharecom= models.BooleanField()
    # opportunity
    opportunity=models.BooleanField()
    
    def __str__(self):
        return '%s' % (self.user)
