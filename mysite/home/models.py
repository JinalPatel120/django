from django.db import models

# Create your models here.

Gender_choices= (('M','Male'),('F','Female'))

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(default=18)
    email=models.EmailField(null=True , blank= True)
    address= models.TextField(null= True , blank = True)
    gender=models.CharField(choices=Gender_choices,default='M')
    

class Car(models.Model):
    car_name= models.CharField(max_length=100)
    speed=models.IntegerField(default=50)
    
    def __str__(self) -> str:
        return self.car_name