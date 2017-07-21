import numpy as np
import random
from util import util

#represent a basic neuron in a neural network
class neuron(object):
    def __init__(self, name = None, weights = None):
        #optional neuron name
        self.name = name
        #weights for input neurons
        self.weights = weights if weights else []
        #neurons we input from 
        self.inputNeurons = []
        #neurons we output to 
        self.outputNeurons = []
        #stores sum of inputs
        self.sum = 0.0
        self.output = 0.0
        #used to store the PD in respect to this neuron
        self.deriv = 0.0

    #set the inputs and outputs of this neuron
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
            #sum up the outputs
            for n, w in zip(self.inputNeurons, self.weights):
                self.sum = self.sum + ( w * n.output )
            self.sum = self.sum + bias
            #activate with sigmoid
            self.output = self.activate()
        #if input neuron, just set the output value
        else:
            self.output = value

    #sigmoid
    def activate(self):
        v = 1 / (1 + np.exp( - self.sum ) )
        return v

    #derivative of sigmoid
    def activateDerivative(self):
        return self.output * ( 1 - self.output )

    #used to get the weight for a neuron that inputs to this neuron
    def getWeightForNeuron(self, n):
        v = self.weights[ self.inputNeurons.index(n) ]
        return v 

    def train(self, lr, expected = None, noTrain = None, catcherDeltas = None): #delta = None
        self.deriv = 0.0
        #this is for the output layer. if there are expected outputs we know we are in the final layer and we do a different method of training
        if expected is not None:
            self.deriv = -(expected - self.output) * self.activateDerivative()
            #print 'error: ', self.error(expected)
        
        #if there are deltas from the catcher network, we treat the network like it connects right onto our own network and set our derivative accordingly
        elif catcherDeltas is not None:
            self.deriv = catcherDeltas[self.name]
        #we are just in regular training on a hidden neuron
        else:
            for nO in self.outputNeurons:
                #get the weights coming into this neuron, as well as the partial derivatives of the previous layer
                self.deriv = self.deriv + (nO.getWeightForNeuron(self) * nO.deriv)
            #KYLE DON'T DELETE THIS LINE
            #multiply by our activation derivative to get the error in respect to the input of this neuron
            self.deriv *= self.activateDerivative()
        #if we just want to get the deltas to pass along, we wont train
        if noTrain is None: 
            #for every weight, update it 
            for i, w in enumerate(self.weights):
                #get the change in error in respect to this specific weight
                delt = (lr * self.deriv * self.inputNeurons[i].output) 
                self.weights[i] = w - delt

    #return squared error 1/2 ( exp - out)^2
    def error(self, expected):
        return .5 * (expected - self.output) ** 2
