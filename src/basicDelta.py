from basicAlpha import basicAlpha
import random


class basicDelta(basicAlpha):
    def __init__(self, riskFactor = 30):
        basicAlpha.__init__(self)
        self.riskFactor = riskFactor
        self.name = 'Basic Delta (Risky Basic Alpha)'

    def play(self, deck, dealer):
        while not self.isStaying():
            dAdd = dealer.getUpCard()
            pAdd = self.getCount()
            if self.strategyTable[pAdd][dAdd] is 's':
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

