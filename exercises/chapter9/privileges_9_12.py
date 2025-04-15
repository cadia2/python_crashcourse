class Privileges:
    '''class only for privileges'''
    def __init__(self, privileges = []):
        '''we will initialise the class'''
        self.privileges = privileges


    def show_privileges(self):
        print("The admin's privileges are:")
        for privilege in self.privileges:
            print(f"\t{privilege}")
