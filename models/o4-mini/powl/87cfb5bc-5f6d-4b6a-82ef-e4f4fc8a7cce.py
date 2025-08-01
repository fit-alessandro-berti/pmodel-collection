# Generated from: 87cfb5bc-5f6d-4b6a-82ef-e4f4fc8a7cce.json
# Description: This process outlines the end-to-end implementation of a bespoke urban farming system tailored for high-density city environments. It involves initial site assessment, soil and air quality analysis, modular design planning, sourcing sustainable materials, installing smart irrigation systems, integrating sensor networks for real-time monitoring, establishing vertical planting modules, implementing pest control using bioengineering methods, training local staff on system maintenance, conducting pilot crop cycles, optimizing nutrient delivery based on AI analytics, coordinating community engagement for shared farming spaces, managing harvest logistics with urban transport considerations, and finally evaluating overall yield performance for continuous improvement and scalability in constrained urban settings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site          = Transition(label='Site Assess')
soil          = Transition(label='Soil Test')
air           = Transition(label='Air Analyze')
design        = Transition(label='Design Plan')
material      = Transition(label='Material Source')
irrig         = Transition(label='Irrigation Setup')
sensor        = Transition(label='Sensor Install')
vertical      = Transition(label='Vertical Plant')
pest          = Transition(label='Pest Control')
train         = Transition(label='Staff Train')
pilot         = Transition(label='Pilot Crop')
nutrient      = Transition(label='Nutrient Adjust')
community     = Transition(label='Community Engage')
harvest       = Transition(label='Harvest Manage')
yield_review  = Transition(label='Yield Review')

# Loop for pilot crop cycles and nutrient adjustment
pilot_loop = OperatorPOWL(operator=Operator.LOOP, children=[pilot, nutrient])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site, soil, air, design, material,
    irrig, sensor, vertical,
    pest, train,
    pilot_loop,
    community, harvest, yield_review
])

# Site assessment leads to soil and air analysis (concurrent)
root.order.add_edge(site, soil)
root.order.add_edge(site, air)

# Analyses both must complete before design planning
root.order.add_edge(soil, design)
root.order.add_edge(air, design)

# Design → sourcing materials
root.order.add_edge(design, material)

# Sourcing materials → installation of irrigation, sensors, vertical modules (these three can be concurrent)
root.order.add_edge(material, irrig)
root.order.add_edge(material, sensor)
root.order.add_edge(material, vertical)

# Installations must complete before pest control and staff training (can be concurrent)
for pre in [irrig, sensor, vertical]:
    root.order.add_edge(pre, pest)
    root.order.add_edge(pre, train)

# After pest control and staff training, conduct pilot crop loop
root.order.add_edge(pest, pilot_loop)
root.order.add_edge(train, pilot_loop)

# After completing pilot cycles, engage community, then manage harvest, then review yield
root.order.add_edge(pilot_loop, community)
root.order.add_edge(community, harvest)
root.order.add_edge(harvest, yield_review)