import nengo
import numpy as np

# dy/dt = x/tau - y/tau

# input: (x/tau) * synapse
# recurrent: (-y/tau) * synapse + y

N1 = 100
D1 = 1

N2 = 100
D2 = 1

synapse = 0.1
tau = 0.1

model = nengo.Network()
with model:
    stim = nengo.Node([0]*D1)
    x = nengo.Ensemble(n_neurons=N1, dimensions=D1, radius=3)
    y = nengo.Ensemble(n_neurons=N2, dimensions=D2)
    nengo.Connection(stim, x)
    
    def input_function(x):
        return x / tau * synapse
    def recurrent_function(y):
        return (-y / tau) * synapse + y
    
    nengo.Connection(x, y, synapse=synapse, function=input_function)
    nengo.Connection(y, y, synapse=synapse, function=recurrent_function)
