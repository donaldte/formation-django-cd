import requests 


class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        """Constructor"""
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        """Return the email"""
        return '{}.{}@company.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        """Return the fullname"""
        return '{} {}'.format(self.first, self.last)
    
    
    def apply_raise(self):
        """Apply the raise"""
        self.pay = int(self.pay * self.raise_amt)
        
    
    def monthly_schedule(self, month):
        
        response = requests.get(f'http://company.com/{self.last}/{month}')
        
        if response.ok:
            
            return response.text
        
        else:
            
            return 'Bad Response!'    