

class histogram(object):
    def __init__(self):
        self.dct = {}

    def addPlayer(self, p):
        if p.getID() not in self.dct:
            self.dct[p.getID()] = { 
                    'wins': 0,
                    'losses': 0, 
                    'histogram': []
                    }

    def addPlayers(self, players):
        for p in players:
            self.addPlayer(p)


    def updateLosses(self, p, lossCount = 1):
        if p.getID() in self.dct:
            self.dct[p.getID()]['losses'] =  self.dct[p.getID()]['losses'] + lossCount
            hist = ['L'] * lossCount
            [self.dct[p.getID()]['histogram'].append(x) for x in hist]
        else:
            self.dct[p.getID()] = {
                    'wins': 0,
                    'losses': lossCount, 
                    'histogram': ['L'] * lossCount
                    }


    def updateWins(self, p, winCount = 1):
        if p.getID() in self.dct:
            self.dct[p.getID()]['wins'] =  self.dct[p.getID()]['wins'] + winCount
            hist = ['W'] * winCount
            [self.dct[p.getID()]['histogram'].append(x) for x in hist]
        else:
            self.dct[p.getID()] = {
                    'wins': winCount,
                    'losses': 0,
                    'histogram': ['W'] * winCount
                    }


    def getHistogram(self, p):
        if p.getID() in self.dct:
            return self.dct[p.getID()]['histogram']
        else:
            return None

    def getInfo(self, p):
        if p.getID() in self.dct:
            return self.dct[p.getID()]
        else:
            return None

