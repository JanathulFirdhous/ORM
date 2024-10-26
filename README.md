# Ex02 Django ORM Web Application
## Date: 26.10.2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](<Untitled document - Google Docs - Google Chrome 26-10-2024 15_02_20.png>)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py

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

admin.py
from django.contrib import admin
from.models import Bankloan,BankloanAdmin
admin.site.register(Bankloan,BankloanAdmin)

```


## OUTPUT

Include the screenshot of your admin page.
![alt text](<Select bankloan to change _ Django site admin - Google Chrome 26-10-2024 14_43_45.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
