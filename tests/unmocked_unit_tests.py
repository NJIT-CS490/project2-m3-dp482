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
        
    def test_Help(self):
        data = {"address": "!! help"}
        res = app.on_new_address(data)
        exp="Bot: Use different commands to explore (!! about, !! help, !! funtranslate)"
        self.assertEqual(exp, res)
    
    def test_Link(self):
        data = {"address":"(?P<url>https?://[^\s]+)"}
        click='url'
        res = app.on_new_address(data)
        exp = None
        self.assertEqual(exp, res)
    
    def test_Connect(self):                                     
        data = {'connect'}
        users_total.append("connect")
        userTotal=len(users_total) 
        res = app.on_connect()
        exp= ["connect"]
        self.assertEqual(exp, res)

    
if __name__ == '__main__':
    unittest.main()