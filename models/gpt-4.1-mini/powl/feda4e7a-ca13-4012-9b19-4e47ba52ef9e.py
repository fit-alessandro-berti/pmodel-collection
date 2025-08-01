# Generated from: feda4e7a-ca13-4012-9b19-4e47ba52ef9e.json
# Description: This process details the comprehensive lifecycle of an urban vertical farming operation integrating hydroponics, AI-driven climate control, and community-driven crop selection. It begins with site analysis and environmental scanning, followed by modular farm design and nutrient solution formulation. Automated seeding and growth monitoring leverage sensor data to optimize plant health. Periodic pest and disease management is conducted using bio-control agents and AI diagnostics. Harvesting is scheduled based on predictive analytics, with produce sorted and packaged through robotic lines. Community feedback is aggregated to refine crop varieties and distribution models. Waste is recycled into compost or biogas, closing the sustainability loop. This atypical process combines technology, ecology, and social dynamics to redefine urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Analysis = Transition(label='Site Analysis')
Env_Scanning = Transition(label='Env Scanning')
Farm_Design = Transition(label='Farm Design')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Automation = Transition(label='Seed Automation')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
AI_Diagnostics = Transition(label='AI Diagnostics')
Harvest_Plan = Transition(label='Harvest Plan')
Robotic_Sort = Transition(label='Robotic Sort')
Packaging_Line = Transition(label='Packaging Line')
Community_Input = Transition(label='Community Input')
Data_Aggregation = Transition(label='Data Aggregation')
Waste_Recycle = Transition(label='Waste Recycle')
Sustainability = Transition(label='Sustainability')

# Pest and Disease management loop: Pest_Control + AI_Diagnostics repeated until exit
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[Pest_Control, AI_Diagnostics])

# Harvesting subprocess partial order: Harvest_Plan --> Robotic_Sort --> Packaging_Line
harvest_po = StrictPartialOrder(nodes=[Harvest_Plan, Robotic_Sort, Packaging_Line])
harvest_po.order.add_edge(Harvest_Plan, Robotic_Sort)
harvest_po.order.add_edge(Robotic_Sort, Packaging_Line)

# Community feedback subprocess partial order: Community_Input --> Data_Aggregation
community_po = StrictPartialOrder(nodes=[Community_Input, Data_Aggregation])
community_po.order.add_edge(Community_Input, Data_Aggregation)

# Waste recycle subprocess partial order: Waste_Recycle --> Sustainability
waste_po = StrictPartialOrder(nodes=[Waste_Recycle, Sustainability])
waste_po.order.add_edge(Waste_Recycle, Sustainability)

# Main partial order nodes
nodes_main = [
    Site_Analysis,
    Env_Scanning,
    Farm_Design,
    Nutrient_Mix,
    Seed_Automation,
    Growth_Monitor,
    pest_loop,
    harvest_po,
    community_po,
    waste_po
]

root = StrictPartialOrder(nodes=nodes_main)

# Define the order relations according to the description

# Initial sequence: Site Analysis --> Env Scanning --> Farm Design --> Nutrient Mix
root.order.add_edge(Site_Analysis, Env_Scanning)
root.order.add_edge(Env_Scanning, Farm_Design)
root.order.add_edge(Farm_Design, Nutrient_Mix)

# Nutrient Mix --> Seed Automation --> Growth Monitor
root.order.add_edge(Nutrient_Mix, Seed_Automation)
root.order.add_edge(Seed_Automation, Growth_Monitor)

# Growth Monitor --> Pest Control loop (pest_loop)
root.order.add_edge(Growth_Monitor, pest_loop)

# After pest loop, Harvesting subprocess
root.order.add_edge(pest_loop, harvest_po)

# Harvesting --> Community feedback
root.order.add_edge(harvest_po, community_po)

# Community feedback --> Waste recycle subprocess
root.order.add_edge(community_po, waste_po)