
import unittest
from unittest.mock import patch

from employee import Employee 


class TestEmployee(unittest.TestCase):
    
    
    @classmethod
    def setUpClass(cls):
        print('setUpClass')
    
    
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
        
    
    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('John', 'Smith', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)
        
    def tearDown(self):
        print('tearDown\n')    
    
    
    def test_email(self):
        
        self.assertEqual(self.emp_1.email, 'John.Smith@company.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@company.com')
        
    
    def test_fullname(self):
       
        self.assertEqual(self.emp_1.fullname, 'John Smith')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith') 
        
        
    def test_apply_raise(self):
       
        
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)  
        
        
    def test_monthly_schedule(self):
        
        
        with patch('employee.requests.get') as mocked_get:
            
            mocked_get.return_value.ok = True    
            
            mocked_get.return_value.text = 'Success'
            
            schedule = self.emp_1.monthly_schedule('May')
            
            mocked_get.assert_called_with('http://company.com/Smith/May')
            
            self.assertEqual(schedule, 'Success')
            
            mocked_get.return_value.ok = False    
            
            mocked_get.return_value.text = 'Bad Response!'
            
            schedule = self.emp_2.monthly_schedule('June')
            
            mocked_get.assert_called_with('http://company.com/Smith/June')
            
            self.assertEqual(schedule, 'Bad Response!')
            
            
        
           

                
if __name__ == '__main__':
    unittest.main()
    
            