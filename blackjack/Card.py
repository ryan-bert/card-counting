class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

        # Set the count for a specific card (rank)
        if self.rank in ['four', 'five', 'six']:
            self.count = 2

        elif self.rank in ['two', 'three', 'seven']:
            self.count = 1

        elif self.rank in ['eight', 'nine']:
            self.count = 0

        elif self.rank in ['ace']:
            self.count = -1

        # Count for ['ten', jack', 'queen', 'king']
        else:
            self.count = -2

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def value(self):
        rank_values = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
                       'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
                       'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}

        return rank_values[self.rank]

    def __eq__(self, other):
        return self.value() == other.value()
