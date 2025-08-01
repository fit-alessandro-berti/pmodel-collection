# Generated from: 2fb36504-c4b5-4b90-8c94-3bbeb02ce2f4.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming facility within a repurposed industrial building. It involves assessing structural integrity, selecting suitable crops, designing multi-tier hydroponic systems, integrating IoT sensors for climate control, sourcing sustainable materials, setting up automated nutrient delivery, implementing renewable energy solutions, training staff on specialized farming techniques, establishing supply chain logistics for perishable goods, ensuring compliance with local agricultural and safety regulations, and launching a community engagement program to promote urban agriculture awareness. The process requires coordination among architects, agronomists, engineers, and marketing teams to create a resilient, efficient, and scalable urban farm that addresses food security in densely populated areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site = Transition(label='Site Survey')
structural = Transition(label='Structural Check')
crop = Transition(label='Crop Select')
design = Transition(label='System Design')
iot = Transition(label='IoT Setup')
material = Transition(label='Material Sourcing')
nutrient = Transition(label='Nutrient Plan')
energy = Transition(label='Energy Install')
staff = Transition(label='Staff Training')
logistics = Transition(label='Logistics Plan')
regulation = Transition(label='Regulation Audit')
community = Transition(label='Community Outreach')
quality = Transition(label='Quality Testing')
launch = Transition(label='Market Launch')
feedback = Transition(label='Feedback Loop')

# Define the loop for quality testing and market launch with feedback
loop_body = StrictPartialOrder(nodes=[quality, launch])
loop_body.order.add_edge(quality, launch)
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, feedback])

# Build the main partial order
root = StrictPartialOrder(nodes=[
    site, structural, crop, design,
    iot, material, nutrient, energy,
    staff, logistics, regulation, community,
    loop
])

# Add control-flow edges
root.order.add_edge(site, structural)
root.order.add_edge(structural, crop)
root.order.add_edge(crop, design)
root.order.add_edge(design, iot)
root.order.add_edge(design, material)
root.order.add_edge(design, nutrient)
root.order.add_edge(design, energy)
for pred in [iot, material, nutrient, energy]:
    root.order.add_edge(pred, staff)
root.order.add_edge(staff, logistics)
root.order.add_edge(logistics, regulation)
root.order.add_edge(regulation, community)
root.order.add_edge(community, loop)