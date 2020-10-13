from __future__ import unicode_literals
from django.db import models
from Service.models import Service
# Create your models here.
class PhysicalCustomer(models.Model):
    Cust_id = models.AutoField(primary_key=True)
    Cust_name= models.CharField(max_length=20, default='insert a name')
    Cust_email=models.CharField(max_length=40,default='sth@upb.ro')
    Cust_feed= models.TextField(default='some feedback')

    def getname(self):
        return self.Cust_name




class Company(models.Model):

    Comp_regCode= models.DecimalField(max_digits=1000,decimal_places=2)
    Comp_name= models.CharField(max_length=20, default='insert a name')
    Comp_domain=models.CharField(max_length=40,default='EX: IT domain')
    Cust_address= models.TextField(default='some address')



