
class Hand(object):

    def __init__(self):

        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        return ','.join(str(card) for card in self.cards)
