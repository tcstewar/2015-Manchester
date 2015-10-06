import nengo
import nengo.spa as spa

D = 32  # the dimensionality of the vectors

model = spa.SPA()
with model:
    model.vision = spa.Buffer(D)
    
    model.noun = spa.Memory(D, synapse=0.2)
    model.verb = spa.Memory(D, synapse=0.2)
    model.sentence = spa.Buffer(D)
    
    model.speech = spa.Buffer(D)
    model.hand = spa.Buffer(D)

    actions = spa.Actions(
        'dot(vision, WRITE+SAY) --> verb=vision',
        'dot(vision, A+B+C+D+E) --> noun=vision',
        'dot(sentence, VERB*WRITE) - dot(vision, WRITE+SAY+A+B+C+D+E)'
            '--> hand=sentence*~NOUN',
        'dot(sentence, VERB*SAY) - dot(vision, WRITE+SAY+A+B+C+D+E)'
            '--> speech=sentence*~NOUN',
        )
        
    model.bg = spa.BasalGanglia(actions)
    model.thalamus = spa.Thalamus(model.bg)
    
    model.cortical = spa.Cortical(spa.Actions(
        'sentence=verb*VERB+noun*NOUN',
        ))