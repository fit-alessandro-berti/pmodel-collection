# Generated from: 49efddab-656a-4286-82b6-94521c5d5e7a.json
# Description: This process outlines the intricate steps involved in transforming underutilized urban rooftop spaces into productive, sustainable farms. It includes assessing structural integrity, securing permits, designing modular irrigation systems, sourcing organic seeds, and training local community members. The workflow also addresses crop rotation planning to maximize yield, integrating solar-powered sensors for optimal growth conditions, managing waste composting onsite, coordinating with local markets for direct sales, and implementing seasonal maintenance protocols to ensure long-term farm health and community engagement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
inspect = Transition(label='Inspect Roof')
permit = Transition(label='Permit Apply')
soil = Transition(label='Soil Testing')
design = Transition(label='Design Layout')
irrig = Transition(label='Irrigation Setup')
compost = Transition(label='Compost Setup')
sensors = Transition(label='Install Sensors')
seed = Transition(label='Seed Sourcing')
train = Transition(label='Train Staff')
market = Transition(label='Market Plan')
plant = Transition(label='Plant Seeds')
crop_rotate = Transition(label='Crop Rotate')
harvest = Transition(label='Harvest Crop')
waste = Transition(label='Waste Collect')
maint = Transition(label='Maintenance Check')
community = Transition(label='Community Meet')

# Build the sub‐process B for the loop: Crop Rotate -> Harvest -> Waste -> Maintenance -> Community Meet
b = StrictPartialOrder(nodes=[crop_rotate, harvest, waste, maint, community])
b.order.add_edge(crop_rotate, harvest)
b.order.add_edge(harvest, waste)
b.order.add_edge(waste, maint)
b.order.add_edge(maint, community)

# Build the LOOP node: first Plant, then repeat B followed by Plant again etc.
loop = OperatorPOWL(operator=Operator.LOOP, children=[plant, b])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    inspect, permit, soil, design,
    irrig, compost, sensors,
    seed, train, market,
    loop
])

# Define the control‐flow dependencies
# Inspection must precede permits and soil testing
root.order.add_edge(inspect, permit)
root.order.add_edge(inspect, soil)
# Permit and soil testing both before layout design
root.order.add_edge(permit, design)
root.order.add_edge(soil, design)
# After design, set up irrigation, composting, sensors, and do market planning in parallel
root.order.add_edge(design, irrig)
root.order.add_edge(design, compost)
root.order.add_edge(design, sensors)
root.order.add_edge(design, market)
# After irrigation, compost and sensors and soil testing, source seeds
root.order.add_edge(irrig, seed)
root.order.add_edge(compost, seed)
root.order.add_edge(sensors, seed)
root.order.add_edge(soil, seed)
# After seeding, train staff
root.order.add_edge(seed, train)
# Both market planning and staff training must complete before starting the seasonal loop
root.order.add_edge(market, loop)
root.order.add_edge(train, loop)