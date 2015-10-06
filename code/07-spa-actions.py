import nengo
import nengo.spa as spa

D = 32  # the dimensionality of the vectors

model = spa.SPA()
with model:
    model.vision = spa.Buffer(D)

    model.speech = spa.Buffer(D)    

    actions = spa.Actions(
        'dot(vision, DOG) --> speech=BARK',
        'dot(vision, CAT) --> speech=MEOW',
        'dot(vision, RAT) --> speech=SQUEAK',
        'dot(vision, COW) --> speech=MOO',
        )
        
    model.bg = spa.BasalGanglia(actions)
    model.thalamus = spa.Thalamus(model.bg)
