import numpy as np

class neuron(object):
    def __init__(self, name = None):
        self.inputs = []
        self.weights = []
        self.outputNeurons = []
        self.output = None
        self.name = name if name else None

    def connectBack(self, layer):
        for n in layer.neurons:
            self.inputs.append(n)
            self.weights.append(0.0)
    
    def connectForward(self, layer):
        for n in layer.neurons:
            self.outputNeurons.append(n)

    def run(self):

    def sum(self, inputs):
        ret = 0.0
        for i, j in inputs, self.weights:
            val = i * j
            ret = ret + val
    
    def activate(self, val):
        return ( 1 / (1 + np.exp(-val) ) )
    
    def activateDerivative(self, val):
        return val * (1 - val)

    def getInputs(self): 
        ret = []
        for n in self.inputs:
            ret.append( n.getOutput() )

    def getOutput(self):
        return self.output

    def getName(self):
        return self.name if self.name else None
