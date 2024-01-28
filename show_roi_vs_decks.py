import pandas as pd
import matplotlib.pyplot as plt
from blackjack.deck import Deck
from entities.basic_strategy_player import BasicPlayer
from entities.dealer import Dealer
from main import init_round


def run_simulation(num_decks_list, num_games, num_rounds_per_game):
    """
    Simulate a series of blackjack games and record game statistics.

    Args:
    - num_games (int): The number of blackjack games to simulate.
    - num_rounds_per_game (int): The number of rounds to play in each game.

    Returns:
    - pd.DataFrame: A DataFrame containing game statistics including earnings, bets, and ROI.
    """
    # Create a DataFrame to hold average ROI data
    average_roi_data = pd.DataFrame(columns=['Num Decks', 'Average ROI'])

    for num_decks in num_decks_list:
        total_roi = 0

        # Simulate multiple games
        for _ in range(num_games):
            deck = Deck(num_decks)
            player = BasicPlayer("Player", card_counting=False)
            dealer = Dealer()

            # Play the specified number of rounds per game
            for _ in range(num_rounds_per_game):
                init_round(player, dealer, deck)

            # Calculate the ROI for current game
            roi = player.total_earnings / player.total_bets if player.total_bets != 0 else 0

            # Accumulate ROI
            total_roi += roi

        # Calculate the average ROI
        average_roi = total_roi / num_games

        # Append to the DataFrame using pd.concat
        average_roi_data = pd.concat([average_roi_data, pd.DataFrame({'Num Decks': [num_decks], 'Average ROI': [average_roi]})],
                                     ignore_index=True)

    return average_roi_data


def plot_average_roi(average_roi_data):
    """
    Plot the average ROI against the number of decks used.

    Args:
    - average_roi_data (pd.DataFrame): DataFrame containing average ROI data.

    Returns:
    - None: Displays the average ROI plot.
    """

    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_facecolor('#262626')  # Slightly darker grey background color

    # Plot average ROI vs. number of decks
    ax.plot(average_roi_data['Num Decks'], average_roi_data['Average ROI'])

    # Label axis
    ax.set_title(f'Avg. Card Counting ROI vs. No. of Decks for {num_games} Games of {num_rounds_per_game} Rounds Each',
                 fontsize=14, color='white')
    ax.set_xlabel('Number of Decks', fontsize=12, color='white')
    ax.set_ylabel('Average ROI', fontsize=12, color='white')

    # Grid lines
    ax.grid(True, linestyle='--', linewidth=0.5, color='grey')
    ax.tick_params(colors='white', which='both')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # Set simulation parameters
    num_games = 10
    num_rounds_per_game = 400
    num_decks_list = [1, 2, 3, 4, 5, 6, 8]

    average_roi_data = run_simulation(
        num_decks_list, num_games, num_rounds_per_game)

    # Plot the average ROI
    plot_average_roi(average_roi_data)
