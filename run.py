#!/usr/bin/env python3.9
from passwordlocker import User
from passwordlocker import Credentials
import os


print(""" 

 __        _______ _     ____ ___  __  __ _____   _____ ___    ____   _    ____ ____     __     ___   _   _ _     
 \ \      / / ____| |   / ___/ _ \|  \/  | ____| |_   _/ _ \  |  _ \ / \  / ___/ ___|    \ \   / / \ | | | | |    
  \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|     | || | | | | |_) / _ \ \___ \___ \ ____\ \ / / _ \| | | | |    
   \ V  V / | |___| |__| |__| |_| | |  | | |___    | || |_| | |  __/ ___ \ ___) |__) |_____\ V / ___ \ |_| | |___ 
    \_/\_/  |_____|_____\____\___/|_|  |_|_____|   |_| \___/  |_| /_/   \_\____/____/       \_/_/   \_\___/|_____|
                                                                                                                  
                                                                                                             


""")


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
    print("""  +-+-+-+-+-+-+   +-+-+-+-+-+-+-+   +-+-+-+   +-+-+   +-+-+-+-+-+-+-+ +-+-+-+-+
 |P|l|e|a|s|e|   |s|i|g|n|-|u|p|   |f|o|r|   |a|n|   |a|c|c|o|u|n|t| |h|e|r|e|
 +-+-+-+-+-+-+   +-+-+-+-+-+-+-+   +-+-+-+   +-+-+   +-+-+-+-+-+-+-+ +-+-+-+-+ """)
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
    print("-"*50)
    print(f"DASHBOARD of {username}'s PASS-VAUL ACCOUNT ")
    print("-"*50)
    print("""USE THE FOLLOWING CODES NAVIGATE THE DASHBOARD ,
        1:st-  STORE EXISTING CREDENTIALS,
        2:nc - CREATE NEW CREDENTIALS
        3:disp - DISPLAY ACCOUNTS""")

    while check_existing_user(username, password):

        code_cred = input("enter NAVIGATION code(st,nc,disp) :").lower()
        if code_cred == "st":
            account = input('Enter ACCOUNT NAME (eg,twitter):')
            user_name = input(f'USERNAME for {account} :')
            pass_word = input(f'PASSWORD for {account} :')
            save_credential(create_credentials(account, user_name, pass_word))
            print('\n')
            print(
                f'details for {account} account have been saved successfully---ENTER disp TO VIEW')
            print("_"*30)

        elif code_cred == 'disp':
            if display_credentials():
                print('\n')
                print("HERE ARE YOUR SAVED CREDENTIALS")
                print("_"*30)
                for credential in display_credentials():
                    print(f"Account name : {credential.account}")
                    print(
                        f"username : {credential.user_name}")
                    print(
                        f"password : {credential.pass_word}")
                    print("_"*30)

            else:
                print("you dont have saved accounts yet")
        elif code_cred == 'nc':
            while True:
                print("Do you want us to generate a secure password for you (y/n)")
                answer = input().lower()
                if answer == 'y':
                    account = input('Enter ACCOUNT NAME (eg,twitter):')
                    user_name = input(f'USERNAME for {account} :')
                    pass_word = generate_password()
                    print(f"Secure password is :  {pass_word}")
                    save_credential(create_credentials(
                        account, user_name, pass_word))
                    print('\n')
                    print(
                        f'details for {account} account have been saved successfully---ENTER disp TO VIEW')
                    print("_"*30)
                    break
                elif answer == 'n':
                    account = input('Enter ACCOUNT NAME (eg,twitter):')
                    user_name = input(f'USERNAME for {account} :')
                    pass_word = input(f'PASSWORD for {account} :')
                    save_credential(create_credentials(
                        account, user_name, pass_word))
                    print('\n')
                    print(
                        f'details for {account} account have been saved successfully---ENTER disp TO VIEW')
                    print("_"*30)
                    break
                else:
                    print("PLease enter YES(y) or NO(n)")
                    continue

        else:
            print("PLEASE ENTER A VALID CODE")

    else:
        print("-"*10)
        print('Please Reload and enter a valid username or password !')
        print("-"*10)


if __name__ == '__main__':

    main()
