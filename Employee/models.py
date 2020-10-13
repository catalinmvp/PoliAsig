from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AddEmployee(models.Model):
    Emp_id= models.AutoField(primary_key=True)
    Emp_Name= models.CharField(max_length=20)
    Emp_add= models.TextField(default='Employees address')
    Emp_payment= models.DecimalField(max_digits=1000,decimal_places=2)


class EmployeeLogin(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20,default='********')