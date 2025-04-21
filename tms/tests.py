from django.test import TestCase
from django.utils.timezone import now, timedelta
import random
import unittest
from tms.models import ProjectModel, TaskModel
from django.contrib.auth.models import User
from tms.serializers import ProjectSerializer, TaskSerializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
import subprocess

class TestUsers(TestCase):
    
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.all()

        self.assertGreaterThan(len(self.user), 0, "No users found in the database.")
        self.assertTrue(self.user[0].is_superuser, "The first user is not a superuser.")

    def test_user_creation(self):
        for user in self.user:
            if not user.is_superuser:
                assertTrue(user.is_superuser, f"User {user.username} is not a superuser.")
                # check token file path
                filePath = f"~/workspace/log/tokens/{user.username}.json"
                assertTrue(os.path.exists(filePath), f"Token file for {user.username} does not exist.")

                data = JSONParser().parse(filePath)
                self.assertIn('refresh', data, f"Refresh token not found for {user.username}.")
                self.assertIn('access', data, f"Access token not found for {user.username}.")
                savedToken = data['token']
                self.assertEqual(savedToken, user.token, f"Token mismatch for {user.username}.")

if __name__ == "__main__":
    unittest.main()
