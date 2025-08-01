# Generated from: 12f92b34-52d6-4c9b-b577-7347af159c6c.json
# Description: This process outlines the comprehensive setup of an urban vertical farming system within a repurposed industrial building. It involves site assessment, modular structure assembly, climate control integration, nutrient solution preparation, automated seeding, growth monitoring via IoT sensors, pest management using biological agents, harvesting automation, waste recycling, and distribution logistics. The process ensures sustainability by incorporating renewable energy sources and water recirculation systems while maintaining compliance with urban agricultural regulations and community engagement for social acceptance.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
Site_Survey = Transition(label='Site Survey')
Structure_Build = Transition(label='Structure Build')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Prep = Transition(label='Nutrient Prep')
Seed_Automation = Transition(label='Seed Automation')
Sensor_Install = Transition(label='Sensor Install')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Harvest_Automate = Transition(label='Harvest Automate')
Waste_Recycle = Transition(label='Waste Recycle')
Energy_Integrate = Transition(label='Energy Integrate')
Water_Recirc = Transition(label='Water Recirc')
Compliance_Check = Transition(label='Compliance Check')
Community_Engage = Transition(label='Community Engage')
Logistics_Plan = Transition(label='Logistics Plan')

# Define partial orders reflecting dependencies and concurrency:

# 1. Initial phase: Site Survey --> Structure Build --> Climate Setup
initial_phase = StrictPartialOrder(nodes=[Site_Survey, Structure_Build, Climate_Setup])
initial_phase.order.add_edge(Site_Survey, Structure_Build)
initial_phase.order.add_edge(Structure_Build, Climate_Setup)

# 2. Nutrient Prep and Energy Integrate and Water Recirc can happen in parallel after Climate Setup
prep_and_infra = StrictPartialOrder(nodes=[Nutrient_Prep, Energy_Integrate, Water_Recirc])
# no order edges between these three to allow concurrency

# 3. Seed Automation depends on Nutrient Prep
seed_phase = StrictPartialOrder(nodes=[Nutrient_Prep, Seed_Automation])
seed_phase.order.add_edge(Nutrient_Prep, Seed_Automation)

# 4. Sensor Install and Pest Control can happen concurrently after Climate Setup and Structure_Build
monitor_phase = StrictPartialOrder(nodes=[Sensor_Install, Pest_Control])
# no direct order edges between these two

# 5. Growth Monitor depends on Sensor Install
grow_monitor_phase = StrictPartialOrder(nodes=[Sensor_Install, Growth_Monitor])
grow_monitor_phase.order.add_edge(Sensor_Install, Growth_Monitor)

# 6. Harvest Automate depends on Growth Monitor and Pest Control
harvest_phase = StrictPartialOrder(nodes=[Growth_Monitor, Pest_Control, Harvest_Automate])
harvest_phase.order.add_edge(Growth_Monitor, Harvest_Automate)
harvest_phase.order.add_edge(Pest_Control, Harvest_Automate)

# 7. Waste Recycle can be concurrent with Harvest Automate
waste_phase = StrictPartialOrder(nodes=[Harvest_Automate, Waste_Recycle])
# no order edges -> concurrent

# 8. Compliance Check and Community Engage can be done in parallel, likely after initial setup and before logistics
compliance_community = StrictPartialOrder(nodes=[Compliance_Check, Community_Engage])
# no order edges so concurrent

# 9. Logistics Plan after Harvest Automate and Community Engage and Compliance Check
logistics_phase = StrictPartialOrder(nodes=[Harvest_Automate, Community_Engage, Compliance_Check, Logistics_Plan])
logistics_phase.order.add_edge(Harvest_Automate, Logistics_Plan)
logistics_phase.order.add_edge(Community_Engage, Logistics_Plan)
logistics_phase.order.add_edge(Compliance_Check, Logistics_Plan)

# Combine the phases together in a larger PO:
# Start: initial_phase
# Then: prep_and_infra concurrent with seed_phase and monitor_phase
# Then: growth monitoring + pest control + harvesting + waste recycling
# Then: compliance/community concurrent
# Finally: logistics

# Partial order nodes:
nodes = [
    initial_phase,
    prep_and_infra,
    seed_phase,
    monitor_phase,
    grow_monitor_phase,
    harvest_phase,
    waste_phase,
    compliance_community,
    logistics_phase
]

root = StrictPartialOrder(nodes=nodes)

# Add order edges between phases:

root.order.add_edge(initial_phase, prep_and_infra)  # after Climate Setup
root.order.add_edge(initial_phase, seed_phase)      # because seed_phase depends on Nutrient Prep which is in prep_and_infra but Nutrient_Prep is in seed_phase nodes too, to be safe add edges from initial_phase
root.order.add_edge(initial_phase, monitor_phase)

root.order.add_edge(prep_and_infra, grow_monitor_phase)
root.order.add_edge(seed_phase, grow_monitor_phase)
root.order.add_edge(monitor_phase, grow_monitor_phase)

root.order.add_edge(grow_monitor_phase, harvest_phase)
root.order.add_edge(monitor_phase, harvest_phase)  # Pest Control is in monitor_phase which is prerequisite to harvest_phase
root.order.add_edge(harvest_phase, waste_phase)

root.order.add_edge(harvest_phase, compliance_community)
root.order.add_edge(waste_phase, compliance_community)

root.order.add_edge(compliance_community, logistics_phase)

# Note: some edges are implicit inside subPOs, here we add only cross-subPO edges.
