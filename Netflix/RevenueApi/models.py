from django.db import models

# Create your models here.
class Predictions(models.Model):
    
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    
    EMPLOYED_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    
    AREA_CHOICES = (
        ('Rural', 'Rural'),
        ('Semi_Urban', 'Semi_Urban'),
        ('Urban','Urban')
    )
    
    GRADUATED_CHOICES = (
        ('Graduated', 'Graduated'),
        ('Not_Graduated', 'Not_Graduated'),
    )
    
    MARRIED_CHOICES = (
        ('Single','Single'),
        ('Divorced','Divorced'),
        ('Married', 'Married'),
    )
    
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices = GENDER_CHOICES)
    employed = models.CharField(max_length=50, choices = EMPLOYED_CHOICES)
    area = models.CharField(max_length=50, choices = AREA_CHOICES)
    graduated = models.CharField(max_length=50, choices = GRADUATED_CHOICES)
    age = models.IntegerField(default=0)
    revenue = models.IntegerField(default=0)
    marital_status = models.CharField(max_length=50, choices = MARRIED_CHOICES)
    
    def __self__(self):
        return self.name
