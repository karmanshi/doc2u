from django.db import models
from django.contrib.auth.models import User
from pandas import notnull
# Create your models here.

# delivery Person Table
class otherDetails(models.Model):
    user=models.OneToOneField(User, verbose_name=(""), on_delete=models.CASCADE)
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=15)
    aadharNo = models.CharField(max_length=20)
    drivingLicenseNo = models.CharField(max_length=20, default=False)
    address = models.CharField(max_length=300)
    profilePic = models.ImageField(upload_to='pics')
    rating = models.FloatField(editable=False, default=0)
    status=models.CharField(max_length=10, null=False)


