'''
this is a card counting network that uses the basic Hi-Lo counting strategy

'''
from counter import counter


class HiLo(counter):
    def __init__(self, netDict = None):
        counter.__init__(self, netDict = netDict)
        #this maps the cards to their respective count values
        self.strategy = 'HiLo'
        self.name = self.strategy
        self.countMap = {
                '2': 1,
                '3': 1,
                '4': 1,
                '5': 1,
                '6': 1,
                '7': 0,
                '8': 0,
                '9': 0,
                '10': -1,
                '11': -1
               }

