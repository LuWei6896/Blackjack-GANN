from basicAlpha import basicAlpha
import random


class basicDelta(basicAlpha):
    def __init__(self, riskFactor = 30):
        basicAlpha.__init__(self)
        #this one will just hit sometimes even if it is supposed to stay
        self.riskFactor = riskFactor
        #name for debugging/logging
        self.name = 'Basic Delta (Risky Basic Alpha)'

    def play(self, deck, dealer, table = None, catcher = None, trainMethod = None):
        while not self.isStaying():
            dAdd = dealer.getUpCard()
            pAdd = self.getCount()
            prevCount = self.getCount()
            decision = None
            if self.strategyTable[pAdd][dAdd] is 's':
                #if our count is less than 17, and the player decides to be risky, hit
                if self.getCount() <= 17:
                    willHit = random.randint(1, 100)
                    if willHit <= self.riskFactor:
                        self.hit(deck)
                        decision = 'hit'
                    else:
                        self.stay()
                        decision = 'stay'
                else:    
                    self.stay()
                    decision = 'stay'
            else:
                self.hit(deck)
                decision = 'stay'
            if catcher is not None:
                dealtCard = self.getCount() - prevCount
                move = None
                if decision is 'hit':
                    move = 1
                else:
                    move = 0


                out = int(round( catcher.run(prevCount, move, 0 if move is 1 else 1)['output'] ))
                diff = abs( out - int(self.isCounting) )
                if diff == 0:
                    catcher.updateRight()
                else:
                    catcher.updateWrong()

                catcher.train(prevCount, move, 0 if move is 1 else 1, [int(self.isCounting)])

        self.checkBust()
        return self.getCount()

