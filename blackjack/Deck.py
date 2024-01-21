from Card import Card
import random


class Deck(object):

    def __init__(self, number_of_decks):

        ranks = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight',
                 'nine', 'ten', 'jack', 'queen', 'king', 'ace']

        suits = ['spades', 'hearts', 'diamonds', 'clubs']

        cards = []

        # Populate the Deck with Card objects
        for i in range(number_of_decks):
            for suit in suits:
                for rank in ranks:
                    cards.append(Card(rank, suit))

        for card in cards:
            print(card)

        random.shuffle(cards)
