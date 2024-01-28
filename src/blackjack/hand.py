
class Hand(object):
    """
    Represents a hand of playing cards in the game.

    Attributes:
        cards (list of Card): The list of cards in the hand.
        value (int): The total value of the hand.
        aces (int): The number of aces in the hand.
    """

    def __init__(self):

        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        """
        Returns a string representation of the cards in the hand.

        Returns:
            str: A comma-separated string of card representations.
        """
        return ','.join(str(card) for card in self.cards)
