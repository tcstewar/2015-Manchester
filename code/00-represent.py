import nengo

N = 100
D = 3

model = nengo.Network()
with model:
    stim = nengo.Node([0]*D)
    
    ens = nengo.Ensemble(n_neurons=N, dimensions=D)
    
    nengo.Connection(stim, ens)