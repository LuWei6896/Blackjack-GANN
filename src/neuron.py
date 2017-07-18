import numpy as np
import random
from util import util

#basic neuron for a neural network
class neuron(object):
    def __init__(self, name = None):
        #name the neuron, for outputs/inputs
        self.name = name if name is not None else None
        #list of neurons that input to this one
        self.inputNeurons = []
        #list of neurons that this outputs to
        self.outputNeurons = []
        #store values input into neuron, for easy training
        self.inputValues = []
        #weights assigned for every input neuron
        self.weights = []
        #delta weights that we will add to weights at end of training
        self.weightDeltas = []
        #output value
        self.outputValue = 0.0
        #sum of all inputs * weights + bias
        self.intermediateValue = 0.0
        #the derivative of everything up to this for backpropogation
        self.deriv = 0.0

    #get the name of the neuron
    def getName(self):
        return self.name if self.name is not None else None
    
    #sigmpoid function
    def activate(self, val):
        v = 1 / (1 + np.exp(-val) )
        #print 'neuron activation:', v
        return v

    #sigmoid derivative
    def activateDerivative(self):
        return self.outputValue * (1.0 - self.outputValue)

    #get all inputs from neurons in previous layer
    def getInputs(self):
        self.inputValues = []
        for n in self.inputNeurons:
            self.inputValues.append( n.getOutput() )

    #sum up inputs * weights + bias
    def sum(self, bias):
        self.intermediateValue = 0.0
        self.getInputs()
        #print 'inputValues:', self.inputValues
        #print 'weights:', self.weights
        for i, w in zip(self.inputValues, self.weights):
            #print 'input', i, 'weight', w, 'bias', bias
            self.intermediateValue = self.intermediateValue + (i * w)
            self.intermediateValue = self.intermediateValue + bias

    #return the output 
    def getOutput(self):
        return self.outputValue

    #run the neuron
    def run(self, bias = None, inputValue = None):#we have inputs here for the input layer neurons
        #print 'NEURON'
        if inputValue is None:
            self.sum(bias)
            #print 'sum of inputs', self.intermediateValue
            self.outputValue = self.activate( self.intermediateValue )
            #print 'output value', self.outputValue
        else:
            self.outputValue = inputValue
    
    #set the neurons inputting into neuron
    def setInputNeurons(self, pLayer):
        for n in pLayer.getNeurons():
            self.inputNeurons.append( n )
            self.weights.append( random.random() )
            self.weightDeltas.append( 0.0 )

    #set neurons that this one outputs to 
    def setOutputNeurons(self, nLayer):
        for n in nLayer.getNeurons():
            self.outputNeurons.append( n )

    def connect(self, pLayer = None, nLayer = None):
        if pLayer is not None:
            self.setInputNeurons(pLayer)
        if nLayer is not None:
            self.setOutputNeurons(nLayer)

    def getOutputNeurons(self):
        return self.outputNeurons

    def getInputNeurons(self):
        return self.inputNeurons
    
    def getWeightForPosition(self, pos):
        return self.weights[pos]
    
    def inputRun(self, value):
        #print 'INPUT NEURON'
        self.outputValue = value
        #print 'output value', self.outputValue

    def applyDeltas(self):
        for i, w in enumerate(self.weights):
            self.weights[i] = w - self.weightDeltas[i]
        for i in range(len(self.weightDeltas)):
            self.weightDeltas[i] = 0.0

    def getWeights(self):
        return self.weights

    def getWeightDeltas(self):
        return self.weightDeltas

    def train(self, expected, lr):
        if self.name is not None:
            self.deriv = -(expected[self.name] - self.getOutput()) * self.activateDerivative()
            print self.name, self.deriv
            print 'expected', expected[self.name]
            print 'outut', self.outputValue
            print 'activate deriv', self.activateDerivative()
        else:
            for nO in self.outputNeurons:
                self.updateDerivative(nO)
         
        for i, w in enumerate(self.weights):
            self.weights[i] = w - ( lr * self.inputNeurons[i].getOutput() * self.deriv)
        


    def updateDerivative(self, nO):
        self.deriv = self.deriv + (nO.deriv * util.getWeightFromNeuron(self, nO) * self.activateDerivative() )
