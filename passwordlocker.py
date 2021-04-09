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
