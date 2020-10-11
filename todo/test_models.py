from django.test import TestCase
from .models import Items


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Items.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

    def test_models_to_return_str(self):
        item = Items.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')