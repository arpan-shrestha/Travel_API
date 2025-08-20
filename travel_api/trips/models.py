from django.db import models

# Create your models here.
class Trip(models.Model):
    url = models.CharField(max_length=500, unique=True, null=True, blank=True)
    title = models.CharField(max_length=200)
    duration = models.IntegerField(help_text="Number of Days")
    night = models.IntegerField(default=0,help_text="Number of Nights")
    difficulty = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class Activities(models.Model):
    url = models.CharField(max_length=500, unique=True, null=True, blank=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title