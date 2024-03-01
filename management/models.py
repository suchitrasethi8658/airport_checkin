from django.db import models

# Create your models here.


class UploadModel(models.Model):
    departure = models.CharField(max_length=100)
    flight = models.CharField(max_length=100)
    airline = models.CharField(max_length=100)
    planetype=models.CharField(max_length=100)

