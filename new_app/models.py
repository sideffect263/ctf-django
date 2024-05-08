from django.db import models

# Create your models here.

class movies(models.Model):
    name = models.CharField(max_length=5000,default="")
    rating = models.FloatField(default=0)
    
    
    def __str__(self):
        return self.name
    
        


