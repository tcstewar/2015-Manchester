import nengo

model = nengo.Network()
with model:
    
    # inputs to control the critter
    food = nengo.Node([0, 0])  # where should it go?
    scare = nengo.Node([0])       # is it scared?

    # where is the critter currently going
    movement = nengo.Ensemble(n_neurons=100, dimensions=2)
    
    # a memory to figure out where it is
    position = nengo.Ensemble(n_neurons=500, dimensions=2, radius=5)
    nengo.Connection(position, position, synapse=0.2)
    nengo.Connection(movement, position, transform=0.5)

    # A system for figuring out if it should follow the food
    do_food = nengo.Ensemble(n_neurons=300, dimensions=2)
    nengo.Connection(food, do_food)
    nengo.Connection(do_food, movement)
    
    def gate_food(scare):
        return -2 if scare > 0.5 else 0
    nengo.Connection(scare, do_food.neurons, transform=[[1]]*do_food.n_neurons,
                     function=gate_food)    
