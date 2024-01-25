from blackjack.hand import Hand
from blackjack.card import Card
from players.dealer import Dealer
import pandas as pd


class BasicPlayer(object):

    def __init__(self):
        self.hand = Hand()

        self.current_bet = 0
        self.total_bets = 0
        self.total_earnings

        self.rounds = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0

    def hit_me(self, deck):

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
        while self.hand.aces > 0:
            if self.hand.value > 21:
                self.hand.value -= 10
                self.hand.aces -= 1

    def get_decision(self):

        pass

    # Normal round outcome (ie no splits, doubling, etc takes place)
    def normal_round_outcome(self, win=False, draw=False, loss=False):

        self.rounds += 1

        if win:
            self.wins += 1
            # Add bet to total_earnings
            self.total_earnings += self.current_bet

        elif loss:
            self.losses += 1
            # Subtract bet from total_earnings
            self.total_earnings -= self.current_bet

        elif draw:
            # total_earnings remains the same
            self.draws += 1

        # Reset current_bet to 0
        self.current_bet = 0

    def start_round(self, deck, bet=10):

        # Update bet variables
        self.current_bet = bet
        self.total_bets += bet

        # Pop 2 cards from deck into Player's hand
        self.hand.cards.append(deck.cards.pop())
        self.hand.cards.append(deck.cards.pop())
