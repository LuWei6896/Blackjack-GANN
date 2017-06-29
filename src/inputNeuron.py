from neuron import neuron

class inputNeuron(neuron):
    def __init__(self):
        self.outputNeurons = []
        self.outputVal = None

    def run(self, value):
        self.outputVal = value
