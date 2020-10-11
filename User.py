class User:

    '''
    A class that gets users input innstance 
    '''

    list = []

    def __init__(self,username, password):

        self.name = name
        self.password = password



    def save_user(self):

        '''
        function for saving user objects to list
        '''

        User.list.append(self)


    def delete_user(self):

        '''
        function for deleting objects from list
        '''

        User.list.remove(self)    

    @classmethod
    def display_accounts(cls):
        '''
        function that returns the list
        '''
        return cls.list    

        
    print("Welcome to Password LocK. select one of the below options to continue:")
    print("\n1. Login \n2. Register new account \n3. Exit")
    user_option = input()

    if user_option == "1":
            print("Enter your account details")
            print ('\n')
            account_name = input('Account: ')
            print ('\n')
            user_name = input('User name: ')
            # print('\n')
            while True:
                print("\n1. To type your own pasword:\n2. To generate random Password")
                password_Choice = input().lower()
                if password_Choice == '1':
                    password = input("Enter Password")
                    break
                elif password_Choice == '2':
                    password = generate_Password()
                    break
                else:
                    print("Invalid password please try again")
    elif user_option == "2":
            user_name = input('New User Name : ')
            # print('/n')
            pwd = input('Password : ')
            print ('\n')

    elif user_option == "3":
            print(f"Have a nice day...")
            # break
    else:
        print("Invalid option")

    