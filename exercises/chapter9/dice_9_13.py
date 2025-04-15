from random import randint

class Die:
    """Represent a die which can be rolled"""
    def __init__(self, sides = 6, rolls = 10):
        """Initialize the die."""
        self.sides = sides
        self.rolls = rolls


    def roll_die(self):
        """Return a number between 1 and number of sides"""
        return randint(1, self.sides)


    def print_rolls(self):
        """Prints the roll list results"""
        roll_list = []
        for roll in range(self.rolls):
            result = self.roll_die()
            roll_list.append(result)
        print(roll_list)

d6  = Die()
d6.print_rolls()

d6  = Die(10)
d6.print_rolls()

d6  = Die(20)
d6.print_rolls()




    
        

