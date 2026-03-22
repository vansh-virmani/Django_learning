from django.db import models
# we write python class-> then orm writes sql auto matic and also creates a migration file (which contains only instructions)
# Create your models here.
class Profile(models.Model):
    name= models.CharField(max_length=70)
    email = models.EmailField(max_length=255)
    city  = models.CharField(max_length=70)
    roll  = models.IntegerField()
    # adding or creating new field add default="" keyword
    comment = models.CharField(max_length=70, default="Nothing") 

    def __str__(self):
       return self.name  ## if u want to return or see the rep as names in admin panel

