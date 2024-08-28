from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountViewsTest(TestCase):
    def setUp(self):
        # Create a test user for login and profile tests
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )
        
        
    def test_register_view_get(self):
        """Test GET request to the register view."""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/registration/register.html')
        
        
    def test_register_view_post_valid(self):
        """Test POST request to register view with valid data."""
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())
        self.assertRedirects(response, reverse('interface'))    
        
        
    def test_register_view_post_invalid(self):
        """Test POST request to register view with invalid data."""
        data = {
            'username': '',
            'email': 'newuser@example.com',
            'password1': 'password123',
            'password2': 'password1234',  # passwords don't match
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='').exists())
          
        
    
    def test_login_view_get(self):
        """Test GET request to the login view."""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')
    
    def test_login_view_post_valid(self):
        """Test POST request to login view with valid credentials."""
        data = {
            'username': 'testuser',
            'password': 'password123',
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('interface'))
    
    def test_login_view_post_invalid(self):
        """Test POST request to login view with invalid credentials."""
        data = {
            'username': 'wronguser',
            'password': 'wrongpassword',
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 200)
        
    
    def test_logout_view(self):
        """Test logout functionality."""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('interface'))
    
    def test_profile_view_get(self):
        """Test GET request to the profile view."""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/profile/profile.html')
    
    def test_profile_view_post_valid(self):
        """Test POST request to profile view with valid data."""
        self.client.login(username='testuser', password='password123')
        data = {
            'username': 'updateduser',
            'email': 'updateduser@example.com',
        }
        response = self.client.post(reverse('profile'), data)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')
        self.assertEqual(self.user.email, 'updateduser@example.com')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('interface'))
    
    def test_profile_view_post_invalid(self):
        """Test POST request to profile view with invalid data."""
        self.client.login(username='testuser', password='password123')
        data = {
            'username': '',  # Invalid username
            'email': 'invalidemail.com',  # Invalid email
        }
        response = self.client.post(reverse('profile'), data)
        self.assertEqual(response.status_code, 200)
             