import pandas as pd
import matplotlib.pyplot as plt
from blackjack.deck import Deck
from entities.basic_strategy_player import BasicPlayer
from entities.dealer import Dealer
from main import init_round


def run_simulation(num_instances, num_rounds_per_instance):
    """
    Simulate a series of blackjack games and record game statistics.

    Args:
    - num_games (int): The number of blackjack games to simulate.
    - num_rounds_per_game (int): The number of rounds to play in each game.

    Returns:
    - pd.DataFrame: A DataFrame containing game statistics including earnings, bets, and ROI.
    """

    # Create a DataFrame to hold player stats over time
    player_stats = pd.DataFrame(
        columns=['Instance', 'Round', 'ROI'])

    # Loop over the no. of instances
    for instance in range(1, num_instances + 1):
        deck = Deck(6)
        player = BasicPlayer("Player", card_counting=False)
        dealer = Dealer()

        player_roi = []

        # Play the specified no. of rounds for this instance
        for round_num in range(1, num_rounds_per_instance + 1):
            init_round(player, dealer, deck)

            # Calculate player's ROI for this round and append to the list
            if player.total_bets != 0:
                roi = player.total_earnings / player.total_bets
            else:
                roi = None  # Set to None when total bets are zero

            player_roi.append(roi)

            # Create a DataFrame for this round's data
            round_data = pd.DataFrame({'Instance': [instance],
                                       'Round': [round_num],
                                       'ROI': [roi]})

            # Concatenate round data to player_stats
            player_stats = pd.concat(
                [player_stats, round_data], ignore_index=True)

    return player_stats


def plot_player_roi(player_stats, num_instances, num_rounds_per_instance):
    """
    Plot the ROI time series for each game instance.

    Args:
    - player_stats (pd.DataFrame): DataFrame containing player ROI data.
    - num_instances (int): The number of blackjack game instances.
    - num_rounds_per_instance (int): The number of rounds played in each game instance.

    Returns:
    - None: Displays the ROI time series plot.
    """
    # Configuration
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_facecolor('#262626')  # Slightly darker grey background color

    # Plot each player's ROI as a lines
    for instance in range(1, num_instances + 1):
        data = player_stats[(player_stats['Instance'] == instance) & (
            player_stats['Round'] <= num_rounds_per_instance)]

        # Filter out None values (where total bets = 0)
        filtered_data = data[data['ROI'].notna()]

        ax.plot(filtered_data['Round'], filtered_data['ROI'])

    # Label axis
    ax.set_title(f'Card Counting ROI Time Series for {num_instances} Instances of {num_rounds_per_instance} Rounds',
                 fontsize=14, color='white')
    ax.set_xlabel('Round', fontsize=12, color='white')
    ax.set_ylabel('ROI', fontsize=12, color='white')

    # Grid lines
    ax.grid(True, linestyle='--', linewidth=0.5, color='grey')
    ax.tick_params(colors='white', which='both')

    # Mean line
    mean_value = player_stats['ROI'].mean()
    ax.axhline(mean_value, color='red', linestyle='dashed', linewidth=2)

    # Mean value (top right corner)
    ax.text(0.95, 0.95, f'Mean: {mean_value:.4f}', transform=ax.transAxes, fontsize=12,
            color='white', horizontalalignment='right', verticalalignment='top')

    # No. of decks (top left corner)
    ax.text(0.05, 0.95, 'No. of Decks = 6', transform=ax.transAxes, fontsize=12, color='white',
            horizontalalignment='left', verticalalignment='top')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # Set simulation parameters
    num_instances = 10
    num_rounds_per_instance = 500

    player_stats = run_simulation(num_instances, num_rounds_per_instance)

    # Plot the ROIs
    plot_player_roi(
        player_stats, num_instances, num_rounds_per_instance)
