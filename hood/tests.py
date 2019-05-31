from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile,Post,Comment,Location,Category,Neighborhood,Company
# Create your tests here.
class UserProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = UserProfile(id=1,first_name='John',last_name='Doe',user = self.user,bio='test bio')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,UserProfile))

class PostTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post(id=1,title='Test',content='This is a test',user = self.user)

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

class CommentTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post(id=1,title='Test',content='This is a test',user = self.user)
        self.comment = Comment(id=1,post=self.post,user=self.user)

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comment))

class LocationTestClass(TestCase):
    #Setup method
    def setUp(self):
        self.location = Location(id=1,name='Test name')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

class CategoryTestClass(TestCase):
    #Setup method
    def setUp(self):
        self.category = Category(id=1,name='Test name')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

class NeighborhoodTestClass(TestCase):
    #Setup method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.location = Location(id=1,name='Test name')
        self.neighborhood = Neighborhood(id=1,name='Test name',location=self.location,admin=self.user,occupants=1)

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.neighborhood,Neighborhood))

    def test_create_neighborhood(self):
        self.location.save()
        self.neighborhood.create_neighborhood()
        self.assertTrue(len(Neighborhood.objects.all()) > 0)

    def test_delete_neighborhood(self):
        self.location.save()
        self.neighborhood.create_neighborhood()
        self.neighborhood = Neighborhood.objects.get(id=1)
        self.neighborhood.delete_neighborhood()
        self.assertTrue(len(Neighborhood.objects.all()) == 0)

    def test_find_neighborhood(self):
        self.location.save()
        self.neighborhood.create_neighborhood()
        self.searched_neighborhood = Neighborhood.find_neighborhood(1)
        self.assertTrue(self.searched_neighborhood == self.neighborhood)

    def test_update_neighborhood(self):
        self.location.save()
        self.neighborhood.create_neighborhood()
        self.neighborhood = Neighborhood.objects.get(id=1)
        self.neighborhood.name = 'Changed name'
        self.neighborhood.update_neighborhood()
        self.updated_neighborhood = Neighborhood.objects.get(id=1)
        self.assertEqual(self.updated_neighborhood.name,'Changed name')

    def test_update_occupants(self):
        self.location.save()
        self.neighborhood.create_neighborhood()
        self.neighborhood = Neighborhood.objects.get(id=1)
        self.neighborhood.update_occupants()
        self.updated_neighborhood = Neighborhood.objects.get(id=1)
        self.assertTrue(self.updated_neighborhood.occupants == 2)

class CompanyTestClass(TestCase):
    #Setup method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.location = Location(id=1,name='Test name')
        self.neighborhood = Neighborhood(id=1,name='Test name',location=self.location,admin=self.user,occupants=1)
        self.category = Category(id=1,name='Test name')
        self.company = Company(id=1,name='Test',user=self.user,description='Test description',neighborhood=self.neighborhood,category=self.category,email='test@test.com')
        self.location.save()
        self.neighborhood.save()
        self.category.save()
        self.company.save()


    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.company,Company))

    def test_create_company(self):
        self.company.create_company()
        self.assertTrue(len(Company.objects.all()) > 0)

    def test_delete_company(self):
        self.company.delete_company()
        self.assertTrue(len(Company.objects.all()) == 0)

    def test_find_company(self):
        self.company = Company.find_company(1)
        self.assertEqual(self.company.id, 1)

    def test_update_company(self):
        self.company = Company.find_company(1)
        self.company.name = 'Changed name'
        self.company.update_company()
        self.updated_company = Company.find_company(1)
        self.assertEqual(self.updated_company.name, 'Changed name')
