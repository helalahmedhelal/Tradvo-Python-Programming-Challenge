from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    
    def test_create_user_with_correct_data(self):
        username='test'
        email='test@example.com'
        password='testpassword'
        user=get_user_model().objects.create_user(
            username=username,
            email=email,
            password=password
            
        )
        self.assertEqual(user.username,username)
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
        
    
    
            
   
            