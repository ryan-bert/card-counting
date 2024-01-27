from blackjack.card import Card
import random


class Deck(object):

    def __init__(self, number_of_decks):

        ranks = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight',
                 'nine', 'ten', 'jack', 'queen', 'king', 'ace']

        suits = ['spades', 'hearts', 'diamonds', 'clubs']

        # Create empty list of Card objects
        self.cards = []
        # Initialize/reset count
        self.running_count = 0

        # Populate the Deck with Card objects
        for i in range(number_of_decks):
            for suit in suits:
                for rank in ranks:
                    self.cards.append(Card(rank, suit))

        # Keep track of no. of decks
        self.number_of_decks = number_of_decks

        # shuffle cards
        random.shuffle(self.cards)

        # Store a copy of the shuffled deck
        self.original_order = self.cards.copy()

    def is_empty(self):
        return len(self.cards) == 0

    def get_remaining_length(self):
        return (len(self.cards)/52.0)
