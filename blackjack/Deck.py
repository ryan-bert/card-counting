from blackjack.card import Card
import random


class Deck(object):

    def __init__(self, number_of_decks):
        """
        Initialize a deck of cards.

        This constructor creates a standard deck of playing cards, multiplied by the 
        number of decks specified. Each deck consists of 52 cards, with 13 ranks in 
        each of the 4 suits: spades, hearts, diamonds, and clubs.

        Args:
            number_of_decks (int): The number of standard 52-card decks to be included 
                                   in the deck.

        The deck is automatically shuffled upon initialization.
        """

        ranks = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight',
                 'nine', 'ten', 'jack', 'queen', 'king', 'ace']

        suits = ['spades', 'hearts', 'diamonds', 'clubs']

        # Create empty list of Card objects
        self.cards = []

        # Populate the Deck with Card objects
        for i in range(number_of_decks):
            for suit in suits:
                for rank in ranks:
                    self.cards.append(Card(rank, suit))

        random.shuffle(self.cards)

    def is_empty(self):
        """
        Check if the deck is empty.

        Returns:
            bool: True if the deck is empty, False otherwise.
        """
        return len(self.cards) == 0
