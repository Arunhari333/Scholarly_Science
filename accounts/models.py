from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class register(models.Model):
    user = models.OneToOneField(
        User,
        models.CASCADE,
        blank=True,
        null=True,
    )
    FirstName = models.CharField(max_length=100, default='')
    LastName = models.CharField(max_length=100, default='')
    Email = models.EmailField(blank=False)
    Mobile = models.IntegerField()
    City = models.CharField(max_length=100, default='')
    College = models.CharField(max_length=100, default='')
    Degree = models.CharField(max_length=100, default='')
    Major = models.CharField(max_length=100, default='')
    StartDate = models.DateField()
    EndDate = models.DateField()

    def __str__(self):
        return '%s' % (self.user)

    # deatail page

class detail(models.Model):
    user = models.OneToOneField(
        User,
        models.CASCADE,
        blank=True,
        null=True,
    )
    accounting = models.BooleanField()
    consulting = models.BooleanField(default=True)
    creativeDesign = models.BooleanField(default=True)
    engineering = models.BooleanField()
    finance = models.BooleanField()
    legal = models.BooleanField(default=True)
    marketing = models.BooleanField()
    nursing = models.BooleanField()
    operations = models.BooleanField()
    research = models.BooleanField()
    SalesDevelopment = models.BooleanField()
    SoftwareEngg = models.BooleanField()

    # preffered roles
    roles = models.CharField(max_length=100)
    # 10 skills
    skills = models.CharField(max_length=100)

    # radio field)
    CHOICES = ((1, 'I am a working professional'), (2, 'I am a fresher'), (3, 'I am a student'))
    experience = models.IntegerField(choices=CHOICES, default=0)

    # on the web
    linkdin = models.CharField(max_length=30, blank=True, null=True)
    github = models.CharField(max_length=30, blank=True, null=True)
    weChat = models.CharField(max_length=30, blank=True, null=True)
    lineID = models.CharField(max_length=30, blank=True, null=True)
    dribble = models.CharField(max_length=30, blank=True, null=True)
    portfolio = models.CharField(max_length=30, blank=True, null=True)

    # share profile
    sharecom = models.BooleanField()
    # opportunity
    opportunity = models.BooleanField()

    def __str__(self):
        return '%s' % (self.user)
