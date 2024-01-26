from blackjack.deck import Deck
from blackjack.hand import Hand
from entities.basic_player import BasicPlayer
from entities.dealer import Dealer


def round(player, dealer, deck):
    # Draw 2 cards and place bet
    dealer.start_round(deck)
    player.start_round(deck, bet=100)

    # Ensure no initial split for testing
    while player.hand.cards[0] == player.hand.cards[1]:
        player.hand.cards.pop()
        player.hit_me(deck)

    # Player decision loop
    while not player.is_done:
        decision = player.get_decision(dealer)
        if decision == 'h':
            player.hit_me(deck)
        elif decision == 's':
            player.stand()
        elif decision == 'd':
            player.doubles()
        elif decision == 'y':       # Split case
            pass

    # Dealer decision loop
    if player.hand.value < 21:
        while not dealer.is_done:
            decision = dealer.get_decision()
            if decision == 'hit':
                dealer.hit_me(deck)
            elif decision == 'stand':
                dealer.stand()

    # Check for busts and compare hand values
    if player.hand.value > 21:
        player.round_outcome(loss=True)
    elif dealer.hand.value > 21:
        player.round_outcome(win=True)

    elif player.hand.value > dealer.hand.value:
        player.round_outcome(win=True)
    elif player.hand.value < dealer.hand.value:
        player.round_outcome(loss=True)
    else:
        player.round_outcome(draw=True)

    print('Player:', player.hand)
    print('Dealer:', dealer.hand)
    print('----------------------------------')
    # Clear hands:
    dealer.hand = Hand()
    player.hand = Hand()


if __name__ == '__main__':
    deck = Deck(8)
    player = BasicPlayer()
    dealer = Dealer()
    for i in range(50):
        round(player, dealer, deck)
