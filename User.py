class User:

    '''
    A class that gets users input innstance 
    '''

    list = []

    def __init__(self,username, password):

        self.name = name
        self.password = password

    print("Welcome to Password LocK. select one of the below options to continue:")
    print("\n1. Login \n2. Register new account \n3. Exit")
    user_option = input()

    if user_option == "1":
        print("Login")
    elif user_option == "2":
        create_account()
    elif user_option == "3":
        exit()
    else:
        print("Invalid option")









 