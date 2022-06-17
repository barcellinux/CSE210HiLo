import random


# TODO: Implement the Card class as follows...

# 1) Add the class declaration. Use the following class comment.
class Card:
    """A card with a different number from 1 to 13.

    The responsibility of Card is to keep track of the card displayed.
   
    Attributes:
        value (int): The number on the card.        
    """

# 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        """Constructs a new instance of Card with a value attribute.

        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1, 13)        

# 3) Create the draw(self) method. Use the following method comment.
    '''def draw(self):
        """Generates a new random value for the card.
        
        Args:
            self (Card): An instance of Card.
        """
               

        if self.value == 1:
            self.points = 100
        elif self.value == 5:
            self.points = 50
        else:
            self.points = 0'''