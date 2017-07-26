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

    def addCounter(self, counter):
        self.counters.append(counter)

    def getCounts(self):
        self.counts = {}
        for player in self.counters:
            self.counts[player.strategy] = player.getCount()

    def train(self, prevSum, move, dealtVal, expected, noTrain = None, catcher = None):
        self.getCounts()
        c = self.counts
        if move is 1:
            values = [ c['HiLo'], c['KO'], c['HiOpt1'], c['HiOpt2'], c['Halves'], c['Omega2'], c['Red7'], c['Zen'], prevSum, 1.0, 0.0, dealtVal]
            self.values = values 
        else:
            values = [ c['HiLo'], c['KO'], c['HiOpt1'], c['HiOpt2'], c['Halves'], c['Omega2'], c['Red7'], c['Zen'], prevSum, 0.0, 1.0, dealtVal]
            self.values = values 
        self.network.train(values, expected, noTrain = noTrain, catcher = catcher)

    def run(self, prevSum, move, dealtVal):
        self.getCounts()
        c = self.counts #just so i don't have to type a million times
        if move is 1:
            values = [ c['HiLo'], c['KO'], c['HiOpt1'], c['HiOpt2'], c['Halves'], c['Omega2'], c['Red7'], c['Zen'], prevSum, 1.0, 0.0, dealtVal]
            self.values = values 
        else:
            values = [ c['HiLo'], c['KO'], c['HiOpt1'], c['HiOpt2'], c['Halves'], c['Omega2'], c['Red7'], c['Zen'], prevSum, 0.0, 1.0, dealtVal]
            self.values = values 
        return self.network.run(values)
