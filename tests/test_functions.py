from app import app
from utils.functions import *
import unittest


class TestValidFilds(unittest.TestCase):
    def test_valid_cedula(self):
        with app.test_client() as test_client:
            print( valid_cedula( "V-12345678" ) )
            self.assertTrue( valid_cedula( "V-12345678" ) )
            self.assertFalse( valid_cedula( "V12345678" ) )
            self.assertFalse( valid_cedula( "V-123456789" ) )
            self.assertFalse( valid_cedula( "V-1234567" ) )
            self.assertFalse( valid_cedula( "V - 123456789") )
        