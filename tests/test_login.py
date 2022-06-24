import unittest
import requests
from utils import functions

class TestLogin(unittest.TestCase):

    def test_login_get(self):
        url = "http://localhost:5000/"
        req = requests.get(url)
        self.assertEqual(req.status_code, 200)
        self.assertTrue(len(str(req.content)) > 50)
        self.assertTrue("Welcome, please log in" in str(req.content))

    def test_login_post(self):
        url = "http://localhost:5000/"
        req = requests.post(url)
        self.assertEqual(req.status_code, 405)


if __name__ == '__main__':
    unittest.main()