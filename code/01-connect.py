import nengo
import numpy as np

N1 = 200
D1 = 3

N2 = 50
D2 = 1

model = nengo.Network()
with model:
    stim = nengo.Node([0]*D1)
    
    x = nengo.Ensemble(n_neurons=N1, dimensions=D1, radius=3)

    y = nengo.Ensemble(n_neurons=N2, dimensions=D2)
    
    nengo.Connection(stim, x)
    
    def function(x):
        return np.sin(x[0]) + x[1]*x[2]
    
    nengo.Connection(x, y, function=function)