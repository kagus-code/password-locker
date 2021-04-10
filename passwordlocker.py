class User:
    '''
    Class that generates new isntance of a user 
    '''
    users_list = []  # empty users list

    def __init__(self, username, password):
        '''
        __init__ method that helps us define properties of the object
        '''
        self.username = username
        self.password = password

    def save_user(self):
        '''
        method that saves user objects into user_list
        '''
        User.users_list.append(self)

    def delete_user(self):
        '''
        method that deletes a saved user 
        '''
        User.users_list.remove(self)

    @classmethod
    def user_exist(cls, username):
        '''
        Method that checks if a user exists from the user list.
        Args:
            username: username to search if they exist
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.users_list:
            if user.username == username:
                return True

        return False


class Credentials:
    '''
    Class generates new instance for credentials 
    '''
    credentials_list = []  # empty credentials list

    def __init__(self, account, user_name, pass_word):
        '''
        init method that defines properties of the object
        '''
        self.account = account
        self.user_name = user_name
        self.pass_word = pass_word

    def save_credentials(self):
        '''
        method that saves Credentials objects into credentials_list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        method that deletes a saved credentials 
        '''
        Credentials.credentials_list.remove(self)
