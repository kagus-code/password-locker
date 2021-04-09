import unittest
from passwordlocker import User


class TestUser (unittest.TestCase):
    '''
    Test class that defines tes cases for the User behavior
    '''

    def setUp(self):
        '''
        Set up method to run before each test case.
        '''
        self.new_user = User("kagus", "king98")

    def test_init(self):
        '''
        Test case to test if the object intialized properly
        '''
        self.assertEqual(self.new_user.username, "kagus")
        self.assertEqual(self.new_user.password, "king98")


if __name__ == '__main__':
    unittest.main()
