from django.db import models

# Create your models here.


# delivery history table

class pickup(models.Model):
    date_time = models.DateTimeField(auto_now_add = True, editable=False)
    pickupAddress = models.CharField(max_length=350)
    pickupPersonName = models.CharField(max_length=100)
    pickupPersonNumber = models.CharField(max_length=15)
    deliveryAddress = models.CharField(max_length=350)
    pickupRequestByUserId = models.IntegerField(default='null', editable=False)
    pickupRequestByUserName = models.CharField(max_length=100, default='null')
    contactNumber = models.CharField(max_length=15, default='null')
    pickupDeliveryPersonId = models.IntegerField(default='null', editable=False)
    deliveryPersonName = models.CharField(max_length=100, default='null')
    deliveryPersonPhNo = models.CharField(max_length=15, default='null')
    deliveryPersonAadharNo = models.CharField(max_length=20, default='null')
    
    timeLimit = models.IntegerField()
    # will be kept in minutes
    
    status= models.BooleanField(default=0)
    # 0 means in way or not picked
    # 1 means delivered

# contact us table

class contact_us(models.Model):
    senderName=models.CharField(max_length=150)
    senderEmail=models.CharField(max_length=150)
    message=models.CharField(max_length=1000)
