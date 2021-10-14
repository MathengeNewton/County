from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class StudentAccount(models.Model):
    membershipNumber = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200,unique=True, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200, null=False, blank=False)
    id_no = models.CharField(max_length=200, null=True, blank=True)
    d_o_b = models.DateField(null=True, blank=True)
    constituency = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    
