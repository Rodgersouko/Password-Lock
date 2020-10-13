from credential import Credentials

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

    @classmethod
    def find_credential(cls, username):
        '''
        Method that checks if Credentials exist in our list

        '''

        for credential in Credential.credential_list:
            if credential.credential_name == name:
                return True

        return False
    

    @classmethod
    def display_user(cls):
        '''
        Method that returns the user list
        '''
        
        return cls.list

    @classmethod
    def user_exist(cls, username):
        '''
        Method that checks if a user exists in the user list
        
        Args:
            name: name of the user to search
            
        Returns:
            Boolean: true/false depending if the user exists
            
        '''
        
        for user in cls.list:
            if user.username == name:
                return True
            
        return False

    def delete_user(self):

        '''
        function for deleting objects from list
        '''

        User.list.remove(self)
        


        
    print("Welcome to Password LocK. select one of the below options to continue:")
    print("\n1. Login \n2. Register new account \n3. View accounts\n4. Exit")
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
            # user_name = input('New User Name : ')
            # # print('/n')
            # pwd = input('Password : ')
            # print('\n')
            print(" ")
            print("-" * 100)
            print("      CREATE A NEW ACCOUNT!")
            print(" ")
            print("what is your first name?..")
            print(" ")
            f_name =input()
            print("What is your middle name?..")
            print(" ")
            m_name= input()
            print("what is your email address?..")
            print(" ")
            e_mail= input()
            print ("what is your facebook password?..")
            print(" ")
            face_bookp =input()
            print("what is your email password?..")
            print(" ")
            e_mailp= input()
            print('\n')
            print(f"New Account  {f_name } { m_name} { face_bookp } has been created")
            print('\n')

            
    elif user_option == "3":
            print(" ")
            print(" ")
            print("TO GENERATE A PASSWORD ADD IN YOUR FIRST NAME AND FACEBOOK BELOW!!")
            print(" ")
            list_of_inputs = [credentials for credentials  in input()]

            # list_of_inputs= list(list_of_inputs)
            list_of_inputs.reverse()



            print(list_of_inputs)
            
    elif user_option == "4":
            print(f"Have a nice day...")
            # break
    else:
        print("Invalid option")

    