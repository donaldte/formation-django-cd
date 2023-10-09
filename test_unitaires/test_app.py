import unittest 
import app 


class TestCalcApp(unittest.TestCase):
    
    
    def test_add(self)  -> None:
        
        result = app.add(10, 5)
        
        self.assertEqual(result, 15)
        
        
    def test_sub(self) -> None:
        result = app.substract(10, 5)
        
        self.assertEqual(result, 5)
        
        
    def test_mul(self) -> None:
        result = app.mytiply(10, 5)
        
        self.assertEqual(result, 50)
        
    
    def test_div(self) -> None:
        result = app.divide(10, 5)
        
        self.assertEqual(result, 2)   
        
        with self.assertRaises(ValueError):
            app.divide(10, 0) 
        
          
        
        


if __name__ == '__main__':
    unittest.main()        