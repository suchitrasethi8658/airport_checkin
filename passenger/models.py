from django.db import models

# Create your models here.
from management.models import UploadModel


class RegisterModel(models.Model):
    firstname=models.CharField(max_length=300)
    lastname=models.CharField(max_length=200)
    userid=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    phoneno=models.BigIntegerField()
    email=models.EmailField(max_length=400)
    gender=models.CharField(max_length=200)
    passenger = models.CharField(max_length=100)
    country = models.CharField(max_length=100)



class PaymentModel(models.Model):
    passid = models.ForeignKey(RegisterModel, on_delete=models.CASCADE)
    manaid = models.ForeignKey(UploadModel, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=500)
    analysis = models.CharField(max_length=500)