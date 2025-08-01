# Generated from: 2d3301d6-889c-43f6-839d-0eec2b0c5b95.json
# Description: This process describes the complex and multifaceted steps involved in establishing an urban vertical farm in a densely populated city. It begins with site analysis and zoning approval, followed by modular structure design and climate system integration. The process continues with nutrient solution preparation, automated seeding, and lighting calibration. Maintenance routines include pest monitoring and system diagnostics, while data analytics optimize growth cycles. Finally, the harvest scheduling and distribution logistics ensure fresh produce delivery within tight urban supply chains, balancing sustainability with commercial viability in constrained spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Site_Analysis = Transition(label='Site Analysis')
Zoning_Review = Transition(label='Zoning Review')
Modular_Design = Transition(label='Modular Design')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Automation = Transition(label='Seed Automation')
Lighting_Calibrate = Transition(label='Lighting Calibrate')
Pest_Monitor = Transition(label='Pest Monitor')
System_Diagnostics = Transition(label='System Diagnostics')
Growth_Analytics = Transition(label='Growth Analytics')
Harvest_Schedule = Transition(label='Harvest Schedule')
Supply_Logistics = Transition(label='Supply Logistics')
Waste_Recycling = Transition(label='Waste Recycling')
Energy_Audit = Transition(label='Energy Audit')
Quality_Testing = Transition(label='Quality Testing')

# Maintenance routine partial order:
# Pest Monitor and System Diagnostics are maintenance routines, possibly concurrent,
# followed by Waste Recycling, Energy Audit, Quality Testing in sequence for final checks.
maintenance = StrictPartialOrder(
    nodes=[Pest_Monitor, System_Diagnostics, Waste_Recycling, Energy_Audit, Quality_Testing]
)
maintenance.order.add_edge(Pest_Monitor, Waste_Recycling)
maintenance.order.add_edge(System_Diagnostics, Waste_Recycling)
maintenance.order.add_edge(Waste_Recycling, Energy_Audit)
maintenance.order.add_edge(Energy_Audit, Quality_Testing)

# Growth related partial order:
# Nutrient Mix, Seed Automation, Lighting Calibrate happen in parallel (concurrent)
prep = StrictPartialOrder(nodes=[Nutrient_Mix, Seed_Automation, Lighting_Calibrate])
# No edges in prep indicating concurrency

# After prep, maintenance runs
# After maintenance, growth analytics (optimizes growth cycles)
# Followed by Harvest Schedule and Supply Logistics in sequence
post_growth = StrictPartialOrder(
    nodes=[maintenance, Growth_Analytics, Harvest_Schedule, Supply_Logistics]
)
post_growth.order.add_edge(maintenance, Growth_Analytics)
post_growth.order.add_edge(Growth_Analytics, Harvest_Schedule)
post_growth.order.add_edge(Harvest_Schedule, Supply_Logistics)

# Structure design partial order:
# Modular Design then Climate Setup
structure = StrictPartialOrder(nodes=[Modular_Design, Climate_Setup])
structure.order.add_edge(Modular_Design, Climate_Setup)

# Initial phase partial order:
# Site Analysis then Zoning Review then structure design
initial = StrictPartialOrder(nodes=[Site_Analysis, Zoning_Review, structure])
initial.order.add_edge(Site_Analysis, Zoning_Review)
initial.order.add_edge(Zoning_Review, structure)

# Combine all phases into one partial order:
root = StrictPartialOrder(nodes=[initial, prep, post_growth])
# initial -> prep
root.order.add_edge(initial, prep)
# prep -> post_growth
root.order.add_edge(prep, post_growth)