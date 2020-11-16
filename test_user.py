import unittest
from user import User
from user import Credential
class TestUser(unittest.TestCase):
    '''
    test class that defines test cases for the user class
    Args:
        unittest,TestCase: TestCase class that helps in creating test
    '''
    def setUp(self):
        '''
        set up method of test case
        '''
        self.new_user=User("Deborah","Debby07","Ingabineza","ingabineza@gmail.com")
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Deborah")
        self.assertEqual(self.new_user.username,"Debby07")
        self.assertEqual(self.new_user.password,"Ingabineza")
        self.assertEqual(self.new_user.email,"ingabineza@gmail.com")
    def test_save_user(self):
        '''
        to test if the user object information is saved into a list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),4)
    def test_display_all_users(self):
        '''
        to display all users saved
        '''
        self.assertEqual(User.display_users(),User.user_list)
    def test_user_exists(self):
        '''
        test if we ca return our user information
        '''
        self.new_user.save_user()
        test_user=User("Test","user","password","test@user.com")
        test_user.save_user()
        user_exists=User.user_exist("Test")
        self.assertTrue(user_exists)
    def test_delete_user(self):
        '''
        delete user to test if we can delete a user
        '''
        self.new_user.save_user()
        test_user=User("Test","user","password","test@user.com")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)
    def test_find_user_by_name(self):
        '''
        test to check if we can find the user name and display information
        '''
        self.new_user.save_user()
        test_user=User("Test","user","password","test@user.com")
        test_user.save_user()
        found_user=User.find_by_name("Test")
        self.assertEqual(found_user.first_name,test_user.first_name)

if __name__=='__main__':
    unittest.main()