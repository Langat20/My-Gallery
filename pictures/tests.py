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

class TestGalore(TestCase):
    

    def setUp(self):

        '''create category and save'''
        self.animals= Category(category="animals")
        self.animals.save_category()

        '''create location and save '''
        self.santorini= Location(location="santorini")
        self.santorini.save_location()

        self.new_galore= galore(title="visit Santorini", description="in bikini", galore="Add image", location=self.nairobi, category= self.animals )
        self.new_galore.save_galore()

    def tearDown(self):
        Galore.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_delete_image(self):
        self.new_image= Galore(title="visit Santorini", description="in bikini", galore="Add image", location=self.nairobi, category= self.animals )
        self.new_image.save_image()
        self.new_image.delete_image()
        