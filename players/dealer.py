from blackjack.hand import Hand
from blackjack.card import Card


class Dealer(object):

    def __init__(self):
        self.hand = Hand()

    # Dealer stands on hard 17, hits on soft 17 (ie H17 game)
    def hit_me(self, deck):

        # Remove card from deck and add to dealers hand
        card = deck.cards.pop()
        self.hand.append(card)

        # Update hand value
        self.hand.value += card.value

        # Check for aces
        ace_instance = Card('ace', 'spades')
        if card == ace_instance:
            self.hand.aces += 1

        # Change ace from 11 to 1 if dealer goes bust with an ace
        while self.hand.aces > 0:
            if self.hand.value > 21:
                self.hand.value -= 10
                self.hand.aces -= 1

    def decide(self):

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
