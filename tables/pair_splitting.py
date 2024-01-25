import pandas as pd


class PairSplitting(object):

    data = {
        # Doubling after split is allowed
        'pair': ['ace', 'king', 'queen', 'jack', 'ten', 'nine', 'eight', 'seven', 'six', 'five', 'four', 'three', 'two'],
        'two': ['y', 'n', 'n', 'n', 'n', 'y', 'y', 'y', 'y', 'n', 'n', 'y', 'y'],
        'three': ['y', 'n', 'n', 'n', 'n', 'y', 'y', 'y', 'y', 'n', 'n', 'y', 'y'],
        'four': ['y', 'n', 'n', 'n', 'n', 'y', 'y', 'y', 'y', 'n', 'n', 'y', 'y'],
        'five': ['y', 'n', 'n', 'n', 'n', 'y', 'y', 'y', 'y', 'n', 'y', 'y', 'y'],
        'six': ['y', 'n', 'n', 'n', 'n', 'y', 'y', 'y', 'y', 'n', 'y', 'y', 'y'],
        'seven': ['y', 'n', 'n', 'n', 'n', 'n', 'y', 'y', 'n', 'n', 'n', 'y', 'y'],
        'eight': ['y', 'n', 'n', 'n', 'n', 'y', 'y', 'n', 'n', 'n', 'n', 'n', 'n'],
        'nine': ['y', 'n', 'n', 'n', 'n', 'y', 'y', 'n', 'n', 'n', 'n', 'n', 'n'],
        'ten': ['y', 'n', 'n', 'n', 'n', 'n', 'y', 'n', 'n', 'n', 'n', 'n', 'n'],
        'jack': ['y', 'n', 'n', 'n', 'n', 'n', 'y', 'n', 'n', 'n', 'n', 'n', 'n'],
        'queen': ['y', 'n', 'n', 'n', 'n', 'n', 'y', 'n', 'n', 'n', 'n', 'n', 'n'],
        'king': ['y', 'n', 'n', 'n', 'n', 'n', 'y', 'n', 'n', 'n', 'n', 'n', 'n'],
        'ace': ['y', 'n', 'n', 'n', 'n', 'n', 'y', 'n', 'n', 'n', 'n', 'n', 'n'],
    }

    # Create the DataFrame
    table = pd.DataFrame(data)

    # Set the first column ('soft totals') as the index
    table.set_index('pairs', inplace=True)


# # Test
pair_splitting_df = PairSplitting.table
print(pair_splitting_df)
