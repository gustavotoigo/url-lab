from django.db import models

# Create your models here.

class Post(models.Model):
    productName = models.TextField()
    companyName = models.TextField()
