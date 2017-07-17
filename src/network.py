from layer import layer
from neuron import neuron
from util import util

#basic neural network class
class network(object):
    def __init__(self):
        self.layers = []
        self.learningRate = 0.001

    '''
    expected is a dictionary with neuron names and expected outputs
    eg:
    {
        'hit': 1,
        'stay':0
    }
    '''
    #train the network given inputs, expected outputs, and an optional catcher netowkr for training the players
    def train(self, inputs, expected, catcher = None): 
        #run and store intermediate values
        self.run(inputs)
        #backpropogate
        for l in reversed(self.layers):
            for n in l.getNeurons():
                #if output layer, derivative is slightly different
                if l is self.layers[-1]:
                    n.deriv = -(expected[n.getName()] - n.getOutput())
                    n.deriv = n.deriv * ( n.activateDerivative() )
                else:
                    for nO in n.getOutputNeurons():
                        util.updateDerivative(n, nO) # (dOut/dnO)*(dnO/dn)*(dn/dnIn)
                c = 0
                for w, wd in n.weights, n.weightDeltas:
                    wd = wd + ( self.learningRate * n.inputs[count].getOutput() * n.deriv ) #lr * (dOut/dnIn) * (dnIn/dW)
                    c = c + 1

        if catcher is not None:
            retList = []
            for l in reversed(catcher.layers):
                for n in l:
                    if l is catcher.layers[-1]: 
                        n.deriv = - (0 - n.getOutput() ) * n.activateDerivative()
                    else:
                        for nO in n.getOutputNeurons():
                            util.updateDerivative(n, nO)
                        if l is catcher.layers[1]:
                            retList.append(n.deriv)
            for l in reversed( self.layers ):
                for n in l:
                    if l is self.layers[-1]:
                        if n.name is 'hit':
                            n.deriv = retList['hit']
                        elif n.name is 'stay':
                            n.deriv = retList['stay']
                        else:
                            pass
                        n.deriv = n.deriv * n.activateDerivative()
                    else:
                        for nO in n.getOutputNeurons():
                            util.updateDerivative(n, nO) # (dOut/dnO)*(dnO/dn)*(dn/dnIn)
                    c = 0
                    for w, wd in n.weights, n.weightDeltas:
                        wd = wd + ( self.learningRate * n.inputs[count].getOutput() * n.deriv ) #lr * (dOut/dnIn) * (dnIn/dW)
                        c = c + 1

                


    
    #run the network given inputs
    def run(self, inputs):
        for l in self.layers:
            l.run()
        out = []
        for n in self.layers[-1].getNeurons():
            out.append( (n.getName(), n.getOutput()) )
        return out
    
    #add a layer to the network
    def addLayer(self, l):
        self.layers.append(l)

    #add the final layer and connect everything
    def addOutputLayer(self, l):
        self.layers.append(l)
        self.connectLayers()

    #connect the neurons in every layer to the neurons in the previous and next layers
    def connectLayers(self):
        count = 0
        for l in self.layers:
            if l is self.layers[0]:
                l.connectLayer(pLayer = None, nLayer = self.layers[count + 1])
            elif l is self.layers[-1]:
                l.connectLayer(pLayer = self.layers[count - 1], nLayer = None)
            else:
                l.connectLayer(pLayer = self.layers[count - 1], nLayer = self.layers[count + 1])
            count = count + 1

