import unittest
import sys
from os.path import dirname, join
sys.path.insert(1, join(dirname(__file__), '../'))
import app
users_total=[]

class BotTest(unittest.TestCase):
    
    def test_Newuser(self):
        data = {"address":"data"}
        res = app.on_new_name(data)
        exp = None
        self.assertEqual(exp, res)
    
    def test_Link(self):
        data = {"address":"(?P<url>https?://[^\s]+)"}
        click='url'
        res = app.on_new_address(data)
        exp = None
        self.assertEqual(exp, res)
    
        
if __name__ == '__main__':
    unittest.main()
    