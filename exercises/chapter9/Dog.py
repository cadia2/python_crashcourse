class Dog:
    '''A simple attempt to model a dog.'''

    def __init__(self, name, age):
        '''Initialise name and age attributes'''
        self.name = name
        self.age = age


    def sit(self):
        '''Simulate a a dog sitting in response to a command'''
        print(f'{self.name} is not sitting.')


    def roll_over(self):
        '''Simulate rolling over in response to a command'''
        print(f'{self.name} rolled over!')

