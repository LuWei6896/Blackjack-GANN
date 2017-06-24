from counter import counter


class HiLo(counter):
    def __init__(self):
        counter.__init__(self)
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


    def play(self, deck, dealer, table): 
        while not self.isStaying():
            c = self.getCount(dealer, table)

