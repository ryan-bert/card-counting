from blackjack.hand import Hand
from blackjack.card import Card
from blackjack.deck import Deck


class Dealer(object):

    def __init__(self):
        self.hand = Hand()

    # Dealer stands on hard 17, hits on soft 17 (ie H17 game)
    def hit_me(self, deck):

        # If deck is empty, replace and shuffle deck
        if deck.is_empty():
            number_of_decks = deck.number_of_decks()
            deck = Deck(number_of_decks)

        # Remove card from deck and add to dealers hand
        card = deck.cards.pop()
        self.hand.cards.append(card)

        # Update hand value
        self.hand.value += card.value

        # Check for aces
        ace_instance = Card('ace', 'spades')
        if card == ace_instance:
            self.hand.aces += 1

        # Change ace from 11 to 1 if dealer goes bust with an ace
        while self.hand.aces > 0 and self.hand.value > 21:
            self.hand.value -= 10
            self.hand.aces -= 1

        # Set up_card field (if applicable)
        if len(self.hand.cards) > 1:
            self.up_card = self.hand.cards[1]

        # Check if dealer has gone bust:
        if self.hand.value > 21:
            self.goes_bust()

    def get_decision(self):
        # Soft hand
        if self.hand.aces > 1:
            if self.hand.value < 18:
                return 'hit'
            else:
                return 'stand'
        # Hard hand
        else:
            if self.hand.value < 17:
                return 'hit'
            else:
                return 'stand'

    def start_round(self, deck):

        # Pop 2 cards from deck into Dealer's hand
        self.hit_me(deck)
        self.hit_me(deck)

        # Set up_card field (if applicable)
        self.up_card = self.hand.cards[1]

    def stand(self):
        self.is_done = True
        self.stands += 1
        print('dealer stands.')

    def goes_bust(self):
        self.is_done = True
        print('dealer goes bust!!')
