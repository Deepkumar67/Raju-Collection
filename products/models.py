from django.db import models
from shops.models import Shop
from phonenumber_field.modelfields import PhoneNumberField

class Product(models.Model):
    title = models.CharField(max_length=350)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    price = models.IntegerField(default=1, blank=True)
    color = models.CharField(max_length=200, default="")
    main_image = models.ImageField(upload_to="main_image/%Y%m%d", default="")
    description = models.TextField(max_length=1000, blank=True)
    out_of_stock = models.BooleanField(default=False)
    size = models.CharField(max_length=200)
    is_new_arrival = models.BooleanField(default=False)
    image1 = models.ImageField(upload_to="image1/%Y%m%d", blank=True)
    image2 = models.ImageField(upload_to="image2/%Y%m%d", blank=True)

    def __str__(self):
        return self.title

class Advertisement(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, default="")
    advertisement_title = models.CharField(max_length=150, default="")
    adv_image1 = models.ImageField(upload_to="adv_image1/%Y%m%d", default="")
    adv_image2 = models.ImageField(upload_to="adv_image2/%Y%m%d", default="",blank=True)
    adv_image3 = models.ImageField(upload_to="adv_image3/%Y%m%d", default="",blank=True)


    def __str__(self):
        return self.advertisement_title


class Contact(models.Model):
    name = models.CharField(max_length=250, blank=False)
    phone = models.CharField(blank=False, max_length=100)
    email = models.EmailField(default="", blank=False)
    address = models.CharField(max_length=250,blank=False)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name

