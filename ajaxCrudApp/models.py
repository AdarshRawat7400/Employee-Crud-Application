from django.db import models
from django.forms import CharField
# from phone_field import PhoneField


# Create your models here.
class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_email = models.EmailField(max_length=100)
    employee_location = models.CharField(max_length=100)
    employee_phone = models.CharField(max_length=15)

    def __str__(self):
        return self.employee_name
