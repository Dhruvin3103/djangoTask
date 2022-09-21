from django.db import models

# Create your models here.
class product(models.Model):
    title = models.CharField(max_length=100)
    descr = models.TextField()
    price = models.TextField()
    summary = models.TextField(default='this is cool ok !')

