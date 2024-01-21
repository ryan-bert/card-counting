class Card(object):

    def __init__(self, rank, suit):
        """
        Initializes a Card object with a rank and a suit.

        Args:
            rank (str): The rank of the card, e.g., 'two', 'three', 'king'.
            suit (str): The suit of the card, e.g., 'hearts', 'diamonds', 'clubs'.

        Attributes:
            rank (str): The rank of the card.
            suit (str): The suit of the card.
            count (int): The count value associated with the card based on the Red Zen or Zen Count system.

        The count value is assigned based on the rank of the card according to the specified counting system.

        """
        self.rank = rank
        self.suit = suit

        # Set count for individual cards
        if self.rank in ['four', 'five', 'six']:
            self.count = 2

        elif self.rank in ['two', 'three', 'seven']:
            self.count = 1

        elif self.rank in ['eight', 'nine']:
            self.count = 0

        elif self.rank in ['ace']:
            self.count = -1
        # Account for ['ten','jack','queen','king']
        else:
            self.count = -2

    def __str__(self):
        """
        Returns a human-readable string representation of the card.

        Returns:
            str: A string representing the card, e.g., 'two of hearts'.
        """
        return f"{self.rank} of {self.suit}"

    def value(self):
        """
        Returns the numerical value of the card based on the Blackjack rules.

        Returns:
            int: The numerical value of the card, e.g., 2, 10, 11 (for Ace).
        """
        rank_values = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
                       'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
                       'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}

        return rank_values[self.rank]

    def __eq__(self, other):
        """
        Checks if two cards are equal based on their numerical values.

        Args:
            other (Card): Another Card object to compare with.

        Returns:
            bool: True if the numerical values of the cards are equal, False otherwise.
        """
        return self.value() == other.value()
