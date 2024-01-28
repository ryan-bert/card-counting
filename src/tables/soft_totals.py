import pandas as pd


class SoftTotals:

    data = {

        'soft totals': [21, 20, 19, 18, 17, 16, 15, 14, 13, 12],
        'two': ['s', 's', 's', 'd', 'h', 'h', 'h', 'h', 'h', 'h'],
        'three': ['s', 's', 's', 'd', 'd', 'h', 'h', 'h', 'h', 'h'],
        'four': ['s', 's', 's', 'd', 'd', 'd', 'd', 'h', 'h', 'h'],
        'five': ['s', 's', 's', 'd', 'd', 'd', 'd', 'd', 'd', 'h'],
        'six': ['s', 's', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'h'],
        'seven': ['s', 's', 's', 's', 'h', 'h', 'h', 'h', 'h', 'h'],
        'eight': ['s', 's', 's', 's', 'h', 'h', 'h', 'h', 'h', 'h'],
        'nine': ['s', 's', 's', 'h', 'h', 'h', 'h', 'h', 'h', 'h'],
        'ten': ['s', 's', 's', 'h', 'h', 'h', 'h', 'h', 'h', 'h'],
        'jack': ['s', 's', 's', 'h', 'h', 'h', 'h', 'h', 'h', 'h'],
        'queen': ['s', 's', 's', 'h', 'h', 'h', 'h', 'h', 'h', 'h'],
        'king': ['s', 's', 's', 'h', 'h', 'h', 'h', 'h', 'h', 'h'],
        'ace': ['s', 's', 's', 'h', 'h', 'h', 'h', 'h', 'h', 'h'],
    }

    # Create the DataFrame
    table = pd.DataFrame(data)

    # Set the first column ('soft totals') as the index
    table.set_index('soft totals', inplace=True)
