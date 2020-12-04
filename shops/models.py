from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Shop(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField(default="",blank=True)
    phone = PhoneNumberField(blank=True)
    location = models.CharField(blank=True, max_length=100)
    

    def __str__(self):
        return self.name
