import nengo
import nengo.spa as spa

D = 32  # the dimensionality of the vectors

model = spa.SPA()
with model:
    model.vision = spa.Buffer(D)
    model.memory = spa.Memory(D)

    actions = spa.Actions(
        'dot(memory, A) --> memory=B',
        'dot(memory, B) --> memory=C',
        'dot(memory, C) --> memory=D',
        'dot(memory, D) --> memory=E',
        'dot(memory, E) --> memory=vision',
        )
        
    model.bg = spa.BasalGanglia(actions)
    model.thalamus = spa.Thalamus(model.bg)
