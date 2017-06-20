import random

class deck(object):
    def __init__(self):
        self.cards = None

    def __populateDeck(self):
        vals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        newDeck = []
        for i in vals:
            v = [i] * 4
            [newDeck.append(x) for x in v]
        self.cards = newDeck

     def shuffle(self, numTimes = 4):
         for i in range(0, numTimes):
             random.shuffle( self.cards )

    def dealCard(self):
        return self.cards.pop(0)
