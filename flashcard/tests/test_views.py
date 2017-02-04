from django.test import TestCase
import unittest
from django.test import Client
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

class FlashcardTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        # self.client = APIClient()
        self.user = User.objects.create_user(username='koala', password='secret') 
        self.user.save() 
        # Logged In Client
        self.client = Client()

        # Logged In REST Client
        self.rest_client = APIClient()
        self.rest_client.login(username='koala', password='secret')
    def test_get_review_stack(self):
        # Issue a GET request.
        response = self.client.get('/review/lvl-2/2/get')
        self.assertEqual(response.status_code, 403)

    def test_get_review_stack_loggedin(self):
        response = self.rest_client.get('/review/lvl-2/2/get')
        self.assertEqual(response.status_code, 200)

# Create your tests here.
