# Generated from: 5d0b7a16-926f-48ce-b2df-0a87ce204be0.json
# Description: This process outlines the establishment of a fully automated urban vertical farm specializing in exotic microgreens and rare herbs. It involves site assessment, modular system design, automated nutrient calibration, climate optimization using AI, pest bio-control integration, and continuous yield monitoring. The process further incorporates local community engagement for education, waste recycling through composting, and real-time market demand analysis to adjust crop cycles dynamically. It ensures sustainable resource use, minimal carbon footprint, and high-quality organic produce delivery within urban environments through advanced logistics and smart packaging solutions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Modular_Design = Transition(label='Modular Design')
System_Assembly = Transition(label='System Assembly')
Sensor_Install = Transition(label='Sensor Install')
Nutrient_Setup = Transition(label='Nutrient Setup')
Climate_Tune = Transition(label='Climate Tune')
Pest_Control = Transition(label='Pest Control')
Seed_Selection = Transition(label='Seed Selection')
Planting_Cycle = Transition(label='Planting Cycle')
Growth_Monitor = Transition(label='Growth Monitor')
Waste_Cycle = Transition(label='Waste Cycle')
Market_Scan = Transition(label='Market Scan')
Demand_Adjust = Transition(label='Demand Adjust')
Harvest_Prep = Transition(label='Harvest Prep')
Packaging_Ops = Transition(label='Packaging Ops')
Delivery_Plan = Transition(label='Delivery Plan')
Community_Meet = Transition(label='Community Meet')

# Initial setup sequence:
# Site Survey -> Modular Design -> System Assembly
initial_seq = StrictPartialOrder(nodes=[Site_Survey, Modular_Design, System_Assembly])
initial_seq.order.add_edge(Site_Survey, Modular_Design)
initial_seq.order.add_edge(Modular_Design, System_Assembly)

# Sensors and Nutrient Setup and Climate Tune and Pest Control are parallel after assembly:
# Sensor Install, Nutrient Setup, Climate Tune, Pest Control all in parallel after System Assembly
sensors_nutrients_climate_pest = StrictPartialOrder(
    nodes=[Sensor_Install, Nutrient_Setup, Climate_Tune, Pest_Control]
)
# The order edges come from System Assembly to each parallel node
# We'll connect System Assembly -> each parallel activity in the main PO,
# so we model them as parallel nodes here.

# Planting cycle loop: (Seed Selection -> Planting Cycle -> Growth Monitor) with loop on Planting Cycle and Growth Monitor,
# allowing repeated adjustment of planting/growth cycles through Market Scan and Demand Adjust
# Model loop as: A=Seed Selection; B=(Planting Cycle -> Growth Monitor -> Market Scan -> Demand Adjust)

# Define the inner PO for B: Planting Cycle -> Growth Monitor -> Market Scan -> Demand Adjust
market_loop_seq = StrictPartialOrder(
    nodes=[Planting_Cycle, Growth_Monitor, Market_Scan, Demand_Adjust]
)
market_loop_seq.order.add_edge(Planting_Cycle, Growth_Monitor)
market_loop_seq.order.add_edge(Growth_Monitor, Market_Scan)
market_loop_seq.order.add_edge(Market_Scan, Demand_Adjust)

loop_node = OperatorPOWL(operator=Operator.LOOP, children=[Seed_Selection, market_loop_seq])

# Waste Cycle runs concurrently and continuously but modeled here as a single activity concurrent to loop
# Waste Cycle runs concurrently with loop and possibly other activities
# To simplify, Waste Cycle concurrent with loop and packaging/delivery

# After loop and waste cycle finish, Harvest Prep -> Packaging Ops -> Delivery Plan sequentially
harvest_seq = StrictPartialOrder(
    nodes=[Harvest_Prep, Packaging_Ops, Delivery_Plan]
)
harvest_seq.order.add_edge(Harvest_Prep, Packaging_Ops)
harvest_seq.order.add_edge(Packaging_Ops, Delivery_Plan)

# Community Meet is independent and can run in parallel anywhere after initial setup

# Build the full POWL combining initial_seq -> parallel after system assembly + loop + waste cycle + harvest + community

# Let's create a PO combining all main blocks:
# nodes: initial_seq nodes + sensors and nutrient/climate/pest nodes + loop + waste cycle + harvest_seq + community

nodes_all = [
    initial_seq,
    sensors_nutrients_climate_pest,
    loop_node,
    Waste_Cycle,
    harvest_seq,
    Community_Meet
]

root = StrictPartialOrder(nodes=nodes_all)

# Edges:
# initial_seq -> sensors_nutrients_climate_pest, loop_node, Waste_Cycle, Community_Meet
root.order.add_edge(initial_seq, sensors_nutrients_climate_pest)
root.order.add_edge(initial_seq, loop_node)
root.order.add_edge(initial_seq, Waste_Cycle)
root.order.add_edge(initial_seq, Community_Meet)

# sensors_nutrients_climate_pest -> harvest_seq
root.order.add_edge(sensors_nutrients_climate_pest, harvest_seq)

# loop_node -> harvest_seq
root.order.add_edge(loop_node, harvest_seq)

# Waste_Cycle -> harvest_seq
root.order.add_edge(Waste_Cycle, harvest_seq)