from basicAlpha import basicAlpha
import random


class basicDelta(basicAlpha):
    def __init__(self, riskFactor = 30):
        basicAlpha.__init__(self)
        #this one will just hit sometimes even if it is supposed to stay
        self.riskFactor = riskFactor
        #name for debugging/logging
        self.name = 'Basic Delta (Risky Basic Alpha)'

    def play(self, deck, dealer, table = None):
        while not self.isStaying():
            dAdd = dealer.getUpCard()
            pAdd = self.getCount()
            if self.strategyTable[pAdd][dAdd] is 's':
                #if our count is less than 17, and the player decides to be risky, hit
                if self.getCount() <= 17:
                    willHit = random.randint(1, 100)
                    if willHit <= self.riskFactor:
                        self.hit(deck)
                    else:
                        self.stay()
                else:    
                    self.stay()
            else:
                self.hit(deck)

        self.checkBust()
        return self.getCount()

