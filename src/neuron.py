import numpy as np
import random
from util import util


class neuron(object):
    def __init__(self, name = None, weights = None):
        self.name = name
        self.weights = weights if weights else []
        self.inputNeurons = []
        self.outputNeurons = []
        self.sum = 0.0
        self.output = 0.0
        self.deriv = 0.0

    def connect(self, forward = None, backward = None):
        self.inputNeurons = backward if backward is not None else []
        self.weights = []
        for i in range(len(self.inputNeurons)): 
            self.weights.append(random.random())
        self.outputNeurons = forward if forward is not None else []

    def run(self, value = None, bias = None):
        if value is None:
            self.sum = 0.0
            self.output = 0.0
            for n, w in zip(self.inputNeurons, self.weights):
                self.sum = self.sum + ( w * n.output )
            self.sum = self.sum + bias
            #print 'bias', bias
            #print 'weights', self.weights
            self.output = self.activate()
        else:
            self.output = value

    def activate(self):
        v = 1 / (1 + np.exp( - self.sum ) )
        return v

    def activateDerivative(self):
        return self.output * ( 1 - self.output )

    def getWeightForNeuron(self, n):
        v = self.weights[ self.inputNeurons.index(n) ]
        #print 'weight for neuron', v
        return v 

    def train(self, lr, expected = None, noTrain = None):
        #print 'new neuron training'
        self.deriv = 0.0
        if expected is not None:
            self.deriv = -(expected - self.output) * self.activateDerivative()
            print 'error: ', self.error(expected)
        else:
            for nO in self.outputNeurons:
                self.deriv = self.deriv + (nO.getWeightForNeuron(self) * nO.deriv)
                #print 'update deriv =', self.deriv
            self.deriv *= self.activateDerivative()
        if noTrain is None: 
            for i, w in enumerate(self.weights):
                delt = (lr * self.deriv * self.inputNeurons[i].output) 
                self.weights[i] = w - delt
            #print self.name if self.name is not None else '', 'delta weight', delt 

    def error(self, expected):
        return .5 * (expected - self.output) ** 2
