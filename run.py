#!/usr/bin/env python3.9
from passwordlocker import User
from passwordlocker import Credentials
import os


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


def check_existing_user(username, password):
    '''
    function to check if a user with that username exists and return Boolean
    '''
    return User.user_exist(username, password)

    # end of user functions


def create_credentials(account, user_name, pass_word):
    '''
    function add credentials 
    '''
    new_credentials = Credentials(account, user_name, pass_word)
    return new_credentials


def save_credential(credentials):
    '''
    function to save credentials
    '''
    credentials.save_credentials()


def delete_credentials(credentials):
    '''
    function to delete credentials
    '''
    credentials.delete_credentials()


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


def main():

    print("Welcome to PassVault  Sign up for an account below")
    username = input("Enter your desired username : ")
    password = input("Enter password :")
    # create and save new user
    save_user(create_user(username, password))

    print("*"*50)
    print(f"Log in to your account to proceed")
    print("*"*50)

    username = input("Username :")

    password = input("Password :")
    os.system('clear')


if __name__ == '__main__':

    main()
