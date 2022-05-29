from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)
    
    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()
    
    def update_location(self):
        self.update()
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    category_image = models.ImageField(upload_to='media/category')
    
    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()
    
    def update_category(self):
        self.update()
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural =("Categories")
        
    @classmethod
    def search_by_name(cls, search_term):
        results = cls.objects.filter(name__icontains=search_term)
        return results
        
    def __str__(self):
        return self.name
    
class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    image_file = models.FileField(upload_to='media/photos/')
    dated = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
    
    def update_image(self):
        self.update()
    
    def get_image_by_id(self, id):
        pass
    
    @classmethod
    def search_image(cls, category):
        results = cls.objects.filter(name__icontains=category)
        return results
    
    @classmethod
    def search_by_name(cls, search_term):
        results = cls.objects.filter(name__icontains=search_term)
        return results
    
    @classmethod
    def filter_by_location(cls, location):
        filtered_images = cls.objects.filter(location__icontains=location)
        return filtered_images
    
    class Meta:
        ordering = ('-dated',)
        
    def __str__(self):
        return self.name

