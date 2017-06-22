import random
from util import util
from deck import deck
from player import player
from dealer import dealer

class game(object):
    def __init__(self):
        self.players = []
        self.tables = {
            'first': [],
            'second': [],
            'third': []
        }

        self.dealers = {
            'first': dealer(),
            'second': dealer(),
            'third': dealer()
        }

        self.decks = {
            'first': deck(),
            'second': deck(),
            'third': deck()
        }
        self.catcher = None

        self.minDeckCount = 20
        self.win = 0
        self.loss = 0

    def playHand(self, table):
        #play all players
        for player in self.tables[table]:
            player.play(self.decks[table], self.dealers[table])
        
        #play dealer last
        self.dealers[table].play(self.decks[table])
        self.assessGame(table)

    def playGame(self, table):

        while self.decks[table].numCards() >= self.minDeckCount:
            #deal the initial hand to everyone
            for player in self.tables[table]:
                player.initialDeal(self.decks[table])
            self.dealers[table].initialDeal(self.decks[table])
            #let all players play a hand of blackjack 
            self.playHand(table)
            self.resetHand(table)

    def resetHand(self, table):
        for player in self.tables[table]:
            player.reset()

        self.dealers[table].reset()


    def shufflePlayerOrder(self):
        random.shuffle(self.players)
    
    #called when one deck gets too shallow
    #mix up tables and reset all players and decks, so network gets realistic blackjack experience
    def reseed(self):
        #get all of the players again, with their updated networks
        p1, p2, p3 = self.tables['first'], self.tables['second'], self.tables['third']
        self.players = p1 + p2 + p3 #fuck python and not having references and stuff
        
        #reset all players
        for player in self.players:
            player.reset()

        for table in self.dealers:
            self.dealers[table].reset()


        #shuffle the player order so that networks learn to deal with being in different positions        
        self.shufflePlayerOrder()
        #split players into three tables
        playerSplit = util.sliceList(self.players, 3)
        #assign players to tables
        self.tables['first'] = playerSplit[0]
        self.tables['second'] = playerSplit[1]
        self.tables['third'] = playerSplit[2]
        
        #reset the deck at every table
        self.decks['first'].resetDeck()
        self.decks['second'].resetDeck()
        self.decks['third'].resetDeck()
        
        

    def addPlayer(self, p):
        #self.players.append(p)
        #TODO: uncomment above. This is just rigged for testing
        self.tables['first'].append(p)
    
    #once every table has gone through 100 complete decks, the game finishes
    def gameLoop(self, numDecks = 10):
        for i in range(0, numDecks):
            print 'playing deck ', i
            self.playGame('first')
            self.reseed()
            print ''

        print 'won: ', self.win
        print 'lost: ', self.loss
            #self.playGame('first')
            #self.playGame('second')
            #self.playGame('third')


    def assessGame(self, table):
        if self.dealers[table].didBust():
            for p in self.tables[table]:
                if not p.didBust():
                    print p, ' beat dealer'
                    self.win = self.win + 1
                else:
                    print p, ' did not beat dealer'
                    self.loss = self.loss + 1
        else:
            for p in self.tables[table]:
                if not p.didBust():
                    if p.getCount() > self.dealers[table].getCount():
                        print p, ' beat dealer'
                        self.win = self.win + 1
                    else:
                        print p, ' did not beat dealer'
                        self.loss = self.loss + 1
                else:
                    print p, ' did not beat dealer'
                    self.loss = self.loss + 1

