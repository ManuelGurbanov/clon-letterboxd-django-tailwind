from django.db import models

class Movie(models.Model):
    imageUrl = models.URLField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    age = models.PositiveIntegerField()
    director = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.name