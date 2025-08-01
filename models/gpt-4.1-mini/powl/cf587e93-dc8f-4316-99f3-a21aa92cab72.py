# Generated from: cf587e93-dc8f-4316-99f3-a21aa92cab72.json
# Description: This process outlines the intricate cycle of managing an urban vertical farm that integrates IoT sensors, hydroponic systems, and AI-driven growth optimization. It begins with seed selection tailored to urban microclimates, followed by nutrient calibration and environmental monitoring. The cycle includes periodic pest management using organic biocontrol agents, automated harvesting via robotic arms, and dynamic market demand analysis to adjust crop variety. Waste is recycled into bio-compost onsite, and energy consumption is optimized through smart grid integration. The process culminates in packaging using biodegradable materials and real-time logistics coordination to ensure freshest delivery to urban retailers, closing the sustainability loop in a dense metropolitan context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Seed_Select = Transition(label='Seed Select')
Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Setup = Transition(label='Sensor Setup')
Env_Monitor = Transition(label='Env Monitor')
Growth_Scan = Transition(label='Growth Scan')
Pest_Control = Transition(label='Pest Control')
Water_Cycle = Transition(label='Water Cycle')
Harvest_Robo = Transition(label='Harvest Robo')
Yield_Assess = Transition(label='Yield Assess')
Waste_Process = Transition(label='Waste Process')
Energy_Sync = Transition(label='Energy Sync')
Pack_Biodeg = Transition(label='Pack Biodeg')
Market_Track = Transition(label='Market Track')
Order_Align = Transition(label='Order Align')
Logistics_Plan = Transition(label='Logistics Plan')
Feedback_Loop = Transition(label='Feedback Loop')

# The main cycle:
# The process begins with seed selection, nutrient mix, sensor setup, env monitor, growth scan
# Then cycle includes pest control, water cycle, harvest robo, yield assess
# Then waste process, energy sync
# Then packaging (pack biodeg)
# Then market track, order align, logistics plan
# Then feedback loop to reinitiate cycle (like adjusting crop variety)
# So Feedback_Loop is used as loop's 'B' branch to cycle back

# Setup the main sequence before the loop
# Partial order of initial sequence before the loop:
initial_nodes = [Seed_Select, Nutrient_Mix, Sensor_Setup, Env_Monitor, Growth_Scan]
initial_po = StrictPartialOrder(nodes=initial_nodes)
initial_po.order.add_edge(Seed_Select, Nutrient_Mix)
initial_po.order.add_edge(Nutrient_Mix, Sensor_Setup)
initial_po.order.add_edge(Sensor_Setup, Env_Monitor)
initial_po.order.add_edge(Env_Monitor, Growth_Scan)

# Define the loop body: pest control, water cycle, harvest robo, yield assess
loop_body_nodes = [Pest_Control, Water_Cycle, Harvest_Robo, Yield_Assess]
loop_body_po = StrictPartialOrder(nodes=loop_body_nodes)
loop_body_po.order.add_edge(Pest_Control, Water_Cycle)
loop_body_po.order.add_edge(Water_Cycle, Harvest_Robo)
loop_body_po.order.add_edge(Harvest_Robo, Yield_Assess)

# After loop body is finished, Feedback_Loop triggers repeating
# The loop requires two nodes: A = loop body (tasks after initial), B = Feedback_Loop node (for continued looping)
# Actually, in POWL LOOP operator: * (A, B) means execute A, then choose to exit or execute B then A again, repeated until exit.
# So the B part usually models the part executed to repeat.

# However, here Feedback_Loop represents the cycle back to initial?
# The initial phase precedes loop, so the loop likely represents the repetitive part after initial.

# So the loop should encapsulate the activities that repeat:
# The cycle includes: Pest_Control to Yield_Assess, then Waste_Process, Energy_Sync,
# Then Packaging (Pack_Biodeg),
# Then Market_Track, Order_Align, Logistics_Plan,
# Then Feedback_Loop (to repeat growth scan and onwards?)

# Let's gather the full cyclic activities (after initial initial_po) into the loop:

# Let's create a partial order for post-growth scan activities before Feedback_Loop:

cycle_nodes = [
    Pest_Control, Water_Cycle, Harvest_Robo, Yield_Assess,
    Waste_Process, Energy_Sync,
    Pack_Biodeg,
    Market_Track, Order_Align, Logistics_Plan
]

cycle_po = StrictPartialOrder(nodes=cycle_nodes)

# Add edges for this cycle according to logical dependencies:

# Pest_Control -> Water_Cycle -> Harvest_Robo -> Yield_Assess
cycle_po.order.add_edge(Pest_Control, Water_Cycle)
cycle_po.order.add_edge(Water_Cycle, Harvest_Robo)
cycle_po.order.add_edge(Harvest_Robo, Yield_Assess)

# Yield_Assess -> Waste_Process and Yield_Assess -> Energy_Sync (these two concurrent)
cycle_po.order.add_edge(Yield_Assess, Waste_Process)
cycle_po.order.add_edge(Yield_Assess, Energy_Sync)

# Waste_Process and Energy_Sync both precede Pack_Biodeg
cycle_po.order.add_edge(Waste_Process, Pack_Biodeg)
cycle_po.order.add_edge(Energy_Sync, Pack_Biodeg)

# Pack_Biodeg precedes combined market activities
cycle_po.order.add_edge(Pack_Biodeg, Market_Track)
cycle_po.order.add_edge(Pack_Biodeg, Order_Align)

# Market_Track and Order_Align precede Logistics_Plan
cycle_po.order.add_edge(Market_Track, Logistics_Plan)
cycle_po.order.add_edge(Order_Align, Logistics_Plan)

# Now the loop is defined as LOOP(A, B) where:
# A = cycle_po
# B = Feedback_Loop (silent transition could be used but activity 'Feedback Loop' is given)
loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle_po, Feedback_Loop])

# Now connect initial and the loop
# growth scan precedes the loop
root = StrictPartialOrder(nodes=[initial_po, loop])
root.order.add_edge(initial_po, loop)

# In POWL, nodes are activities or operator nodes, so edges between PO or OperatorPOWL nodes are allowed.
# This models initial phase followed by a loop repeatedly doing cycle then feedback loop until exit.

# Finally this represents the process accurately
