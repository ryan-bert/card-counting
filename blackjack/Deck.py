from blackjack.card import Card
import random


class Deck(object):

    def __init__(self, number_of_decks):

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

        # shuffle cards
        random.shuffle(self.cards)

    def is_empty(self):
        return len(self.cards) == 0
