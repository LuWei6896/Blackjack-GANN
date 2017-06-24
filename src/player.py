import uuid 

basicBet = 1

class player(object):
    def __init__(self):
        #hand
        self.upCards = []

        #info to determine what player is going to do
        self.staying = False
        self.bust = False

        #for training networks
        self.isCounting = False
        self.name = 'basic player'
        self.id = str(uuid.uuid4())

        #money
        self.bet = basicBet

    def __str__(self):
        return self.name + ' [' + self.id + ']'

    def getID(self):
        return self.id

    def reset(self, mode = 'round'):
        self.upCards = []
        self.staying = False
        self.bust = False
        self.bet = basicBet
    
    def getCount(self):
        return sum( self.upCards )

    def play(self, deck, dealer):
        return self.getCount()

    def hit(self, deck):
        card = deck.dealCard() #pop first card
        self.upCards.append(card)
        if self.getCount() >= 21:
            self.staying = True
    
    def stay(self):
        self.staying = True
    
    def doubleBet(self):
        self.bet = self.bet * 2

    def doubleDown(self, deck):
        self.doubleBet() 
        self.hit(deck)
        self.stay()

    def isCounting(self):
        return self.isCounting

    def initialDeal(self, deck):
        for i in range(0, 2):
            self.hit(deck)

    def didBust(self):
        return self.bust

    def checkBust(self):
        if self.getCount() > 21:
            self.bust = True
            return True
        else:
            self.bust = False
            return False
    def isStaying(self):
        return self.staying
