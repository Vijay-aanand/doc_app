from django.db import models

# Create your models here.
class Profile(models.Model):
    phone_number=models.CharField(max_length=15,unique=True)
