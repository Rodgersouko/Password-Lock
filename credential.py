class Credentials():
    """
    credentials class to create new objects of credentials
    """
    credentials_list = []

    def __init__(self,account,userName, password):
 
        self.account = account
        self.userName = userName
        self.password = password

    def save_details(self):
        """
        function for saving user objects to credential-list
        """
        Credentials.credentials_list.append(self)

    @classmethod
    def generate_password(cls):
        '''
        Method that generates a random alphanumeric password
        '''
        size = 8

        alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase

        password = ''.join( choice(alphanum) for num in range(size) )
        
        return password

    @classmethod
    def display_credentials(cls,password):
        """
        function returning items in the credentials list
        """
        redential_list = []

        for credential in cls.credential_list:
            if credential.user_password == password:
                user_credential_list.append(credential)

        return credential_list

    @classmethod
    def credential_exist(cls, name):
        
        '''
        Method that checks if a credential exists in the credential list
            
        '''
        
        for credential in cls.credential_list:
            if credential.credential_name == name:
                return True
            
        return False 

    # def delete_credentials(self):
    #     """
    #     function for deleting objects from credential_list
    #     """
    #     Credentials.credentials_list.remove(self)
   

    # @classmethod
    # def display_accounts(cls):
    #     '''
    #     function that returns the list
    #     '''
    #     return cls.list    