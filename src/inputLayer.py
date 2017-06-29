from layer import layer
from inputNeuron import inputNeuron

class inputLayer(layer):
    def __init__(self, numInputs):
        self.neurons = [ inputNeuron() ] * numInpts
    
    def run(self, inputs):
        for i, n in inputs, self.neurons:
            n.run(i)

