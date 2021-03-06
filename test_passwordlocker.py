import unittest
import string
import random
from passwordlocker import User
from passwordlocker import Credentials


class TestUser (unittest.TestCase):
    '''
    Test class that defines tes cases for the User behavior
    '''

    def setUp(self):
        '''
        Set up method to run before each test case.
        '''
        self.new_user = User("kagus", "king98")

    def tearDown(self):
        '''
        tearDown method cleans up after each test is run 
        '''
        User.users_list = []

    def test_init(self):
        '''
        Test case to test if the object intialized properly
        '''
        self.assertEqual(self.new_user.username, "kagus")
        self.assertEqual(self.new_user.password, "king98")

    def test_save_user(self):
        '''
        test_save_user tests if new user object is saved into the contact list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list), 1)

    def test_save_multiple_users(self):
        '''
        test to check if we can save multiple users into the contact list 
        '''
        self.new_user.save_user()
        test_user = User('muraya', 'orion')
        test_user.save_user()
        self.assertEqual(len(User.users_list), 2)

    def test_delete_user(self):
        '''
        test if we can remove a user from the user_list 
        '''
        self.new_user.save_user()
        test_user = User("thanos", "infinity")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.users_list), 1)

    def test_user_exists(self):
        '''
        test to check if we can return boolean if user doesnt exist
        '''
        self.new_user.save_user()
        test_user = User("kagus", "king98")
        test_user.save_user()
        user_exists = User.user_exist("kagus", "king98")
        self.assertTrue(user_exists)

        # END OF USER INSTANCES


class TestCredentials (unittest.TestCase):
    '''
    Test class that defines tes cases for the User behavior
    '''

    def setUp(self):
        '''
        Set up method for each credentials test case
        '''
        self.new_credentials = Credentials("facebook", "droid", "access")

    def tearDown(self):
        '''
        tearDown method cleans up after each test is run 
        '''
        Credentials.credentials_list = []

    def test_init(self):
        '''
        Test case to test if the object intialized properly
        '''
        self.assertEqual(self.new_credentials.account, "facebook")
        self.assertEqual(self.new_credentials.user_name, "droid")
        self.assertEqual(self.new_credentials.pass_word, "access")

    def test_save_credentials(self):
        '''
        test_save_credentials tests if new credentials object is saved into the credentials list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        '''
        test to check if we can save multiple credentials into the contact list 
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("insta", "invuctus", "maneo")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credentials(self):
        '''
        test if we can remove credentials from credentials list 
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("twitter", "mwangi", "kutus")
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_display_all_credentials(self):
        '''
        method to display all credentials saved 
        '''
        self.assertEqual(Credentials.display_credentials(),
                         Credentials.credentials_list)

    def test_generate_random_password(self):
        '''
        test method for generating random password for new credentials 
        '''
        random_pass = Credentials.generate_password()

        self.new_credentials = Credentials(f"insta", "kagwima", random_pass)
        self.assertEqual(self.new_credentials.account, "insta")
        self.assertEqual(self.new_credentials.user_name, "kagwima")
        self.assertEqual(self.new_credentials.pass_word, random_pass)

    def test_find_credential_by_account(self):
        '''
        test to check if we can find a  credential by account name 
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("fb", "lol", "grant")
        test_credentials.save_credentials()
        found_account = Credentials.find_by_account("fb")
        self.assertEqual(found_account.user_name, test_credentials.user_name)

    def test_credentials_exists(self):
        '''
        test to check if we can return a boolean if we cannot find credentials
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("photoshop", "kagus", "king98")
        test_credentials.save_credentials()
        credentials_exists = Credentials.credential_exists("photoshop")
        self.assertTrue(credentials_exists)


if __name__ == '__main__':
    unittest.main()
