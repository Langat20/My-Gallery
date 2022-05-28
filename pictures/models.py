from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length =30)
    def __str__(self):
        return self.category
    def save_category(self):
        self.save()
    def delete_category(self):
        self.delete()
        

class Location(models.Model):
    location = models.CharField(max_length =30)
    def __str__(self):
        return self.location
    def save_location(self):
        self.save()
    def delete_location(self):
        self.delete()


class Galore(models.Model):
    title = models.CharField(max_length=60)
    image = CloudinaryField('image/', default="")
    description = models.TextField()
    location = models.ManyToManyField('location')
    category = models.ManyToManyField('category')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save_galleria(self):
        self.save()
    def delete_galleria(self):
        self.delete()
        