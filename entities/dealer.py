from blackjack.hand import Hand
from blackjack.card import Card
from blackjack.deck import Deck


class Dealer(object):

    def __init__(self):
        self.hand = Hand()
        self.is_done = False

    # Dealer stands on hard 17, hits on soft 17 (ie H17 game)
    def hit_me(self, deck, player):

        # If deck is empty, replace and shuffle deck
        if deck.is_empty():
            number_of_decks = deck.number_of_decks
            deck.shuffle(number_of_decks)
            # Reset count
            if player.card_counting:
                self.count = 0

        # Remove card from deck and add to dealers hand
        card = deck.cards.pop()
        self.hand.cards.append(card)

        # Add to count
        if player.card_counting:
            player.count += card.count_value

        # Decrease the no. of cards left in deck
        # if deck.cards_left < 1:
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

        # Set up_card field (if applicable)
        if len(self.hand.cards) > 1:
            self.up_card = self.hand.cards[1]

        # Check if dealer has gone bust:
        if self.hand.value > 21:
            self.is_done = True

    def get_decision(self):
        # Soft hand
        if self.hand.aces > 1:
            if self.hand.value < 18:
                return 'h'
            else:
                return 's'
        # Hard hand
        else:
            if self.hand.value < 17:
                return 'h'
            else:
                return 's'

    def start_round(self, deck, player):

        # Pop 2 cards from deck into Dealer's hand
        # with SuppressPrint:
        self.hit_me(deck, player)
        self.hit_me(deck, player)

        # Set up_card field (if applicable)
        self.up_card = self.hand.cards[1]

        print('Dealer:', self.hand)

    def stand(self):
        self.is_done = True

    def goes_bust(self):
        print('dealer goes bust!!')
