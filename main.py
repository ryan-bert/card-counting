from blackjack.deck import Deck
from entities.basic_player import BasicPlayer
from entities.dealer import Dealer


def round(player, dealer, deck):

    # Create a deck object
    deck = Deck(8)

    # ! REMOVE
    player = BasicPlayer()
    dealer = Dealer()
    # ! REMOVE

    # Draw 2 cards and place bet
    dealer.start_round(deck)
    player.start_round(deck, bet=100)

    decision = player.get_decision(dealer)

    print(player.hand.cards[0], player.hand.cards[1], f'dealer:{dealer.up_card}',
          f'Decision: {decision}', sep='\n')


if __name__ == '__main__':
    player = BasicPlayer()
    dealer = Dealer()
    deck = Deck(8)

    round(player, dealer, deck)
