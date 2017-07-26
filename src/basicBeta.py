from player import player

#https://www.blackjackinfo.com/blackjack-basic-strategy-engine/

class basicBeta(player):
    def __init__(self):
        player.__init__(self)
        #name for debugging/logging purposes
        self.name = 'Basic Beta (Double)'
        #strategy table. Same as basic alpha, but with doubling as well
        self.strategyTable = [
                  #0  1   2   3   4   5   6   7   8   9   10  A
                ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'], #0
                ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'], #1
                ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'], #2
                ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'], #3
                ['n', 'n', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h'], #4
                ['n', 'n', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h'], #5
                ['n', 'n', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h'], #6
                ['n', 'n', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h'], #7
                ['n', 'n', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h'], #8
                ['n', 'n', 'h', 'd', 'd', 'd', 'd', 'h', 'h', 'h', 'h', 'h'], #9
                ['n', 'n', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'h', 'h'], #10
                ['n', 'n', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd'], #11
                ['n', 'n', 'h', 'h', 's', 's', 's', 'h', 'h', 'h', 'h', 'h'], #12
                ['n', 'n', 's', 's', 's', 's', 's', 'h', 'h', 'h', 'h', 'h'], #13
                ['n', 'n', 's', 's', 's', 's', 's', 'h', 'h', 'h', 'h', 'h'], #14
                ['n', 'n', 's', 's', 's', 's', 's', 'h', 'h', 'h', 'h', 'h'], #15
                ['n', 'n', 's', 's', 's', 's', 's', 'h', 'h', 'h', 'h', 'h'], #16
                ['n', 'n', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's'], #17
                ['n', 'n', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's'], #18
                ['n', 'n', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's'], #19
                ['n', 'n', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's'], #20
                ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']#21
            ]


    def play(self,  deck,  dealer, table = None, catcher = None, trainMethod = None):
        while not self.isStaying():
            #get table addresses 
            dAdd = dealer.getUpCard()
            pAdd = self.getCount()
            #take action depending on address
            prevCount = self.getCount()
            decision = None
            if self.strategyTable[pAdd][dAdd] is 's':
                self.stay()
                decision = 'stay'
            elif self.strategyTable[pAdd][dAdd] is 'h':
                self.hit(deck)
                decision = 'hit'
            elif self.strategyTable[pAdd][dAdd] is 'd':
                #you can only double down on your first hit
                if len(self.upCards) is 2:
                    self.doubleDown(deck)
                    decision = 'hit'
                else:
                    self.hit(deck)
                    decision = 'hit'
            else:
                pass
            if catcher is not None: 
                dealtCard = self.getCount() - prevCount
                move = None
                if decision is 'hit':
                    move = 1
                else:
                    move = 0
                catcher.train(prevCount, move, dealtCard, [int(self.isCounting)])

        self.checkBust()
        return self.getCount()


