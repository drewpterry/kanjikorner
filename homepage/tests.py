from django.test import TestCase
import unittest
from django.test import Client
from django.contrib.auth.models import User

class HomePageTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345') 
        self.user.save() 

    def test_get_index(self):
        # Issue a GET request.
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage/index.html')

    def test_get_index_loggedin(self):
        # Issue a GET request.
        login = self.client.login(username='testuser', password='12345')

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'manageset/dashboard.html')
