from blackjack.hand import Hand
from blackjack.card import Card
from blackjack.deck import Deck
from tables.hard_totals import HardTotals
from tables.soft_totals import SoftTotals
from tables.pair_splitting import PairSplitting
from utils.suppress_print import SuppressPrint


# TODO: MAKE SPLIT FUNCTION

class BasicPlayer(object):

    def __init__(self):
        self.hand = Hand()
        # Variable True if player stands or goes bust
        self.is_done = False
        # Financial`metrics`
        self.current_bet = 0
        self.total_bets = 0
        self.total_earnings = 0
        # Incremental metrics
        self.rounds = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        # Busts vs stands (stands include doubling-down)
        self.busts = 0
        self.stands = 0

    def hit_me(self, deck):

        print('hit me.')

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
        while self.hand.aces > 0 and self.hand.value > 21:
            self.hand.value -= 10
            self.hand.aces -= 1

        # Check if player went bust
        if self.hand.value > 21:
            self.goes_bust()

        # Check if player got a blackjack
        elif len(self.hand.cards) == 2 and self.hand.value == 21:
            self.gets_blackjack()

    def get_decision(self, dealer):

        # create function variables
        decision = None
        deck_length = len(self.hand.cards)
        first_two_match = self.hand.cards[0] == self.hand.cards[1]

        # check for pair
        if deck_length == 2 and first_two_match:
            decision = self._search_split_table(dealer)
            # If decision is not to split, re-route to different table
            if decision == 'n' and self.hand.aces > 0:      # Pair of aces
                decision = self._search_soft_table(dealer)
            elif decision == 'n' and self.hand.aces == 0:   # Pair of non-aces
                decision = self._search_hard_table(dealer)

        # Handle ace(s)
        elif self.hand.aces > 0:
            # get decision from soft totals table
            decision = self._search_soft_table(dealer)
            # Can't double if deck_length != 2
            if decision == 'd' and deck_length > 2:
                decision = 'h'
        # Hard totals (ie no pairs, no aces)
        else:
            decision = self._search_hard_table(dealer)
            if decision == 'd' and deck_length > 2:
                decision = 'h'

        return decision

    def doubles(self):
        self.total_bets += self.current_bet
        self.current_bet *= 2
        self.is_done = True
        print("Player doubled down!")

    def gets_blackjack(self):
        self.current_bet *= 1.5
        self.is_done = True
        self.round_outcome(win=True)
        print('Blackjack!!')

    def goes_bust(self):
        self.is_done = True
        self.busts += 1
        print("Player goes bust!!")

    def stand(self):
        self.is_done = True
        self.stands += 1
        print('player stands.')

    def start_round(self, deck, bet=10):

        # Update bet variables
        self.current_bet = bet
        self.total_bets += bet

        # Pop 2 cards from deck into Player's hand
        with SuppressPrint:
            self.hit_me(deck)
            self.hit_me(deck)

        print('Player:', self.hand)

    # Normal round outcome (ie no splits, doubling, etc takes place)
    def round_outcome(self, win=False, draw=False, loss=False):

        self.rounds += 1

        if win:
            self.wins += 1
            # Add bet to total_earnings
            self.total_earnings += self.current_bet
            print('Win!')

        elif loss:
            self.losses += 1
            # Subtract bet from total_earnings
            self.total_earnings -= self.current_bet
            print('loss!')

        elif draw:
            # total_earnings remains the same
            self.draws += 1
            print('draw!')

        # Reset current_bet to 0
        self.current_bet = 0

    def _search_split_table(self, dealer):

        index = self.hand.cards[0].rank
        column = dealer.up_card.rank

        # returns 'y' or 'n'
        return PairSplitting.table.loc[index, column]

    def _search_hard_table(self, dealer):

        index = self.hand.value
        column = dealer.up_card.rank

        # returns 'h', 's' or 'd'
        return HardTotals.table.loc[index, column]

    def _search_soft_table(self, dealer):

        index = self.hand.value
        column = dealer.up_card.rank

        # returns 'h', 's' or 'd'
        return SoftTotals.table.loc[index, column]
