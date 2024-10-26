from django.db import models
from django.contrib import admin
class Bankloan(models.Model):
         Name=models.CharField(max_length=10)
         Accountno=models.IntegerField(primary_key="accountno")
         Aadharno=models.IntegerField()
         DoB=models.DateField()
         Email=models.EmailField()
         Branch=models.CharField(max_length=21)
class BankloanAdmin(admin.ModelAdmin):
         list_display=('Name','Accountno','Aadharno','DoB','Email','Branch')
