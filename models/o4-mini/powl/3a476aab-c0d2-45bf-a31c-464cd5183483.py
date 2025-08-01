# Generated from: 3a476aab-c0d2-45bf-a31c-464cd5183483.json
# Description: This process outlines the unconventional approach of establishing a sustainable urban rooftop farm on a high-rise building. It involves site assessment, structural analysis, soil preparation, microclimate optimization, planting, automated irrigation setup, pest control using integrated biological methods, crop monitoring via drones, community engagement for education, harvesting, yield analysis, and finally, distribution logistics tailored for urban markets. The process requires coordination among architects, agronomists, engineers, and local authorities to ensure compliance with safety and environmental standards while maximizing crop output and minimizing resource usage, making it a complex yet innovative business model for urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the core activities
site = Transition(label='Site Assess')
struct = Transition(label='Structural Check')
soil = Transition(label='Soil Prep')
climate = Transition(label='Climate Tune')
plant = Transition(label='Planting Plan')
irrig = Transition(label='Irrigation Setup')
pest = Transition(label='Pest Control')
drone = Transition(label='Drone Survey')
growth = Transition(label='Growth Monitor')
community = Transition(label='Community Meet')
harvest = Transition(label='Harvest Crop')
yieldA = Transition(label='Yield Audit')
market = Transition(label='Market Link')
waste = Transition(label='Waste Manage')
report = Transition(label='Report Review')

# A silent transition for optional/loop constructs
skip = SilentTransition()

# 1) Optional community engagement (Community Meet or skip)
comm_choice = OperatorPOWL(operator=Operator.XOR, children=[community, skip])

# 2) Monitoring loop: zero or more iterations of (Drone Survey -> Growth Monitor -> Pest Control)
body = StrictPartialOrder(nodes=[drone, growth, pest])
body.order.add_edge(drone, growth)
body.order.add_edge(growth, pest)
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[skip, body])

# 3) Distribution choice: either Market Link or Waste Manage
dist_choice = OperatorPOWL(operator=Operator.XOR, children=[market, waste])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    site, struct, soil, climate, plant, irrig,
    comm_choice, monitor_loop,
    harvest, yieldA, dist_choice, report
])

# Add control‐flow edges
root.order.add_edge(site, struct)
root.order.add_edge(struct, soil)
root.order.add_edge(soil, climate)
root.order.add_edge(climate, plant)
root.order.add_edge(plant, irrig)
root.order.add_edge(irrig, comm_choice)
root.order.add_edge(comm_choice, monitor_loop)
root.order.add_edge(monitor_loop, harvest)
root.order.add_edge(harvest, yieldA)
root.order.add_edge(yieldA, dist_choice)
root.order.add_edge(dist_choice, report)