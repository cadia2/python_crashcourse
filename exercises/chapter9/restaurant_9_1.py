class Restaurant:
    '''A simple attempt describing a restaurant'''

    def __init__(self, name, cuisine):
        '''Initialise name and cuisine attributes'''
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        '''Prints the name and cuisine'''
        print(f'The name of the restaurant is {self.name}')
        print(f'The cuisine of the restaurant is {self.cuisine}')

    def open_restaurant(self):
        '''Prints that the restaurant is open'''
        print(f'{self.name} is open.')

#restaurant = Restaurant('Nobu','japaneese')

#print(restaurant.name)
#print(restaurant.cuisine)
#restaurant.describe_restaurant()
#restaurant.open_restaurant()

