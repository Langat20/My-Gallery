from django.test import TestCase

# Create your tests here.
class CategoryTestCase(TestCase):
    '''method to create instance before each test is run '''
    def setUp(self):
        self.animals= Category(category = "animals")
        
    '''Testing  instance'''
    def test_instance(self):
        self.assertTrue(isinstance(self.animals,Category))
    
    def test_save_location(self):
        self.animals.save_category()
        category= Category.objects.all()
        self.assertTrue(len(category)>0)


class LocationTest(TestCase):
    '''method to create instance before each test is run '''

    def setUp(self):
        self.nairobi = Location(location='Nairobi')
    '''Testing  instance'''
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))

    def test_save_location(self):
        self.nairobi.save_location()
        location= Location.objects.all()
        self.assertTrue(len(location))

