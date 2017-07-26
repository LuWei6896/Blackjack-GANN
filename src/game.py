import random
from util import util
from deck import deck
from player import player
from dealer import dealer
from histogram import histogram

#TODO: make loss/win histogram for players
#runs games of blackjack
#blackjack has like 6 players per table so run many tables to train the catcher against many strategies
class game(object):
    def __init__(self):
        self.players = []
        #represents the tables of blackjack
        self.tables = {
            'first': [],
            'second': [],
            'third': []
        }
        #the dealers you have to beat at every table
        self.dealers = {
            'first': dealer(),
            'second': dealer(),
            'third': dealer()
        }
        #the deck for every table
        self.decks = {
            'first': deck(),
            'second': deck(),
            'third': deck()
        }
        #add the catcher once we create it, but for now it is nothing
        self.catcher = None
        #reseed deck if there is less than this many cards in the deck
        self.minDeckCount = 30
        
        #track win/loss history for all players
        self.hst = histogram()

    def playHand(self, table):
        #play all players
        for p in self.tables[table]:
            p.play(self.decks[table], self.dealers[table], table = self.tables[table], catcher = self.catcher, trainMethod = 'poker')
        
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
        #reset all players at a table after the hand is over
        for player in self.tables[table]:
            player.reset()

        self.dealers[table].reset()

    #mix up the players every once in a while
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
        #im just trying to finish this, so this is a lazy workaround, i am truly sorry i'll fix it later
        self.tables['first'].append(p)
        self.reseed()


    def addCatcher(self, catcher):
        self.catcher = catcher
    
    #once every table has gone through 10 complete decks, the game finishes
    def gameLoop(self, numDecks = 10):
        #track all players
        self.hst.addPlayers(self.players)
        #run all games
        for i in range(0, numDecks):
            print 'Playing game', i, 'on every table'
            self.playGame('first')
            self.playGame('second')
            self.playGame('third')
            self.reseed()
        #asses all games
        self.finalAssessment()

    #assess if players won game or not
    def assessGame(self, table):
        if self.dealers[table].didBust():
            for p in self.tables[table]:
                if not p.didBust(): # beat dealer
                    self.hst.updateWins(p)
                else: # did not beat dealer
                    self.hst.updateLosses(p)
        else:
            for p in self.tables[table]:
                if not p.didBust():
                    if p.getCount() > self.dealers[table].getCount(): # beat dealer
                        self.hst.updateWins(p)
                    elif p.getCount() == self.dealers[table].getCount(): #tie, even money
                        self.hst.updateTies(p)
                    else: # did not beat dealer
                        self.hst.updateLosses(p)
                else: # did not beat dealer
                    self.hst.updateLosses(p)
    
    #get the histogram info and log it o console
    def finalAssessment(self):
        for p in self.players:
            h = self.hst.getInfo(p)
            win, loss, tie = h['wins'], h['losses'], h['ties']
            winRatio =  100.0 * ( float( win ) /float( win + loss + tie ) )
            winRatio = round(winRatio, 1)
            print p.getID(), '(', p, ')', 'won:', win, 'games, lost:', loss, 'games, tied', tie, 'games with a win ratio of', ( str(winRatio) + '%')
