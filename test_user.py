import unittest
from user import User
from user import Credential
class TestUser(unittest.TestCase):
    '''
    test class that defines test cases for the user class
    '''
    def setUp(self):
        '''
        set up method of test case
        '''
        self.new_user=User("Claudine","Clauma","123456","clauma@gmail.com")
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Claudine")
        self.assertEqual(self.new_user.username,"Clauma")
        self.assertEqual(self.new_user.password,"123456")
        self.assertEqual(self.new_user.email,"clauma@gmail.com")
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
class TestCredentials(unittest.TestCase):
    '''
    class that test the credential
    Args:append
        unittestappend and test case help in creating test for our credential
    '''
    def test_check_user(self):
        '''
        methode to check if our user login work
        '''
        self.new_user=User("Claudine","Clauma","123456","clauma@gmail.com")
        self.new_user.save_user()
        userOne=User("Claudine","Clauma","123456","clauma@gmail.com")
        userOne.save_user()
        for user in User.user_list:
            if user.first_name == userOne.first_name and user.password==userOne.password:
                current_user=user.first_name
        return current_user
        self.assertEqual(current_user,Credential.check_user(userOne.password,userOne.first_name))
    def setUp(self):
        '''
        set up method of test case
        '''
        self.new_credential=Credential("mahoro","instagram","mah_oro","00000")
    def test__init(self):
        '''
        test_init test case to test if the object is initialized properly for credential
        '''
        self.assertEqual(self.new_credential.first_name,'mahoro')
        self.assertEqual(self.new_credential.platform_name,"instagram")
        self.assertEqual(self.new_credential.account_name,"mah_oro")
        self.assertEqual(self.new_credential.password,"00000")
    def test_save_credentials(self):
        '''
        method which test to save credential
        '''
        self.new_credential.save_credential()
        twitter=Credential("coco","Twitter","coco12","33333")
        twitter.save_credential()
        self.assertEqual(len(Credential.credential_list),2)
    def tearDown(self):
        '''
        tear down method that does clean after each test case.
        '''
        User.user_list=[]
        Credential.credential_list=[]
    def test_disp_credential(self):
        '''
        method to check if display works
        '''
        self.new_credential.save_credential()
        twitter=Credential("coco","Twitter","coco12","33333")
        twitter.save_credential()
        gmail=Credential("Claudine","gmail","Clauma","123456")
        gmail.save_credential()
        instagram=Credential("mahoro","instagram","mah_oro","00000")
        self.assertEqual(len(Credential.disp_credential(twitter.first_name)),3)
    def test_find_site(self):
        '''
        Methode to find by site name and retun the correct credentials
        '''
        self.new_credential.save_credential()
        twitter=Credential("coco","Twitter","coco12","33333")
        twitter.save_credential()
        credential_exists=Credential.find_site('Twitter')
        self.assertEqual(credential_exists,twitter)
if __name__=='__main__':
    unittest.main()