from player import player

#strategy based on https://www.blackjackapprenticeship.com/resources/blackjack-strategy-charts/

class basicAlpha(player):
    def __init__(self):
        player.__init__(self)
        #name the player so that we can tell what they are, for purposes of debugging
        self.name = 'Basic Alpha (No Double)'
        #what action to take depending on the dealer's up card, and the player's count
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
                ['n', 'n', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h'], #9
                ['n', 'n', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h'], #10
                ['n', 'n', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h'], #11
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

    def play(self, deck, dealer, table = None, catcher = None, trainMethod = None):
        while not self.isStaying():
            #get the table address to look at depending on player hand total, and dealer up card
            dAdd = dealer.getUpCard()
            pAdd = self.getCount()
            #play depending on strategy table
            prevCount = self.getCount()
            decision = None
            if self.strategyTable[pAdd][dAdd] is 's':
                self.stay()
                decision = 'stay'
            else:
                self.hit(deck)
                decision = 'hit'
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


