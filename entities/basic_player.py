from blackjack.hand import Hand
from blackjack.card import Card
from blackjack.deck import Deck
from tables.hard_totals import HardTotals
from tables.soft_totals import SoftTotals
from tables.pair_splitting import PairSplitting


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

        # If deck is empty, replace and shuffle
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
        while self.hand.aces > 0:
            if self.hand.value > 21:
                self.hand.value -= 10
                self.hand.aces -= 1

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

    def get_decision(self, dealer):

        # create function variables
        decision = None
        len = len(self.hand.cards)
        first_two_match = self.hand.cards[0] == self.hand.cards[1]

        # check for pair
        if len == 2 and first_two_match:
            decision = self.search_split_table(self.hand, dealer)

        # Handle ace(s)
        elif self.hand.aces > 0:
            # get decision from soft totals table
            decision = self.search_soft_table(self.hand, dealer)
            # Can't double if length != 2
            if decision == 'd' and len != 2:
                decision = 'h'
        # Hard totals (ie  pairs, no aces)
        else:
            decision = self.search_hard_table(self.hand, dealer)
            if decision == 'd' and len != 2:
                decision = 'h'

        return decision

    def start_round(self, deck, bet=10):

        # Update bet variables
        self.current_bet = bet
        self.total_bets += bet

        # Pop 2 cards from deck into Player's hand
        self.hand.cards.append(deck.cards.pop())
        self.hand.cards.append(deck.cards.pop())

    def _search_split_table(self, hand, dealer):

        index = self.hand.cards[0].rank
        column = dealer.up_card.rank

        # returns 'y' or 'n'
        return PairSplitting.table.loc[index, column]

    def _search_hard_table(self, hand, dealer):

        index = self.hand.value
        column = dealer.up_card.rank

        # returns 'h', 's' or 'd'
        return HardTotals.table.loc[index, column]

    def _search_soft_table(self, hand, dealer):

        index = self.hand.value
        column = dealer.up_card.rank

        # returns 'h', 's' or 'd'
        return SoftTotals.table.loc[index, column]
