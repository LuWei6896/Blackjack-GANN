

class player(object):
    def __init__(self):
        self.upCards = []
        self.staying = False
        self.isCounting = False

    def reset(self):
        self.upCards = []
        self.staying = False
    
    def getCount(self):
        return sum( self.upCards )

    def play(self, deck):
        return self.getCount()

    def hit(self, deck):
        card = deck.dealCard() #pop first card
        self.upCards.append(card)
    
    def stay(self):
        self.staying = True

    def isCounting(self):
        return self.isCounting

    def initialDeal(self, deck):
        for(i in range(0, 2)):
            self.hit(deck)
