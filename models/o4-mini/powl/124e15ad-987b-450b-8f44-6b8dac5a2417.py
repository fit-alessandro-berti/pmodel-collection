# Generated from: 124e15ad-987b-450b-8f44-6b8dac5a2417.json
# Description: This process outlines the complex and atypical supply chain involved in producing artisan cheese from small-scale farms to niche gourmet shops. It begins with seasonal milk collection, followed by precise fermentation control, handcrafting curd molding, and quality maturation monitoring. The process includes sensory evaluation panels, organic certification audits, and custom packaging design tailored to regional tastes. Distribution leverages specialized cold transport logistics and direct-to-chef delivery schedules. Feedback loops from retailers and consumers inform iterative recipe adjustments, ensuring unique flavors and consistent quality across batches. Sustainability tracking and waste repurposing are integrated throughout, emphasizing eco-conscious production and community engagement within a localized artisan network.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
milk = Transition(label='Milk Harvest')
ferm = Transition(label='Fermentation Check')
curd = Transition(label='Curd Molding')
salt = Transition(label='Salt Application')
press = Transition(label='Pressing Stage')
matur = Transition(label='Maturation Monitor')
quality = Transition(label='Quality Testing')
sensory = Transition(label='Sensory Panel')
cert = Transition(label='Certification Audit')
pack = Transition(label='Packaging Design')
cold = Transition(label='Cold Transport')
retail = Transition(label='Retail Delivery')
cons_feedback = Transition(label='Consumer Feedback')
recipe = Transition(label='Recipe Tuning')
waste = Transition(label='Waste Recycling')

# Body of the loop: the main cheese‐making and distribution sequence
body = StrictPartialOrder(nodes=[
    milk, ferm, curd, salt, press, matur,
    quality, sensory, cert, pack, cold, retail
])
body.order.add_edge(milk, ferm)
body.order.add_edge(ferm, curd)
body.order.add_edge(curd, salt)
body.order.add_edge(salt, press)
body.order.add_edge(press, matur)
body.order.add_edge(matur, quality)
body.order.add_edge(quality, sensory)
body.order.add_edge(sensory, cert)
body.order.add_edge(cert, pack)
body.order.add_edge(pack, cold)
body.order.add_edge(cold, retail)

# Feedback sub‐workflow: consumer/retailer feedback leading to recipe tuning
feedback = StrictPartialOrder(nodes=[cons_feedback, recipe])
feedback.order.add_edge(cons_feedback, recipe)

# Loop: do the body, then optionally take feedback and redo the body
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, feedback])

# Root: the loop runs, and waste recycling can occur at any time (concurrent)
root = StrictPartialOrder(nodes=[loop, waste])
# no ordering edge between 'loop' and 'waste' => concurrency