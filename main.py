from blackjack.deck import Deck
from blackjack.hand import Hand
from entities.basic_strategy_player import BasicPlayer
from entities.dealer import Dealer


def main():

    # initialize game objects
    player = BasicPlayer()
    dealer = Dealer()
    deck = Deck(4)

    # Draw 2 cards and place bet
    player.start_round(deck, bet=100)
    dealer.start_round(deck)

    decision = player.get_decision(dealer)
    if decision == 's':
        player.split(deck)

    for index in range(len(player.hands)):
        player.index = index
        round(player, dealer, deck)


def round(player, dealer, deck):

    # Player decision loop
    while not player.is_done:
        decision = player.get_decision(dealer)
        print(f'decision: {decision}')
        if decision == 'h':
            player.hit_me(deck)
        elif decision == 's':
            player.stand()
        elif decision == 'd':
            player.doubles()
        elif decision == 'y':       # Split case
            player.hit_me(deck)

    # Dealer decision loop
    if player.hand.value < 21:
        while not dealer.is_done:
            decision = dealer.get_decision()
            if decision == 'hit':
                dealer.hit_me(deck)
            elif decision == 'stand':
                dealer.stand()

    # Check for busts
    if player.hand.value > 21:
        player.goes_bust()
    elif dealer.hand.value > 21:
        dealer.goes_bust()
        player.round_outcome(win=True)

    # Check for blackjack
    elif player.hand.value == 21 and len(player.hand.cards) == 2:
        player.gets_blackjack()

    # Compare raw hand values
    elif player.hand.value > dealer.hand.value:
        player.round_outcome(win=True)
    elif player.hand.value < dealer.hand.value:
        player.round_outcome(loss=True)
    else:
        player.round_outcome(draw=True)

    print('Player:', player.hand)
    print('Dealer:', dealer.hand)
    print(f'total earnings {player.total_earnings}')
    print('total bets:', player.total_bets)
    print('----------------------------------')

    # Clear hands:
    dealer.hand = Hand()
    player.hand = Hand()

    # Reset dealer.is_done()
    dealer.is_done = False


if __name__ == '__main__':
    for i in range(10):
        main()
