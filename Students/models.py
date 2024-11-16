from django.db import models
from Coures.models import Coures

# Create your models here.

class Student(models.Model) :

    users = models.CharField(max_length=20 , null=True)
    
    name = models.CharField(max_length=20 , null=True) 

    address = models.CharField(max_length=20 , null=True)

    moblie = models.CharField(max_length=10 , null=True)

    selected_coures = models.ForeignKey(Coures , on_delete= models.SET_NULL , null= True)

    placement = models.BooleanField(null=True)

    fees = models.IntegerField(default=0)

    gst = models.FloatField(default=0)

    total_fees = models.IntegerField(default=0)

    paid_fees = models.IntegerField(default=0)

    remaining_fees = models.IntegerField(default=0)

    pictuer = models.ImageField(null = True , upload_to = 'images/')

    def __str__(self):

        return self.name


class FeedBack(models.Model) :

    Title = models.CharField(max_length=200 , null=True)

    Body = models.TextField(null = True)
    
    slug = models.SlugField(null = True)

    def __str__(self) :
        return self.Title