from django.db import models

class Scooter(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)      
    price = models.IntegerField()                    

    def __str__(self):
        return f'{self.title}'
