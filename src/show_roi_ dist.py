import pandas as pd
import matplotlib.pyplot as plt
from blackjack.deck import Deck
from entities.basic_strategy_player import BasicPlayer
from entities.dealer import Dealer
from main import init_round


def run_simulation(num_games, num_rounds_per_game):
    """
    Simulate a series of blackjack games and record game statistics.

    Args:
    - num_games (int): The number of blackjack games to simulate.
    - num_rounds_per_game (int): The number of rounds to play in each game.

    Returns:
    - pd.DataFrame: A DataFrame containing game statistics including earnings, bets, and ROI.
    """

    # Create a DataFrame to hold game stats
    game_stats = pd.DataFrame(
        columns=['Game', 'Total Earnings', 'Total Bets', 'ROI'])

    # Loop over the no. of games to simulate
    for game in range(num_games):
        deck = Deck(6)
        player = BasicPlayer("Player", card_counting=False)
        dealer = Dealer()

        # Play the specified no. of rounds per game
        for round_num in range(num_rounds_per_game):
            init_round(player, dealer, deck)

        # Calculate the ROI
        roi = player.total_earnings / \
            player.total_bets if player.total_bets != 0 else 0

        # Get new entry and add to DataFrame
        new_row = pd.DataFrame({'Game': [game + 1], 'Total Earnings': [player.total_earnings],
                               'Total Bets': [player.total_bets], 'ROI': [roi]})
        game_stats = pd.concat([game_stats, new_row], ignore_index=True)

    return game_stats


def plot_roi_distribution(game_stats):
    """
    Plot the distribution of Return on Investment (ROI) across multiple games.

    Args:
    - game_stats (pd.DataFrame): DataFrame containing game statistics.

    Returns:
    - None: Displays the ROI distribution plot.
    """

    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_facecolor('#262626')

    ax.hist(game_stats['ROI'], bins=20,
            color='dodgerblue', alpha=0.7, edgecolor='white')

    # Label axis
    ax.set_title('Distribution of Basic Strategy ROI Across 500 Games of 1000 Rounds Each',
                 fontsize=14, color='white')
    ax.set_xlabel('ROI', fontsize=12, color='white')
    ax.set_ylabel('Frequency', fontsize=12, color='white')

    # Grid-lines
    ax.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey')
    ax.tick_params(colors='white', which='both')

    # Mean Value
    mean_value = game_stats['ROI'].mean()
    ax.axvline(mean_value, color='red', linestyle='dashed', linewidth=2)

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
    num_games = 500
    num_rounds_per_game = 1000

    game_stats = run_simulation(num_games, num_rounds_per_game)
    print(game_stats)

    # Plot the ROI distribution
    plot_roi_distribution(game_stats)

    # Configure
    plt.style.use('dark_background')
    plt.tight_layout()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_facecolor('#262626')

    # Label axis
    ax.set_title('Title', fontsize=14, color='white')
    ax.set_xlabel('X-axis label', fontsize=12, color='white')
    ax.set_ylabel('Y-axis label', fontsize=12, color='white')

    # Grid-lines
    ax.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey')
    ax.tick_params(colors='white', which='both')
