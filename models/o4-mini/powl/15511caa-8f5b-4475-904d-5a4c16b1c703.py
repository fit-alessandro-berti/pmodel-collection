# Generated from: 15511caa-8f5b-4475-904d-5a4c16b1c703.json
# Description: This process involves orchestrating a product launch that integrates multisensory marketing techniques to engage customers on visual, auditory, olfactory, and tactile levels. The process begins with conceptualizing sensory themes, proceeds through iterative prototype testing with focus groups using VR and AR environments, and coordinates with supply chain teams to source unique materials for packaging that enhance touch and smell. Marketing campaigns are synchronized across digital, physical, and experiential channels, incorporating soundscapes and scent diffusers in retail locations. Post-launch, customer feedback is gathered via biometric sensors and sentiment analysis to refine future launches. This atypical approach ensures a deeply immersive brand experience, differentiating the product in competitive markets by leveraging sensory psychology and advanced technology integration.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
theme = Transition(label='Theme Concept')
prot_vr = Transition(label='Prototype VR')
focus = Transition(label='Focus Testing')
material = Transition(label='Material Sourcing')
packaging = Transition(label='Packaging Design')
scent = Transition(label='Scent Development')
sound = Transition(label='Sound Creation')
campaign = Transition(label='Campaign Sync')
retail = Transition(label='Retail Setup')
sensor = Transition(label='Sensor Install')
launch = Transition(label='Launch Event')
data = Transition(label='Data Capture')
sentiment = Transition(label='Sentiment Scan')
feedback = Transition(label='Feedback Review')
refine = Transition(label='Refinement Plan')

# Iterative prototype‐test loop: Prototype VR then Focus Testing
loop = OperatorPOWL(operator=Operator.LOOP, children=[prot_vr, focus])

# Build the partial order model
root = StrictPartialOrder(nodes=[
    theme, loop,
    material, packaging, scent,
    sound,
    campaign, retail, sensor, launch,
    data, sentiment, feedback, refine
])

# Define the control‐flow dependencies
root.order.add_edge(theme, loop)

# After prototyping loop, branch into packaging chain and sound creation in parallel
root.order.add_edge(loop, material)
root.order.add_edge(loop, sound)

# Packaging chain for tactile & olfactory enhancements
root.order.add_edge(material, packaging)
root.order.add_edge(packaging, scent)

# Synchronize multi‐sensory marketing assets
root.order.add_edge(scent, campaign)
root.order.add_edge(sound, campaign)

# Deploy into channels and setup in retail
root.order.add_edge(campaign, retail)
root.order.add_edge(retail, sensor)

# Launch event once setup is complete
root.order.add_edge(sensor, launch)

# Post‐launch feedback gathering
root.order.add_edge(launch, data)
root.order.add_edge(launch, sentiment)

# Review and plan refinements
root.order.add_edge(data, feedback)
root.order.add_edge(sentiment, feedback)
root.order.add_edge(feedback, refine)