from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from django.shortcuts import render

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=70, default="")
    profile = models.TextField(max_length=500, default="")
    loan_acc_no = models.IntegerField(default="")

    def __str__(self):
        return self.name

class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    zone_name = models.CharField(max_length=50)
    region_name = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=70, default="")
    branch_code = models.IntegerField(default="")

    def __str__(self):
        return self.branch_name

class Home(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    add_1 = models.CharField(max_length=50, default="")
    add_2 = models.CharField(max_length=50, default="")
    add_3 = models.CharField(max_length=70, default="")
    home_code = models.IntegerField(default="")
    landmark = models.CharField(max_length=70, default="")


class Office(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    add_1 = models.CharField(max_length=50, default="")
    add_2 = models.CharField(max_length=50, default="")
    add_3 = models.CharField(max_length=70, default="")
    off_code = models.IntegerField(default="")
    landmark = models.CharField(max_length=70, default="")



class Loan(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    agr_date = models.DateField()
    lrn = models.IntegerField(default="")
    tenor = models.DateField()
    adv_emi = models.IntegerField(default="")
    mob = models.IntegerField(default="")



class Excel(models.Model):
    file = models.FileField(upload_to='documents')