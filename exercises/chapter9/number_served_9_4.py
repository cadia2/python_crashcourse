class Restaurant:
    '''A simple attempt describing a restaurant'''


    def __init__(self, name, cuisine):
        '''Initialise name and cuisine attributes'''
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0


    def describe_restaurant(self):
        '''Prints the name and cuisine'''
        print(f'The name of the restaurant is {self.name}')
        print(f'The cuisine of the restaurant is {self.cuisine}')


    def open_restaurant(self):
        '''Prints that the restaurant is open'''
        print(f'{self.name} is open.')

    def set_number_served(self, number):
        self.number = number
        self.number_served = self.number

    def increment_number_served(self, number):
        '''Adds more clients served '''
        self.number_served += number 
        

restaurant = Restaurant('Nobu','japaneese')

#print(restaurant.name)
#print(restaurant.cuisine)
#restaurant.describe_restaurant()
#restaurant.open_restaurant()

#print(f'The number of served customers is: {restaurant.number_served}')
#restaurant.number_served = 6
#print(f'The number of served customers is: {restaurant.number_served}')
#

#restaurant.set_number_served(12)
restaurant.increment_number_served(78)
print(f'The number of served customers is: {restaurant.number_served}')
