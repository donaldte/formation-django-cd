from django.test import TestCase
# import mock 
from django.test import RequestFactory

from unittest.mock import patch

from django.test import Client

from django.urls import reverse

from .models import User

from .views import signup_view


class TestViews(TestCase):
    
    
    def setUp(self) -> None:
        
        self.client = Client()
        
        self.signup_url = reverse('compte:signup')
        
        data = {
            'email': 'donaldtedom@gmail.com',
            'first_name': 'donald',
            'last_name': 'tedom',
        }
        
        user = User(**data)
        
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.set_password('12ldflasdlfjaksdf@3456')
        user.save()
        
    
    def test_signup_view(self):
        
        response = self.client.get('http://127.0.0.1:8000/en/compte/signup/')
        
        self.assertEquals(response.status_code, 200)
        
        self.assertTemplateUsed(response, 'signup.html')
        
        # self.assertTemplateUsed(response, 'base.html')
        
        # self.assertTemplateUsed(response, 'compte/base.html')
        
        # self.assertTemplateUsed(response, 'compte/includes/navbar.html')
        
        # self.assertTemplateUsed(response, 'compte/includes/footer.html')
        
        # self.assertTemplateUsed(response, 'compte/includes/head.html')
        
        # self.assertTemplateUsed(response, 'compte/includes/scripts.html')
        
        # self.assertTemplateUsed(response, 'compte/includes/sidebar.html')
        
        # self.assertTemplateUsed(response, 'compte/includes/topbar.html')
        
        # self.assertTemplateUsed(response, 'compte/includes/content.html')  
        
    
    def test_login_view(self):
        
        login_url = reverse('compte:login')
        
        response = self.client.get('http://127.0.0.1:8000/en/compte/login/') 
        
        self.assertEquals(response.status_code, 200)
        
        self.assertTemplateUsed(response, 'login.html')
        
    
    
    def test_signup_post_view(self):
        
        signup_url = reverse('compte:signup')
        
        data = {
            'email': 'engine@gmail.com',
            'username': 'test1',
            'first_name': 'donald',
            'last_name': 'tedom',
            'password1': '12ldflasdlfjaksdf@3456',
            'password2': '12ldflasdlfjaksdf@3456',
        } 
        
        # test signup here
        
        response = self.client.post('http://127.0.0.1:8000/en/compte/signup/', data=data)
        
        # test  here that the user is return in login view after creatin an account 
        
        #self.assertHTMLEqual(response, 'http://127.0.0.1:8000/en/compte/login/')
        self.assertEqual(response.status_code, 200)
        assert response.status_code == 200

        
        
        
    
     
    def test_login_post_view(self):
        
        login_url = reverse('compte:login')
        
        data = {
            'email': 'donald@gmail.com',
            'username': 'donald',
            'password': '12ldflasdlfjaksdf@3456'
        }
        
       # test login here 
            
        response = self.client.post('http://127.0.0.1:8000/en/compte/login/', data=data)
        
        # test assert here 
        
        self.assertEqual(response.status_code, 200)
        
        #self.assertHTMLEqual(response, 'http://127.0.0.1:8000/en/dashboard/')
        
        
        
        
        
        
          
          
        
        
        
        
        
