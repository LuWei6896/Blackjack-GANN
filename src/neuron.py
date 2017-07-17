import numpy as np

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
        return 1 / (1 + np.exp(-val) )

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
        self.getInputs()
        for i, w in self.inputValues, self.weights:
            self.intermediateValue = self.intermediateValue + (i * w) + bias

    #return the output 
    def getOutput(self):
        return self.outputValue

    #run the neuron
    def run(self, bias = None, inputValue = None):#we have inputs here for the input layer neurons
        if inputValue is None:
            self.sum(bias)
            self.outputValue = self.activate( self.intermediateValue )
        else:
            self.outputValue = inputValue
    
    #set the neurons inputting into neuron
    def setInputNeurons(self, pLayer):
        for n in pLayer.getNeurons():
            self.inputNeurons.append( n )

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


