import random


class Card():
    """A card with a number between 1 and 13.

    The responsibility of Card is to keep track of the card number.
   
    Attributes:
        value (int): The number of card.
    """

    def __init__(self) -> None:
        """Constructs a new instance of Card with a value and points attribute.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0

    def pick_one(self):
        """Generates a new random value and display the value.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1,13)
