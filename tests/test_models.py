from django.test import TestCase
from restaurant.models import Menu
from restaurant.views import MenuItemView

from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse

client = APIClient()

class MenuTest(TestCase):

    def setUp(self):
        Menu.objects.create(title='Helado', price=80, inventory=100)

    def test_get_item(self):
        item = Menu.objects.get(title='Helado')
        items = Menu.objects.all()
        self.assertEqual(str(item), 'Helado : 80.00')
        self.assertEqual(item.inventory, 100)
        self.assertEqual(len(items), 1)

    def test_get_items(self):
        items = Menu.objects.all()
        self.assertEqual(len(items), 1)


class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(title='Helado', price=80, inventory=100)
        # client.credentials()

    def test_get_all(self):
        response = client.get(reverse('menu-view'))
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


