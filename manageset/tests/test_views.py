from django.test import TestCase
# import unittest
from django.test import Client
from django.contrib.auth.models import User

class ManagesetsViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
