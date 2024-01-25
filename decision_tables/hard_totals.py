import pandas as pd


class HardTotals:

    data = {
        # Index
        'hard totals': [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4],
        # dealer.up_card.value < 3
        'two': ['s', 's', 's', 's', 's', 's', 's', 's', 's', 'h', 'd', 'd', 'h', 'h', 'h', 'h', 'h', 'h'],
        # 3 <= dealer.up_card.value < 4
        'three': ['s', 's', 's', 's', 's', 's', 's', 's', 's', 'h', 'd', 'd', 'd', 'h', 'h', 'h', 'h', 'h'],
        # 4 <= dealer.up_card.value < 7
        'four': ['s', 's', 's', 's', 's', 's', 's', 's', 's', 's', 'd', 'd', 'd', 'h', 'h', 'h', 'h', 'h'],
        'five': ['s', 's', 's', 's', 's', 's', 's', 's', 's', 's', 'd', 'd', 'd', 'h', 'h', 'h', 'h', 'h'],
        'six': ['s', 's', 's', 's', 's', 's', 's', 's', 's', 's', 'd', 'd', 'd', 'h', 'h', 'h', 'h', 'h'],
        # 7 <= dealer.up_card.value < 10
        'seven': ['s', 's', 's', 's', 's', 'h', 'h', 'h', 'h', 'h', 'd', 'd', 'h', 'h', 'h', 'h', 'h', 'h'],
        'eight': ['s', 's', 's', 's', 's', 'h', 'h', 'h', 'h', 'h', 'd', 'd', 'h', 'h', 'h', 'h', 'h', 'h'],
        'nine': ['s', 's', 's', 's', 's', 'h', 'h', 'h', 'h', 'h', 'd', 'd', 'h', 'h', 'h', 'h', 'h', 'h'],
        # dealer.up_card.value >= 10
        'ten': ['s', 's', 's', 's', 's', 'h', 'h', 'h', 'h', 'h', 'd', 'h', 'h', 'h', 'h', 'h', 'h', 'h'],
        'jack': ['s', 's', 's', 's', 's', 'h', 'h', 'h', 'h', 'h', 'd', 'h', 'h', 'h', 'h', 'h', 'h', 'h'],
        'queen': ['s', 's', 's', 's', 's', 'h', 'h', 'h', 'h', 'h', 'd', 'h', 'h', 'h', 'h', 'h', 'h', 'h'],
        'king': ['s', 's', 's', 's', 's', 'h', 'h', 'h', 'h', 'h', 'd', 'h', 'h', 'h', 'h', 'h', 'h', 'h'],
        'ace': ['s', 's', 's', 's', 's', 'h', 'h', 'h', 'h', 'h', 'd', 'h', 'h', 'h', 'h', 'h', 'h', 'h'],
    }

    # Create the DataFrame
    table = pd.DataFrame(data)

    # Set the first column ('hard totals') as the index of the DataFrame
    table.set_index('hard totals', inplace=True)


# Access the class attribute to get the DataFrame
hard_totals_df = HardTotals.df

print(hard_totals_df)
