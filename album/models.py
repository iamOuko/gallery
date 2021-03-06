from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=30)

class Category(models.Model):
    name = models.CharField(max_length=30)

class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    image = CloudinaryField('image')

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update()

    @classmethod
    def search_by_category(cls,search_term):
        category = cls.objects.filter(category__name__contains=search_term)
        return category

    @classmethod
    def search_by_location(cls,search_term):
        location = cls.objects.filter(location__name__contains=search_term)
        return location

