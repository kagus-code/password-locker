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
