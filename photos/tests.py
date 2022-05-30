from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.
class LocationTestClass(TestCase):
    #set up method
    def setUp(self):
        '''
        This set up method runs before any instance is executed
        '''
        self.loc = Location(name='Zambia')
        
    # tesing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.loc,Location))
        
    #test save method
    def test_save_method(self):
        '''
        Test to check the save method execution
        '''
        self.loc.save_location()
        locs = Location.objects.all()
        self.assertTrue(len(locs)> 0)
        
class CategoryTestClass(TestCase):
    #set up method
    def setUp(self):
        '''
        This set up method runs before any instance is executed
        '''
        self.cat = Category(name='nature', description='blissful, serene, and peaceful', category_image='media/category/nature.jpg')
        
    # tesing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.cat,Category))
        
    #test save method
    def test_save_method(self):
        '''
        Test to check the save method execution
        '''
        self.cat.save_category()
        categoriess = Category.objects.all()
        self.assertTrue(len(categoriess)> 0)
        
        
class ImageTestClass(TestCase):
    def setUp(self):
        ''' 
        Creating a new location and saving it
        '''
        self.loc1 = Location(name = 'Arusha')
        self.loc1.save_location()
        
        ''' Creating a new category instance and saving it '''
        self.cat1 = Category(name='nature', description='blissful, serene, and peaceful', category_image='media/category/nature.jpg')
        self.cat1.save_category()
        
        ''' Creating a new Image instance '''
        self.new_image = Image(name="Test image ", description="This is a random test post", location = self.loc1, category = self.cat1, dated='May 29, 2022, 3:51 p.m.')
        self.new_image.save_image()
        
        
    def tearDown(self):
        '''
        This tearDown method does clean up after each test case has run.
        '''
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()
        
    def test_search_by_name(self):
        '''
        To test whether the search functionality is implemented properly
        '''
        searched = Image.search_by_name('Test image')
        self.assertTrue(len(searched) > 0)
        
    # def test_filter_by_location(self):
    #     filtered = Image.filter_by_location('Arusha')
    #     self.assertTrue(len(filtered) > 0)
                
        
#running tests
# python3 manage.py test news
# ./manage.py tests