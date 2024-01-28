from blackjack.card import Card
import random


class Deck(object):
    """
    A class to represent a deck of playing cards for blackjack.

    Attributes:
        ranks (list of str): Possible card ranks.
        suits (list of str): Possible card suits.
        cards (list of Card): The list of Card objects in the deck.
        running_count (int): The running count for card counting strategies.
        number_of_decks (int): The number of decks used in the game.
        cards_left (int): The number of cards left in the deck.
    """

    def __init__(self, number_of_decks):
        """
        Constructs all the necessary attributes for the deck object.

        Parameters:
            number_of_decks (int): The number of individual decks to include in the deck.
        """

        # Possible Card.rank values
        self.ranks = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight',
                      'nine', 'ten', 'jack', 'queen', 'king', 'ace']
        # Possible Card.rank values
        self.suits = ['spades', 'hearts', 'diamonds', 'clubs']

        # Create empty list of Card objects
        self.cards = []
        # Initialize/reset count
        self.running_count = 0

        # Populate the Deck with Card objects
        for i in range(number_of_decks):
            for suit in self.suits:
                for rank in self.ranks:
                    self.cards.append(Card(rank, suit))

        # Keep track of OG no. of decks and cards left
        self.number_of_decks = number_of_decks
        self.cards_left = number_of_decks * 52

        # shuffle cards
        random.shuffle(self.cards)

    def is_empty(self):
        """
        Checks if the deck is empty.

        Returns:
            bool: True if the deck is empty, False otherwise.
        """
        return len(self.cards) == 0

    def shuffle(self, number_of_decks):
        """
        Replenishes and shuffles the deck to the original number of decks.

        Parameters:
            number_of_decks (int): The number of individual decks to refill the deck.
        """

        self.cards = []

        # Populate the Deck with Card objects
        for i in range(number_of_decks):
            for suit in self.suits:
                for rank in self.ranks:
                    self.cards.append(Card(rank, suit))

        # Keep track of OG no. of decks and cards left
        self.number_of_decks = number_of_decks
        self.cards_left = number_of_decks * 52

        # shuffle cards
        random.shuffle(self.cards)
