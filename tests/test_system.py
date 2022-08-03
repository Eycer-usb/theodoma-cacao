import unittest
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from app import create_test
from utils.db import db
from utils.functions import *

class TestSystem(unittest.TestCase):

    def setUp(self):
        self.app = create_test()
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()


    #--------------------------UTILS FUNCTIONS----------------------------#
    def test_valid_name(self):
        self.assertFalse( valid_name("Hola09") )
        self.assertTrue( valid_name("QWERTYUIOPASDFGHJKLZXVCBBCX..asd.,asdasd") )
    
    def test_valid_username1(self):
        self.assertTrue(valid_username("Username_with_underscores", True))
        self.assertFalse(valid_username("username-with-scores", True))

    def test_valid_username2(self):
        self.assertFalse(valid_username("asd", True))
        self.assertFalse(valid_username("ATooLongUsernameMostNotBeAllowedAtAll", True))
        self.assertFalse(valid_username("   no    empty   espaces  ", True))

    def test_valid_username3(self):
        self.assertTrue( valid_username("eycer", True) )

    def test_valid_email(self):
        self.assertTrue( valid_email( "email@domin.extention" ) )
        self.assertFalse( valid_email( "email.domin.extention" ) )
        self.assertFalse( valid_email("randomwords") )
        self.assertFalse( valid_email( "   email@domin.extention   " ) )

    def test_valid_gender(self):
        self.assertTrue( valid_gender('Masculino') )
        self.assertTrue( valid_gender('Femenino') )
        self.assertTrue( valid_gender('Otro') )

    def test_invalid_gender(self):
        self.assertFalse( valid_gender('Helicoptero') )
        self.assertFalse( valid_gender('No Binario') )

    def test_valid_passwd(self):
        self.assertTrue( valid_password("SuperSecret@omg.wtf") )

    def test_valid_date(self):
        self.assertTrue( valid_date( "12/01/2022" ) )
        self.assertTrue( valid_date( "12-11-2022" ) )
        self.assertTrue( valid_date( "10.02.2022" ) )
        self.assertTrue( valid_date( "2022/12/01" ) )
        self.assertTrue( valid_date( "2022-04-31" ) )
        self.assertTrue( valid_date( "2022.05.20" ) )
        self.assertTrue( valid_date( "12/02/2022" ) )
        self.assertTrue( valid_date( "12-02-2022" ) )
        self.assertTrue( valid_date( "12.02.2022" ) )
        self.assertFalse( valid_date( "13-13-2020" ) )

    def test_valid_user_rol(self):
        app = create_test()
        with app.app_context():
            self.assertTrue( valid_user_rol( "admin" ) )
            self.assertTrue( valid_user_rol( "user" ) )
            self.assertTrue( valid_user_rol( "shopping-analyst" ) )

    def test_valid_cedula(self):
        app = create_test()
        with app.app_context():
            self.assertTrue( valid_cedula( "V-01234567" , True) )
            self.assertTrue( valid_cedula( "E-12345678" , True) )

    def test_invalid_cedula_omisis(self):
        app = create_test()
        with app.app_context():
            self.assertFalse( valid_cedula( "1234567" , True) )
            self.assertFalse( valid_cedula( "V1234567" , True) )
            self.assertFalse( valid_cedula( "V-123456789" , True) )
            self.assertFalse( valid_cedula( "     V-1234567" , True) )

    def test_invalid_cedula_exceed(self):
        app = create_test()
        with app.app_context():
            self.assertFalse( valid_cedula( "V-123456789" , True) )
            self.assertFalse( valid_cedula( "     V-1234567" , True) )


    def test_valid_ended(self):
        app = create_test()
        with app.app_context():
            self.assertTrue( valid_ended( "12/01/2022" , "12/02/2022") )
            self.assertTrue( valid_ended( "12/01/2021" , "12/01/2022") )

    def test_valid_harvest(self):
        app = create_test()
        with app.app_context():
            self.assertTrue( validate_harvest( "Cosecha i" ) )
            self.assertTrue( validate_harvest( "Cosecha 2" ) )

    def test_valid_harvest_status(self):
        self.assertTrue( valid_harvest_status( "active" ) )
        self.assertTrue( valid_harvest_status( "closed" ) )
        self.assertFalse( valid_harvest_status( "other" ) )

    def test_invalid_harvest_status(self):
        self.assertFalse( valid_harvest_status( "other" ) )
        self.assertFalse( valid_harvest_status( "Activa" ) )
        self.assertFalse( valid_harvest_status( "Cerrada" ) )
        self.assertFalse( valid_harvest_status( "Active" ) )
        self.assertFalse( valid_harvest_status( "Closed" ) )


    def test_valid_user_name(self):
        self.assertTrue( valid_user( "Analista" ) )
        self.assertTrue( valid_user( "Eros" ) )
        self.assertTrue( valid_user( "admin" ) )
        self.assertFalse( valid_user( "other" ) )
        self.assertFalse( valid_user( "vendedor" ) )

    def test_valid_productor(self):
        app = create_test()
        with app.app_context():
            self.assertTrue( valid_productor( "Alana" ) )

    def test_invalid_productor(self):
        app = create_test()
        with app.app_context():
            self.assertFalse( valid_productor( "Lorem" ) )


    #---------------------LOGIN ROUTES -----------------------#
    def test_root_get(self):
        res = self.client.get('/')
        self.assertEqual(200, res.status_code)
        self.assertIn( b"Theodoma Cacao", res.data )

    def test_root_post(self):
        res = self.client.post('/')
        self.assertEqual(405, res.status_code)

    def test_login_get(self):
        res = self.client.get('/login')
        redir = b"redirected"
        self.assertEqual(302, res.status_code)
        self.assertIn( redir, res.data )

    def test_login_post(self):
        res = self.client.post('/login')
        self.assertEqual(302, res.status_code)


    #----------------ACCESS-LOGOUT WARRANTED-----------------#

    def test_admin_access(self):
        self.client.post('/login', data=dict(username='admin', password='admin'))
        res = self.client.get('/')
        self.assertIn( b"Bienvenido", res.data )
        self.client.get('/logout')
        res = self.client.get('/')
        self.assertEqual(200, res.status_code)
        self.assertIn( b"Theodoma Cacao", res.data )

    #------------------UPDATE PASSWOD---------------------#

    def test_update_password(self):
        self.client.post('/login', data=dict(username='admin', password='admin'))
        res = self.client.get('/')
        self.assertIn( b"Bienvenido", res.data )
        



    



if __name__ == '__main__':
    unittest.main()