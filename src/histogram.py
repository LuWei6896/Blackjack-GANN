
#represent histogram for wins and losses for every player
class histogram(object):
    def __init__(self):
        self.dct = {}
        self.catcherHst = {
                'right': 0,
                'wrong': 0,
                'histogram': [],
                'count': 0
                }

            
    #add a player to track
    def addPlayer(self, p):
        if p.getID() not in self.dct:
            self.dct[p.getID()] = { 
                    'wins': 0,
                    'losses': 0, 
                    'ties': 0,
                    'histogram': []
                    }
    #add multiple players to track
    def addPlayers(self, players):
        for p in players:
            self.addPlayer(p)

    #update the loss count for a player
    def updateLosses(self, p, lossCount = 1):
        if p.getID() in self.dct:
            self.dct[p.getID()]['losses'] =  self.dct[p.getID()]['losses'] + lossCount
            hist = ['L'] * lossCount
            [self.dct[p.getID()]['histogram'].append(x) for x in hist]
        else:
            self.dct[p.getID()] = {
                    'wins': 0,
                    'losses': lossCount, 
                    'ties': 0,
                    'histogram': ['L'] * lossCount
                    }

    #update the win count for a player
    def updateWins(self, p, winCount = 1):
        if p.getID() in self.dct:
            self.dct[p.getID()]['wins'] =  self.dct[p.getID()]['wins'] + winCount
            hist = ['W'] * winCount
            [self.dct[p.getID()]['histogram'].append(x) for x in hist]
        else:
            self.dct[p.getID()] = {
                    'wins': winCount,
                    'losses': 0,
                    'ties': 0,
                    'histogram': ['W'] * winCount
                    }
    #update the tie count for a player
    def updateTies(self, p, tieCount = 1):
        if p.getID() in self.dct:
            self.dct[p.getID()]['ties'] =  self.dct[p.getID()]['ties'] + tieCount
            hist = ['T'] * tieCount
            [self.dct[p.getID()]['histogram'].append(x) for x in hist]
        else:
            self.dct[p.getID()] = {
                    'wins': 0,
                    'losses': 0,
                    'ties': tieCount,
                    'histogram': ['T'] * tieCount
                    }


    def updateCatcherRight(self, rightCount = 1):
        self.catcherHst['right'] = self.catcherHst['right'] + rightCount
        h = ['W'] * rightCount
        [self.catcherHst['histogram'].append(x) for x in h]
        self.catcherHst['count'] = self.catcherHst['count'] + rightCount

    def updateCatcherWrong(self, wrongCount = 1):
        self.catcherHst['wrong'] = self.catcherHst['wrong'] + wrongCount
        h = ['L'] * wrongCount
        [self.catcherHst['histogram'].append(x) for x in h]
        self.catcherHst['count'] = self.catcherHst['count'] + wrongCount

    
    #get the histogram for one player
    def getHistogram(self, p):
        if p.getID() in self.dct:
            return self.dct[p.getID()]['histogram']
        else:
            return None

    def getCatcherHistogram(self):
        return self.catcherHst['histogram']

    def getCatcherInfo(self):
        return self.catcherHst
    
    #return all info for one player
    def getInfo(self, p):
        if p.getID() in self.dct:
            return self.dct[p.getID()]
        else:
            return None

