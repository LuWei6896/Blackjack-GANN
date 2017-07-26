from counter import counter
class HiOpt1(counter):
    def __init__(self, netDict = None):
        counter.__init__(self, netDict = netDict)
        self.strategy = 'HiOpt1'
        self.name = self.strategy
        self.countMap = {
                '2': 0,
                '3': 1,
                '4': 1,
                '5': 1,
                '6': 1,
                '7': 0,
                '8': 0,
                '9': 0,
                '10': -1,
                '11': 0
               }
