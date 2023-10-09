import unittest 
from unittest.mock import patch
from unittest.mock import MagicMock

import joke


class TestJoke(unittest.TestCase):
    
    @patch('joke.get_joke')
    def test_len(self, mock_get_joke) -> None:
        
        mock_get_joke.return_value = 'abc'
        
        result = joke.len_joke()
        
        self.assertEqual(result, 3)
        
        

    def test_get_joke(self):
        
        with patch ('joke.requests') as mock_requests:
            
            mock_response = MagicMock()
            
            mock_response.status_code = 200 
            
            mock_response.json.return_value = {'value': 'abc'}
            
            mock_requests.get.return_value = mock_response
            
            self.assertEqual(joke.get_joke(), 'abc')
            
            mock_response.status_code = 400 
            
            mock_response.json.return_value = {'value': 'no joke'}
            
            mock_requests.get.return_value = mock_response
            self.assertEqual(joke.get_joke(), 'no joke')
            
            
if __name__ == '__main__':
    unittest.main()        