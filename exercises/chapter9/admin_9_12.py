from user_9_12 import User
from privileges_9_12 import Privileges
class Admin(User):
    '''We will make an admin class which lists his privileges'''
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()
