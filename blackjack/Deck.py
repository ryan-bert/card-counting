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

    def update_count(self):
        # Reset the count
        self.running_count = 0

        # Find played cards using list comprehension
        played_cards = [
            card for card in self.original_order if card not in self.cards]

        played_cards_str = ", ".join(str(card) for card in played_cards)
        print("Played Cards:", played_cards_str)

        # Update count based on played cards
        for card in played_cards:
            self.running_count += card.count_value

        return self.running_count

    def get_true_count(self):
        # Calculate approximate no. of decks remaining
        cards_remaining = len(self.cards)
        decks_remaining = cards_remaining / 52  # There are 52 cards in a deck

        print(f'Running count: {self.running_count}')

        if decks_remaining > 0:
            # Calculate true count
            true_count = self.running_count / decks_remaining
        else:
            true_count = self.running_count

        return true_count
