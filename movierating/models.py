from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=4, blank=True)

    def __str__(self):
        return f"{self.title} {self.year}"
