from django.db import models

# Create your models here.
class Flames(models.Model):
    name1 = models.CharField(max_length=30)
    name2 = models.CharField(max_length=30)
    result = models.CharField(max_length=30)
    
    date = models.DateField()

    def __str__(self):
        return self.name1

class Contact(models.Model):
    name = models.CharField(max_length=30)
    rating = models.CharField(max_length=1)
    feedback = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.name
    
