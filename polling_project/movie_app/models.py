from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)


class Review(models.Model):
    name = models.CharField(max_length=200)
    vote = models.IntegerField()

class Visitors(models.Model):
    ip = models.CharField(max_length=50)

