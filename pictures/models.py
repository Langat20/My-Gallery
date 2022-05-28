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