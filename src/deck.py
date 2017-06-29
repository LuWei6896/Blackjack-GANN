import random

class deck(object):
    def __init__(self, numberOfDecks = 4):
        self.cards = None
        self.numDecks = numberOfDecks
        self.__populateDeck()
        self.shuffle()
        self.history = []
        self.hidden = []

    def __populateDeck(self):
        self.history = []
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

    def dealCard(self, holeCard = False):
        card = self.cards.pop(0)
        #we want to keep track of cards that have been dealt so that counters can get the whole table count
        #dealer hole card is hidden, so we can't let players know that
        #players can only take the dealer's hole card into account after it has been dealt
        if not holeCard:
            self.history.append(card)
        else:
            self.hidden.append(card)
        return card

    def addHiddenToHistory(self):
        [self.history.appen(x) for x in self.hidden]
        self.history = []

    def resetDeck(self):
        self.__populateDeck()
        self.shuffle()

    def numCards(self):
        return len( self.cards )

    def __str__(self):
        return ' '.join(str(e) for e in self.cards)
