from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.CharField(max_length=100,primary_key=True)
    profile_pic=models.ImageField(upload_to="profilepics",null=True)
    employee_name=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    salary=models.PositiveIntegerField()
    experience=models.PositiveIntegerField(null=True)
    def __str__(self):
        return self.employee_name