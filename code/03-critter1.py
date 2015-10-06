import nengo

model = nengo.Network()
with model:
    
    # inputs to control the critter
    food = nengo.Node([0, 0])  # where should it go?

    # where is the critter currently going
    movement = nengo.Ensemble(n_neurons=100, dimensions=2)
    
    # a memory to figure out where it is
    position = nengo.Ensemble(n_neurons=500, dimensions=2, radius=5)
    nengo.Connection(position, position, synapse=0.2)
    nengo.Connection(movement, position, transform=0.5)

    nengo.Connection(food, movement)