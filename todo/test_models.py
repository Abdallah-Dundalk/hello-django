from django.test import TestCase
from .models import Item
# Create your tests here.


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

    def test_Item_returns_self_name(self):
        item = Item.objects.create(name='test item')
        self.assertEqual((str(item)), 'test item')

