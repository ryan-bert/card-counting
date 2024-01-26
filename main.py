from blackjack.deck import Deck
from blackjack.hand import Hand
from entities.basic_strategy_player import BasicPlayer
from entities.dealer import Dealer
from copy import deepcopy


def init_round(player, dealer, deck):

    # Create dummy-player variable (for splitting)
    dummy = None

    # Draw 2 cards and place bet
    player.start_round(deck, bet=100)
    dealer.start_round(deck)

    # Check for split
    decision = player.get_split_decision(dealer)
    if decision == 'y':
        # Player & dummy must have 2 cards
        print('Split!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print(f'checkpoint1: {player.hand.value}')

        dummy = BasicPlayer()
        print(f'currentbet1: {player.current_bet}')
        print(f'totalbet1: {player.total_bets}')

        # Do a manual hit_me()
        card = player.hand.cards.pop()
        player.hand.value -= card.value
        dummy.hand.cards.append(card)
        dummy.hand.value += card.value

        # since start_round is never used
        dummy.current_bet = player.current_bet
        dummy.total_bets += player.current_bet

        dummy.hit_me(deck)
        print(f'currentbet2: {player.current_bet}')
        print(f'totalbet2: {player.total_bets}')
        player.hit_me(deck)
        print(f'currentbet3: {player.current_bet}')
        print(f'totalbet3: {player.total_bets}')
        # Duplicate
        # copied_deck = deepcopy(deck)
        round(dummy, dealer, deck)
    # no split
    round(player, dealer, deck)
    # print(f'total bets: {player.total_bets}')
    player.add_totals(dummy)
    # print(f'total bets: {player.total_bets}')


def round(player, dealer, deck):
    print(f'currentbetvv: {player.current_bet}')
    print(f'totalbetvv: {player.total_bets}')

    # Player decision loop (split NOT included)
    while not player.is_done:
        print(f'currentbetww: {player.current_bet}')
        print(f'totalbetww: {player.total_bets}')
        decision = player.get_other_decision(dealer)
        print(f'currentbetxx: {player.current_bet}')
        print(f'totalbetxx: {player.total_bets}')
        print(f'decision: {decision}')
        if decision == 'h':
            player.hit_me(deck)
        elif decision == 's':
            player.stand()
        elif decision == 'd':
            player.hit_me(deck)
            player.doubles()
    print(f'currentbet4: {player.current_bet}')
    print(f'totalbet4: {player.total_bets}')
    # Dealer decision loop
    if player.hand.value < 21:
        while not dealer.is_done:
            decision = dealer.get_decision()
            if decision == 'hit':
                dealer.hit_me(deck)
            elif decision == 'stand':
                dealer.stand()
        print(f'currentbet1: {player.current_bet}')
        print(f'totalbet1: {player.total_bets}')
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

    # Print end-of-round info
    print('Player:', player.hand)
    print('Dealer:', dealer.hand)
    print(f'total earnings {player.total_earnings}')
    print('total bets:', player.total_bets)
    print('--------------------------------------')

    # Clear hands:
    dealer.hand = Hand()
    player.hand = Hand()

    # Reset dealer.is_done()
    dealer.is_done = False


if __name__ == '__main__':
    # Initialize game objects for the entire game session
    deck = Deck(4)
    player = BasicPlayer()
    dealer = Dealer()

    # Number of rounds to play
    num_rounds = 100  # Change this to play more or fewer rounds

    # Play multiple rounds
    for i in range(num_rounds):
        print(f"Round {i + 1}")
        init_round(player, dealer, deck)

        # Optionally shuffle the deck here if you're not using a new deck each round
        # deck.shuffle()

        # Reset player and dealer for the next round if necessary
        # player.reset()
        # dealer.reset()

        # Print round summary or update round statistics here (if needed)

    # Print game summary (total earnings, win rate, etc.) after all rounds are completed
    print("Game Summary")
    print(f'Total earnings {player.total_earnings}',
          f'Total bets {player.total_bets}',
          f'Ratio: {player.total_earnings/player.total_bets if player.total_bets != 0 else "N/A"}')
    print(
        f'Win rate: {player.wins/player.rounds if player.rounds != 0 else "N/A"}')
