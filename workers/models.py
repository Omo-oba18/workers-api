# workers/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Worker(models.Model):
    WORKER_SET= (
        ('carpenter', 'Carpenter'),
        ('tailor', 'Tailor'),
        ('driver', 'Driver'),
        ('housekeeper', 'Housekeeper'),
        ('plumber', 'Plumber'),
        ('cook', 'Cooker'),
    )
    name = models.CharField(max_length=100) #name field
    occupation = models.CharField(max_length=20, choices=WORKER_SET)  # Store the role/occupation here
    phone = models.CharField(max_length=15) #phone number
    address = models.CharField(max_length=200) #address
    

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    # Add any additional fields you want for the user here
    # For example, you can add profile picture, address, etc.
    role = models.CharField(max_length=255, blank=True)
    # Add other fields specific to your user model

    def __str__(self):
        return self.username

class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.user} rated {self.worker} with {self.rating}"
