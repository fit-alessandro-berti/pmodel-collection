# Generated from: 5e9b1592-4abe-45af-a761-1e7d07763c76.json
# Description: This process involves the complex orchestration of launching an urban vertical farm within a densely populated city environment. It includes site analysis, modular design planning, securing permits, integrating IoT sensors for climate control, sourcing sustainable materials, recruiting specialized agronomists, installing hydroponic systems, setting up renewable energy sources, executing controlled environment tests, developing a local supply chain, initiating community engagement programs, implementing waste recycling methods, launching a direct-to-consumer platform, conducting ongoing crop yield analysis, and establishing scalability frameworks for future expansion. Each step requires precise coordination of technology, regulatory compliance, and stakeholder involvement to ensure the farm's viability and sustainability in an unconventional agricultural setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site = Transition(label='Site Analysis')
design = Transition(label='Design Planning')
permit = Transition(label='Permit Securing')
iot = Transition(label='IoT Integration')
material = Transition(label='Material Sourcing')
recruit = Transition(label='Recruit Agronomists')
hydro = Transition(label='Hydroponic Setup')
energy = Transition(label='Energy Installation')
testing = Transition(label='Environment Testing')
supply = Transition(label='Supply Chain')
outreach = Transition(label='Community Outreach')
waste = Transition(label='Waste Recycling')
platform = Transition(label='Platform Launch')
yield_analysis = Transition(label='Yield Analysis')
scale_framework = Transition(label='Scale Framework')

# Define a loop: perform yield analysis then scale framework, repeat until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_analysis, scale_framework])

# Build the partial order model
root = StrictPartialOrder(nodes=[
    site, design, permit, iot, material, recruit, hydro, energy,
    testing, supply, outreach, waste, platform, loop
])

# Add ordering constraints
root.order.add_edge(site, design)
root.order.add_edge(design, permit)
root.order.add_edge(permit, iot)
root.order.add_edge(iot, material)
root.order.add_edge(material, recruit)
root.order.add_edge(recruit, hydro)
root.order.add_edge(hydro, energy)
root.order.add_edge(energy, testing)

# After environment testing, supply chain and community outreach can proceed in parallel
root.order.add_edge(testing, supply)
root.order.add_edge(testing, outreach)

# Waste recycling depends on both supply chain and community outreach
root.order.add_edge(supply, waste)
root.order.add_edge(outreach, waste)

# Platform launch follows waste recycling
root.order.add_edge(waste, platform)

# After platform launch, enter the loop of yield analysis and scaling
root.order.add_edge(platform, loop)