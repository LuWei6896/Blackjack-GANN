from layer input layer

class outputLayer(layer):
    def __init__(self, numOutputs, names = None):
        self.neurons = []
        if names is None:
            self.neurons = [ neuron() ] * numOutputs
        else:
            for name in names:
                self.neurons.append( neuron(name) )
                

    def run(self):
        for n in self.neurons:
            n.run()

    def getOutputs(self):
        lst = []
        for n in self.neurons:
            lst.append( (n.getName(), n.getOutput()) )
        return lst
