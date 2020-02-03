from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name=models.CharField(max_length=120)
    last_name=models.CharField(max_length=120)
    email=models.CharField(max_length=120)

    def __str__(self):
        return self.first_name



