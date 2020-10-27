import unittest
import sys
from os.path import dirname, join
sys.path.insert(1, join(dirname(__file__), '../'))
import app
users_total=[]

class BotTest(unittest.TestCase):
    def test_About(self):
        data =	{"address": "!! about"}
        res = app.on_new_address(data)
        exp ="Bot: Welcome to Text+ "
        self.assertEqual(exp, res)
        
if __name__ == '__main__':
    
    unittest.main()