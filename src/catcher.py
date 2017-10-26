'''
network inputs:
hilo count
ko count
hiopt1 count
hiopt2 count
halves count
omega2 count
red7 count
zen count
previous count
hit
stay
dealt card value
'''
class catcher(object):
    def __init__(self, network):
        self.network = network
        self.counters = []
        self.counts = {}
        self.values = None
        self.hst = None

    def addHst(self, h):
        self.hst = h

    def updateWrong(self, wrongCount = 1):
        self.hst.updateCatcherWrong(wrongCount)
    
    def updateRight(self, rightCount = 1):
        self.hst.updateCatcherRight(rightCount)

    def addCounter(self, counter):
        self.counters.append(counter)

    def getCounts(self):
        self.counts = {}
        for player in self.counters:
            self.counts[player.strategy] = player.getCount()

    def train(self, prevSum, hit, stay, expected, noTrain = None, catcher = None):
        self.getCounts()
        c = self.counts
        values = [ c['HiLo'], c['KO'], c['HiOpt1'], c['HiOpt2'], c['Halves'], c['Omega2'], c['Red7'], c['Zen'], prevSum, hit, stay]
        self.values = values 
        out = self.run(prevSum, hit, stay)
        
        self.network.train(values, expected, noTrain = noTrain, catcher = catcher)

    def run(self, prevSum, hit, stay):
        self.getCounts()
        c = self.counts #just so i don't have to type a million times
        values = [ c['HiLo'], c['KO'], c['HiOpt1'], c['HiOpt2'], c['Halves'], c['Omega2'], c['Red7'], c['Zen'], prevSum, hit, stay]
        self.values = values 
        return self.network.run(values)

    def getValues(self, prevSum, hit, stay):
        self.getCounts()
        c = self.counts
        values = [ c['HiLo'], c['KO'], c['HiOpt1'], c['HiOpt2'], c['Halves'], c['Omega2'], c['Red7'], c['Zen'], prevSum, hit, stay]
        return values
