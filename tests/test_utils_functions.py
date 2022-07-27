from utils.functions import *
import unittest
from app import create_app

class TestUtilsFunctions(unittest.TestCase):
    
    def test_valid_name(self):
        self.assertFalse( valid_name("Hola09") )
        self.assertTrue( valid_name("QWERTYUIOPASDFGHJKLZXVCBBCX..asd.,asdasd") )
    
    def test_valid_username(self):
        self.assertTrue(valid_username("Username_with_underscores"))
        self.assertFalse(valid_username("username-with-scores"))
        self.assertFalse(valid_username("asd"))
        self.assertFalse(valid_username("ATooLongUsernameMostNotBeAllowedAtAll"))
        self.assertFalse(valid_username("   no    empty   espaces  "))
        self.assertFalse( valid_username("eycer") )

    def test_valid_email(self):
        self.assertTrue( valid_email( "email@domin.extention" ) )
        self.assertFalse( valid_email( "email.domin.extention" ) )
        self.assertFalse( valid_email("randomwords") )
        self.assertFalse( valid_email( "   email@domin.extention   " ) )

    def test_valid_gender(self):
        self.assertTrue( valid_gender('male') )
        self.assertTrue( valid_gender('female') )
        self.assertTrue( valid_gender('other') )
        self.assertFalse( valid_gender('helicopter') )
        self.assertFalse( valid_gender('noBinary') )


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
        app = create_app()
        with app.app_context():
            self.assertTrue( valid_user_rol( "admin" ) )
            self.assertTrue( valid_user_rol( "user" ) )
            self.assertTrue( valid_user_rol( "shopping-analyst" ) )
            self.assertFalse( valid_user_rol( "Lorem" ) )

    def test_valid_cedula(self):
        app = create_app()
        with app.app_context():
            self.assertTrue( valid_cedula( "V-01234567" , True) )
            self.assertTrue( valid_cedula( "E-12345678" , True) )
            self.assertFalse( valid_cedula( "1234567" , True) )
            self.assertFalse( valid_cedula( "     V-1234567" , True) )
            self.assertFalse( valid_cedula( "V1234567" , True) )
            self.assertFalse( valid_cedula( "V-123456789" , True) )
        
    def test_valid_ended(self):
        app = create_app()
        with app.app_context():
            self.assertTrue( valid_ended( "12/01/2022" , "12/02/2022") )
            self.assertTrue( valid_ended( "12/01/2021" , "12/01/2022") )
            self.assertFalse( valid_ended( "12/01/2022" , "12/01/2021") )
    
    def test_valid_productor_type(self):
        app = create_app()
        with app.app_context():
            self.assertTrue( valid_productor_type("Productor 1I"))
            self.assertFalse( valid_productor_type( "Productor 1" ) )

    def test_valid_harvest(self):
        app = create_app()
        with app.app_context():
            self.assertTrue( validate_harvest( "Cosecha i" ) )
            self.assertTrue( validate_harvest( "Cosecha 2" ) )
            self.assertTrue( validate_harvest( "Cosecha Jun 22 - Jul 22" ) )
            self.assertFalse( validate_harvest( "Lorem" ) )


    def test_valid_harvest_status(self):
        self.assertTrue( valid_harvest_status( "active" ) )
        self.assertTrue( valid_harvest_status( "closed" ) )
        self.assertFalse( valid_harvest_status( "other" ) )


    def test_valid_user_name(self):
        self.assertTrue( valid_user( "Analista" ) )
        self.assertTrue( valid_user( "Eros" ) )
        self.assertTrue( valid_user( "administrador" ) )
        self.assertFalse( valid_user( "other" ) )
        self.assertFalse( valid_user( "vendedor" ) )

    def test_valid_purchase(self):
        app = create_app()
        with app.app_context():
            self.assertTrue( valid_purchase( "Seco" ) )
            self.assertTrue( valid_purchase( "Fermentado" ) )
            self.assertFalse( valid_purchase( "Lorem" ) )

    def test_valid_productor(self):
        app = create_app()
        with app.app_context():
            self.assertTrue( valid_productor( "Alan" ) )
            self.assertFalse( valid_productor( "Lorem" ) )

if __name__ == '__main__':
    unittest.main()