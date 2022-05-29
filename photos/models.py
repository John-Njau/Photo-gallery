from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)
    
    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    category_image = models.ImageField(upload_to='media/category')
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural =("Categories")
        
    def __str__(self):
        return self.name
    
class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    image_file = models.FileField(upload_to='media/photos/')
    dated = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    url_link = models.URLField(max_length=200)
    
    class Meta:
        ordering = ('dated',)
        
    def __str__(self):
        return self.name

