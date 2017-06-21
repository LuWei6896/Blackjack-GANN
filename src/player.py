

class player(object):
    def __init__(self):
        self.upCards = []
        self.staying = False
        self.isCounting = False
        self.bust = False

    def reset(self, mode = 'round'):
        self.upCards = []
        self.staying = False
        self.bust = False
    
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
        for i in range(0, 2):
            self.hit(deck)
        print 'after initial deal, hand is ', self.getCount()

    def didBust(self):
        return self.bust

    def checkBust(self):
        if self.getCount() > 21:
            self.bust = True
            return True
        else:
            self.bust = False
            return False
