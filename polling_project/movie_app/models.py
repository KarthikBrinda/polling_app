from django.db import models

# Create your models here.
class MovieModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)


class ReviewModel(models.Model):
    name = models.CharField(max_length=100)
    vote = models.IntegerField()

