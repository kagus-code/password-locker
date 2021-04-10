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
