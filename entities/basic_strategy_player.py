from blackjack.hand import Hand
from blackjack.card import Card
from blackjack.deck import Deck
from tables.hard_totals import HardTotals
from tables.soft_totals import SoftTotals
from tables.pair_splitting import PairSplitting


class BasicPlayer(object):

    def __init__(self, name, card_counting=False):
        self.hand = Hand()
        # Name for when split occurs
        self.name = name
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
        # Initialise card counting variables
        if card_counting:
            self.count = 0
            self.card_counting = True
        else:
            self.card_counting = False

    def hit_me(self, deck):

        print(deck.cards_left)

        # If deck is empty, replace and shuffle
        if deck.is_empty():
            number_of_decks = deck.number_of_decks
            deck.shuffle(number_of_decks)
            # Reset count
            if self.card_counting:
                self.count = 0

        # Remove card from deck and add to dealers hand
        card = deck.cards.pop()
        self.hand.cards.append(card)

        # Add to count
        if self.card_counting:
            self.count += card.count_value

        # Decrease the no. of cards left in deck
        # if deck.cards_left < 1:
        #     print('EMPTY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1')
        #     deck.cards_left = number_of_decks * 52
        deck.cards_left -= 1

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

            self.is_done = True

        # Check if player got a blackjack
        elif len(self.hand.cards) == 2 and self.hand.value == 21:
            self.is_done = True

        print(deck.cards_left)

    def get_other_decision(self, dealer):

        # Default
        decision = 's'
        # Util
        deck_length = len(self.hand.cards)

        # Handle ace(s)
        if self.hand.aces > 0:
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

    def get_split_decision(self, dealer):

        # Initialize variables
        decision = 'n'
        deck_length = len(self.hand.cards)
        first_two_match = self.hand.cards[0] == self.hand.cards[1]

        # check for pair
        if deck_length == 2 and first_two_match:
            decision = self._search_split_table(dealer)

        return decision

    def doubles(self):

        self.total_bets += self.current_bet
        self.current_bet *= 2
        self.is_done = True
        print("Player doubled down!")

    def gets_blackjack(self):

        self.current_bet *= 1.5
        self.is_done = True
        print('Blackjack!!')
        self.round_outcome(win=True)

    def goes_bust(self):
        self.busts += 1
        print("Player goes bust!")
        self.round_outcome(loss=True)

    def stand(self):
        self.is_done = True
        self.stands += 1

    def start_round(self, deck, bet=10):
        # Update bet variables
        self.current_bet = bet
        self.total_bets += bet
        # Pop 2 cards from deck into Player's hand
        self.hit_me(deck)
        self.hit_me(deck)

        print(f'bet: {bet}')
        print(f'{self.name}:', self.hand)

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
        # Reset is_done to False
        self.is_done = False

    def split(self):
        # Create a new player for the split hand
        split_player = BasicPlayer("Dummy")

        # Transfer or copy the necessary attributes
        split_player.current_bet = self.current_bet
        split_player.total_bets = self.current_bet
        split_player.total_earnings = 0

        return split_player

    def add_totals(self, other):

        if other is not None:
            self.total_bets += other.total_bets
            self.total_earnings += other.total_earnings
            self.rounds += other.rounds
            self.wins += other.wins
            self.draws += other.draws
            self.losses += other.losses
            self.busts += other.busts
            self.stands += other.stands

    def _search_split_table(self, dealer):
        # Parameters for DataFrame.loc()
        index = self.hand.cards[0].rank
        column = dealer.up_card.rank

        # returns 'y' or 'n'
        return PairSplitting.table.loc[index, column]

    def _search_hard_table(self, dealer):
        # Parameters for DataFrame.loc()
        index = self.hand.value
        column = dealer.up_card.rank

        # returns 'h', 's' or 'd'
        return HardTotals.table.loc[index, column]

    def _search_soft_table(self, dealer):
        # Parameters for DataFrame.loc()
        index = self.hand.value
        column = dealer.up_card.rank

        # returns 'h', 's' or 'd'
        return SoftTotals.table.loc[index, column]

    def calculate_bet(self, zen_count, min_bet, cards_left):
        # Calculate the True Count
        decks_remaining = cards_left / 52.0
        print(f'decks_remaining: {decks_remaining}')
        if decks_remaining > 0:
            true_count = float(zen_count) / decks_remaining
        else:
            true_count = float(zen_count)

        # Calculate the bet based on the multiplier
            print(f'True count: {true_count}')
        bet = min_bet * true_count

        # Ensure bet > 0
        if true_count > 1:
            bet = min(bet, 0)
        else:
            bet = 0

        return bet
