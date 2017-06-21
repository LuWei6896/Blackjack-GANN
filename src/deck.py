import random

class deck(object):
    def __init__(self):
        self.cards = None
        self.numDecks = 3
        self.__populateDeck()
        self.shuffle()

    def __populateDeck(self):
        vals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        newDeck = []
        for x in range(0, self.numDecks):
            for i in vals:
                v = [i] * 4
                [newDeck.append(x) for x in v]
        self.cards = newDeck

    def shuffle(self, numTimes = 4):
        for i in range(0, numTimes):
            random.shuffle( self.cards )

    def dealCard(self):
        return self.cards.pop(0)

    def resetDeck(self):
        self.__populateDeck()

    def numCards(self):
        return len( self.cards )

    def __str__(self):
        return ' '.join(str(e) for e in self.cards)
