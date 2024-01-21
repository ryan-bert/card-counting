from card import Card
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

        self.last_round = False

        ranks = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight',
                 'nine', 'ten', 'jack', 'queen', 'king', 'ace']

        suits = ['spades', 'hearts', 'diamonds', 'clubs']

        self.cards = []  # Use an instance variable instead of a local variable

        # Populate the Deck with Card objects
        for i in range(number_of_decks):
            for suit in suits:
                for rank in ranks:
                    self.cards.append(Card(rank, suit))

        # Printing each card for debugging purposes
        # for card in self.cards:
        #     print(card)

        random.shuffle(self.cards)

    def deal(self):
        """
        Deal a card from the deck.

        Removes and returns the top card of the deck. If the deck is empty, it returns
        None or can optionally raise an exception.

        Returns:
            Card: The top card from the deck. Returns None if the deck is empty.
        """

        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

    def is_empty(self):
        """
        Check if the deck is empty.

        Returns:
            bool: True if the deck is empty, False otherwise.
        """
        return len(self.cards) == 0
