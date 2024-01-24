from blackjack.card import Card
from blackjack.deck import Deck
from players.dealer import Dealer
import pandas as pd


hard_totals_data = {
    '2': ['H', 'H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'H', 'S'],
    '3': ['H', 'H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'H', 'S'],
    '4': ['H', 'H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'H', 'S'],
    '5': ['H', 'H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'H', 'S'],
    '6': ['H', 'H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'S', 'S'],
    '7': ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S'],
    '8': ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S'],
    '9': ['H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S'],
    '10': ['H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S'],
    'A': ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S']
}

# Define the index for the DataFrame
# This represents the player's hand value
index = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

# Create the DataFrame
hard_totals_df = pd.DataFrame(hard_totals_data, index=index)

# Set the DataFrame column names to match the dealer's upcard
hard_totals_df.columns = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A']

print(hard_totals_df)
