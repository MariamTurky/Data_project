from distutils.command.upload import upload
from django.db import models
from datetime import datetime

# Create your models here.


class Device(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_active = models.BooleanField(default=True)
    purchasing_date = models.DateTimeField(default=datetime.now)
    serial_number = models.PositiveIntegerField()
    room_number = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Contact_US(models.Model):
    name = models.CharField(max_length=150)
    Email = models.EmailField(max_length=50)
    Mobil = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name
