class User:
    '''A class that stores users information'''

    def __init__(self, first_name, last_name, age, location):
        '''We will initialise the class'''
        self.first_name  =  first_name
        self.last_name = last_name  
        self.age = age 
        self.location = location 
        self.login_attempts = 0

    def describe_user(self):
        '''Prints the summary of users'''
        print(f'The users name is {self.first_name}')

    def greet_user(self):
        '''Greets the user'''
        print(f'hello {self.first_name} {self.last_name}')

    def increment_login_attempts(self):
        '''Increments the login attempts'''
        self.login_attempts += 1

    def reset_login_attempts(self):
        '''Increments the login attempts'''
        self.login_attempts = 0
