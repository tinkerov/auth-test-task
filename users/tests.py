from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthTests(APITestCase):
    def setUp(self):
        self.register_url = reverse('auth_register')
        self.login_url = reverse('token_obtain_pair')
        self.user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword123",
            "password_confirm": "testpassword123",
            "first_name": "",
            "last_name": ""
        }

    def test_registration(self):
        """Тест регистрации пользователя"""
        response = self.client.post(self.register_url, self.user_data)
        
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_login(self):
        """Тест получения JWT токена"""

        data = self.user_data.copy()
        data.pop('password_confirm', None)
        
        
        User.objects.create_user(**data)
        
        login_data = {
            "email": "test@example.com",
            "password": "testpassword123"
        }
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)