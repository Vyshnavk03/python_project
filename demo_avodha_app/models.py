from django.db import models

# Create your models here.
class shop(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    price=models.IntegerField()

