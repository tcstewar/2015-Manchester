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
    do_food = nengo.Ensemble(n_neurons=300, dimensions=3, radius=1.4)
    def attention_food(scare):
        if scare < 0.5:
            return 1
        else:
            return 0
    nengo.Connection(scare, do_food[0], function=attention_food)
    nengo.Connection(food, do_food[1:])
    
    # combine the two above systems to get a total movement command
    def apply_attention(state):
        attention, x, y = state
        return attention * x, attention * y
    nengo.Connection(do_food, movement, function=apply_attention)
