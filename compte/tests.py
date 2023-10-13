from django.test import RequestFactory, TestCase
from django.contrib.auth.models import Group
from unittest.mock import patch
from .custom_forms import PlanForm2
from django.test import Client
from .models import Plan
from django import forms

from django.urls import reverse

from .models import User

from .views import signup_view



class TestModelPlanTestCase(TestCase):
    
    """
    Description: this class helps to test a Plan model table
    """
    
    
    def setUp(self):
        
        self.data = {
            'name': 'premium',
            'description': 'premium',
            'price': 56
        }
        plan = Plan.objects.create(**self.data)
        
    
        
    def test_create_model(self):
        
        plan = Plan.objects.create(**self.data) 
        
        assert plan.name == 'premium'
        assert plan.description == 'premium'
        assert plan.price == 56
        
    def test_modify_model(self):
        
        plan = Plan.objects.get(name='premium')
        
        plan.name = 'Basic'
        plan.save()
        
        assert plan.name == 'Basic' 
        
    def test_list_model(self):
        
        plan_count = Plan.objects.count()
        
        self.assertEqual(plan_count, 1)
        
    
    # def test_delete_model(self):
        
        plan = Plan.objects.get(name='premium')
        
        plan.is_deleted = True
        plan.save()
        
        plan_count = Plan.objects.filter(is_deleted=False).count()
        
        self.assertEqual(plan_count, 0)
        


class TestPlanForm2TestCase(TestCase):
    
    """
    
    Name: test plan form2
    description: this class test helps to test a form
    
    """
    
    def setUp(self):
        
        self.data = {
            'name': 'premium',
            'description': 'premium',
            'price': 200
        }
        self.form = PlanForm2
        
    
    def test_valid_form(self):
        
        form = self.form(self.data) 
        
        self.assertTrue(form.is_valid())  
        

    def test_invalid_form_name(self):
        self.data['name'] = ''
        
        form = self.form(self.data)
        
        self.assertFalse(form.is_valid())
        
    
    def test_invalid_form_price(self):
        
        self.data['price'] = 'hello'  
        
        form = self.form(self.data)
        
        self.assertEqual(form.is_valid(), False) # equivalent to this:  assert form.is_valid() == False
        
        
        
        
    def test_clean_name(self):
        
        self.data['name'] = 'abc'
        
        form = self.form(self.data)
        
        self.assertRaises(forms.ValidationError)
        


class TestAccountViewsTestCasse(TestCase):
    
    
    def setUp(self) -> None:
        
        self.client = Client()
        self.factory = RequestFactory()
        
        self.signup_url = reverse('compte:signup')
        
        data = {
            'email': 'donaldtedom@gmail.com',
            'username': 'donald',
            'first_name': 'donald',
            'last_name': 'tedom',
        }
        
        
        user = User(**data)
        
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.set_password('12ldflasdlfjaksdf@3456')
        user.save()
        
        group = Group.objects.create(name='premium')
        
        user.groups.add(group)
        
    
    def test_get_signup_view(self):
        
        request = self.factory.get(reverse('compte:signup'))
        
        response = signup_view(request)
        
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('http://127.0.0.1:8000/en/compte/signup/') 
        
        self.assertEqual(response.status_code, 200)

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
        
    
    def test_get_login_view(self):
        print(reverse('compte:login'))
        response = self.client.get(reverse('compte:login')) 
        
        self.assertEqual(response.status_code, 200)
        
        self.assertTemplateUsed(response, 'login.html')
        
    
    
    def test_signup_post_view(self):
        
        data = {
            'email': 'engine@gmail.com',
            'username': 'test1',
            'first_name': 'donald',
            'last_name': 'tedom',
            'password1': '12ldflasdlfjaksdf@3456',
            'password2': '12ldflasdlfjaksdf@3456',
        } 
        
        # test signup here
        
        response = self.client.post(reverse('compte:signup'), data=data)
        
        user = User.objects.filter(username='test1')
        
        self.assertTrue(user.exists())
        
        self.assertTrue(user.first().check_password('12ldflasdlfjaksdf@3456'))
        
        
       
        self.assertEqual(response.status_code, 302)
        
        self.assertRedirects(response, reverse('compte:login'), 302)

        
     
    def test_login_post_view(self):
        
        login_url = reverse('compte:login')
        
        data = {
            'username': 'donald',
            'password': '12ldflasdlfjaksdf@3456'
        }
        
       # test login here 
        self.assertTrue(User.objects.filter(username='donald').exists())    
        response = self.client.post(reverse('compte:login'), data=data)
        
        # test assert here 
        
        self.assertEqual(response.status_code, 302)
        
    
        
        self.assertRedirects(response, reverse('dashboard:dashboard'), 302)
        #self.assertHTMLEqual(response, 'http://127.0.0.1:8000/en/dashboard/')
        
        
        
        
        
        
          
          
        
        
        
        
        
