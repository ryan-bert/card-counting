
class Card(object):
    """
    Represents a playing card.

    Attributes:
        rank (str): The rank of the card (e.g., 'two', 'king').
        suit (str): The suit of the card (e.g., 'spades', 'hearts').
        count_value (int): The card's value for card counting.
        value (int): The numeric value of the card in the game.
    """

    def __init__(self, rank, suit):

        # Set object fields
        self.rank = rank
        self.suit = suit

        # Set count_value for individual cards
        if self.rank in ['four', 'five', 'six']:
            self.count_value = 2
        elif self.rank in ['two', 'three', 'seven']:
            self.count_value = 1
        elif self.rank in ['eight', 'nine']:
            self.count_value = 0
        elif self.rank in ['ace']:
            self.count_value = -1
        # Account for ['ten','jack','queen','king']
        else:
            self.count_value = -2

        # Set card value
        rank_values = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
                       'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
                       'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}
        self.value = rank_values[self.rank]

    def __str__(self):
        """
        Returns a string representation of the card.

        Returns:
            str: A string in the format "{rank} of {suit}".
        """
        return f"{self.rank} of {self.suit}"

    def __eq__(self, other):
        """
        Checks if two cards have the same rank.

        Parameters:
            other (Card): The other card to compare.

        Returns:
            bool: True if the cards have the same rank, False otherwise.
        """
        return self.rank == other.rank
