from player import player
from network import network


#template class for a card counting network
class counter(player):
    #initialize the player, potentially with a neural network
    def __init__(self, netDict = None):
        player.__init__(self)
        self.network = network(lr = netDict['lr'], inputs = netDict['inputs'], hidden = netDict['hidden'], outputs = netDict['outputs']) if netDict is not None else None
        self.count = None
        self.countMap = None
        self.isCounting = True
    
    #map cards to the count associated with it
    def setCountMap(self, cm):
        self.countMap = cm
   
    #get the information required to send to the network: the count on the table, the dealer's up card, and the total cards in the player's hand
    def getInfo(self, deck, dealer, table):
        count = self.getTableCount(deck)
        dealerUpCard = dealer.getUpCard()
        hand = self.getCount()
        return {'count': count, 'upCard': dealerUpCard, 'hand': hand}
    
    #play a hand of blackjack
    def play(self, deck, dealer, table, trainMethod = None, catcher = None):
        while not self.isStaying():
            #get the info to pass to the network
            info = self.getInfo(deck, dealer, table) 
            #format it into an array to pass in to the network
            arr = [info[val] for val in info]
            #run the network
            out = self.network.run(arr)
            #get  the primary decision made (this will be the name of the neuron that outputs the highest value)
            decision = network.getBestDecision(out)
            
            #track the hand value before card was dealt
            prevCount = self.getCount()
            #make the desired move
            if decision is 'hit':
                self.hit(deck)
            else:
                self.stay()
            #get the value of the card dealt to the player
            dealtCard  = self.getCount() - prevCount
            #check if we've busted, for use in training
            bust = self.checkBust()
            #determine if we should've hit or stayed based on whether or not we busted
            expected = None
            if not bust:
                #for some reason the stay neuron is first
                expected = [0, 1]
            else:
                expected = [1, 0]
            #train the network in one of a few ways 
            '''
            for training to play poker, we are simply teaching the networks how to play blackjack, and not worried about them getting caught cheating. The catcher network won't be trained against the moves made in this phase, because we don't want it to learn a million games of what isn't really card counting yet.
            For training to card count, we will train the networks not to get caught and also train the catcher to catch the networks 
            '''
            if trainMethod is not None:
                if trainMethod is 'poker': #just teaching the network how to play poker, don't run against catcher, maybe train catcher just to look at them playing poker
                    #use the values determined earlier for the expected move, and train the network to make the appropriate move
                    self.network.train(arr, expected)

                elif trainMethod is 'counting': #train both us and catcher against eachother 
                    #refer to document Project Notes to continue writing this
                    #train the network to make the appropriate move, also with respect to the catcher network
                    self.network.train(arr, expected, catcher = catcher)
                    #TODO: there should be a more pythonic way to do this
                    #move = 1 if decision is 'hit' else 0
                    #assign a numerical value to the move made by the network
                    move = None
                    if decision is 'hit':
                        move = 1
                    else:
                        move = 0
                    
                    #train the catcher network to recognize this player as card counting

                    num = catcher.run(prevCount, move, 0 if move is 1 else 1)['output']
                    out = int(round( num ))
                    diff = abs( out - int(self.isCounting) )
                    if diff == 0:
                        catcher.updateRight()
                    else:
                        catcher.updateWrong()

                    catcher.train(prevCount, move, 0 if move is 1 else 1, [int(self.isCounting)])
                    
        #we still need to tell the game whether or not we've busted            
        self.checkBust()
        return self.getCount()
            

    #get the count associated with cards on the table 
    def getTableCount(self, deck):
        count = 0.0
        arr = deck.getHistory()
        numCards = len(arr)
        numDecks = float(numCards) / 52.0
        #for every card present on the table, update the count that this network uses
        for card in arr:
            count += self.countMap[str(card)]
        #print 'for cards', arr, 'count is', count, 'for system', self.strategy
        return count/numDecks
