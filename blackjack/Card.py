class Card(object):

    def __init__(self, rank, suit):

        # Set object fields
        self.rank = rank
        self.suit = suit

        # Set count_value for individual cards
        if self.rank in ['four', 'five', 'six']:
            self.count_value = 2
        elif self.rank in ['two', 'three', 'seven']:
            self.count_value = 1
        elif self.rank in ['eight', 'nine']:
            self.count_value = 0
        elif self.rank in ['ace']:
            self.count_value = -1
        # Account for ['ten','jack','queen','king']
        else:
            self.count_value = -2

        # Set card value
        rank_values = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
                       'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
                       'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}
        self.value = rank_values[self.rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __eq__(self, other):
        return self.rank == other.rank
