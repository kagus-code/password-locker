#!/usr/bin/env python3.9
from passwordlocker import User
from passwordlocker import Credentials


def create_user(username, password):
    '''
    function to create new user 
    '''
    new_user = User(username, password)
    return new_user


def save_user(user):
    '''
    function to save user 
    '''
    user.save_user()


def del_user(user):
    '''
    Function to delete user account
    '''
    user.delete_user()


def check_existing_user(username):
    '''
    function to check if a user with that username exists and return Boolean
    '''
    return User.user_exist(username)

    # end of user functions


def create_credentials(account, username, password):
    '''
    function add credentials 
    '''
    new_credentials = Credentials(account, user_name, pass_word)
    return new_credentials


def save_credentials(credentials):
    '''
    function to save credentials
    '''
    return credentials.save_credentials()


def delete_credentials(credentials):
    '''
    function to delete credentials
    '''
    return credentials.delete_credentials()


def display_credentials():
    '''
    function that returns a list of all saved credentials 
    '''
    return Credentials.display_credentials()


def generate_password():
    '''
    function to generate random password
    '''
    return Credentials.generate_password()
