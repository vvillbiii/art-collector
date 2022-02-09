from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=300)
    image = models.CharField(max_length=500)
    period = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']