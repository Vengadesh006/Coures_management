from django.db import models

# Create your models here.

class Coures(models.Model) :
    
    coures = models.CharField(max_length= 20 , null= True)

    duration = models.CharField(max_length= 20 , null= True)

    fees = models.FloatField(default=0)

    gst = models.FloatField(default=0) 
    
    final_fees = models.FloatField(default=0)

    def __str__(self) :
        return self.coures

class Card(models.Model) :

    title = models.CharField(max_length=100 , null = True)

    content = models.CharField(max_length=100 , null=True)

    image = models.ImageField(null = True , upload_to = 'data/')

    def __str__(self) : 

        return self.title


    