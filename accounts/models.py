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

    def __str__(self):
        return '%s' % (self.user)