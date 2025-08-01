# Generated from: 870ed8f6-46ef-44f9-a282-83cd8427bc27.json
# Description: This process outlines the comprehensive steps involved in establishing a sustainable urban rooftop farm on a commercial building. It includes site analysis, environmental impact assessments, selecting appropriate crops, structural reinforcements, irrigation system design, soil preparation, installation of climate control technologies, integration of renewable energy sources, pest management strategies, community engagement, ongoing maintenance scheduling, yield monitoring, and finally, produce distribution logistics. The process ensures maximization of limited space, compliance with local regulations, and creation of a resilient urban agriculture ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Site_Survey = Transition(label='Site Survey')
Load_Analysis = Transition(label='Load Analysis')
Permits_Request = Transition(label='Permits Request')
Crop_Selection = Transition(label='Crop Selection')
Soil_Testing = Transition(label='Soil Testing')
Irrigation_Setup = Transition(label='Irrigation Setup')
Structural_Reinforce = Transition(label='Structural Reinforce')
Climate_Control = Transition(label='Climate Control')
Energy_Integration = Transition(label='Energy Integration')
Pest_Management = Transition(label='Pest Management')
Community_Outreach = Transition(label='Community Outreach')
Maintenance_Plan = Transition(label='Maintenance Plan')
Yield_Monitoring = Transition(label='Yield Monitoring')
Harvest_Schedule = Transition(label='Harvest Schedule')
Distribution_Plan = Transition(label='Distribution Plan')

# Partial order (strict sequence) for main process with parallel branches where appropriate
# 1-3 mandatory initial steps in sequence
# Then Crop Selection, Soil Testing and Irrigation Setup, Structural Reinforce run in parallel
# Then Climate Control and Energy Integration in parallel
# Then Pest Management and Community Outreach in parallel
# Then Maintenance Plan, Yield Monitoring, Harvest Schedule, Distribution Plan in sequence

# Parallel sets
# Parallel group 1: Crop Selection, Soil Testing, Irrigation Setup, Structural Reinforce
group1_nodes = [Crop_Selection, Soil_Testing, Irrigation_Setup, Structural_Reinforce]

# Parallel group 2: Climate Control, Energy Integration
group2_nodes = [Climate_Control, Energy_Integration]

# Parallel group 3: Pest Management, Community Outreach
group3_nodes = [Pest_Management, Community_Outreach]

# Create root partial order node list:
nodes = [
    Site_Survey,
    Load_Analysis,
    Permits_Request,
] + group1_nodes + group2_nodes + group3_nodes + [
    Maintenance_Plan,
    Yield_Monitoring,
    Harvest_Schedule,
    Distribution_Plan,
]

root = StrictPartialOrder(nodes=nodes)

# Add order edges for sequential dependencies

# Initial sequence: Site Survey --> Load Analysis --> Permits Request
root.order.add_edge(Site_Survey, Load_Analysis)
root.order.add_edge(Load_Analysis, Permits_Request)

# Permits Request --> all group1_nodes (parallel start after permits)
for n in group1_nodes:
    root.order.add_edge(Permits_Request, n)

# All group1_nodes --> all group2_nodes (group2 starts after all group1 done)
# Enforce ordering that all group1_nodes precede group2_nodes by edges from each group1 node to each group2 node
for g1 in group1_nodes:
    for g2 in group2_nodes:
        root.order.add_edge(g1, g2)

# All group2_nodes --> all group3_nodes (same as above)
for g2 in group2_nodes:
    for g3 in group3_nodes:
        root.order.add_edge(g2, g3)

# All group3_nodes --> Maintenance Plan
for g3 in group3_nodes:
    root.order.add_edge(g3, Maintenance_Plan)

# Maintenance Plan --> Yield Monitoring --> Harvest Schedule --> Distribution Plan
root.order.add_edge(Maintenance_Plan, Yield_Monitoring)
root.order.add_edge(Yield_Monitoring, Harvest_Schedule)
root.order.add_edge(Harvest_Schedule, Distribution_Plan)