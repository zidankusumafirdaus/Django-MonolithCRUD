from django.test import TestCase
from .models import TBCars

class TBCarsModelTest(TestCase):

    def setUp(self):
        TBCars.objects.create(carname="Test Car", carbrand="Test Brand", carmodel="Test Model", carprice="10000")

    def test_car_creation(self):
        car = TBCars.objects.get(carname="Test Car")
        self.assertEqual(car.carbrand, "Test Brand")
        self.assertEqual(car.carmodel, "Test Model")
        self.assertEqual(car.carprice, "10000")

class TBCarsViewTest(TestCase):

    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cars/index.html')

    def test_createcar_view(self):
        response = self.client.get('/createcar/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cars/createcar.html')

    def test_readcar_view(self):
        response = self.client.get('/readcar/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cars/readcar.html')