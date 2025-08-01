# Generated from: 184bf411-abe9-4d61-8bce-5c577be2da95.json
# Description: This process outlines the complex steps required to establish a sustainable urban rooftop farm in a metropolitan environment. It involves assessing structural viability, securing permits, selecting crop types based on microclimate analysis, installing modular hydroponic systems, integrating IoT sensors for environment monitoring, implementing water recycling mechanisms, training staff in vertical farming techniques, managing pest control using organic methods, coordinating with local suppliers for seed and nutrient sourcing, establishing a community engagement program for education and outreach, scheduling regular maintenance and yield optimization, and finally setting up distribution channels to local markets and restaurants. The process ensures environmental sustainability, maximizes limited urban space, and fosters local food production with a focus on innovation and community involvement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Load_Test = Transition(label='Load Test')
Permit_Apply = Transition(label='Permit Apply')

Crop_Select = Transition(label='Crop Select')

System_Design = Transition(label='System Design')

Sensor_Setup = Transition(label='Sensor Setup')

Water_Recycle = Transition(label='Water Recycle')

Staff_Train = Transition(label='Staff Train')

Pest_Control = Transition(label='Pest Control')

Supplier_Link = Transition(label='Supplier Link')

Community_Engage = Transition(label='Community Engage')

Maintenance_Plan = Transition(label='Maintenance Plan')
Yield_Monitor = Transition(label='Yield Monitor')

Market_Setup = Transition(label='Market Setup')
Logistics_Plan = Transition(label='Logistics Plan')

# Build partial order for initial site and permit assessment
initial_PO = StrictPartialOrder(nodes=[Site_Survey, Load_Test, Permit_Apply])
initial_PO.order.add_edge(Site_Survey, Load_Test)
initial_PO.order.add_edge(Load_Test, Permit_Apply)

# Crop selection depends on Permit Apply
# System Design depends on Crop Select
# Sensor Setup, Water Recycle, Staff Train, Pest Control, Supplier Link run concurrently after System Design

# Define concurrently executed activities after System Design
concurrent_after_design = StrictPartialOrder(
    nodes=[Sensor_Setup, Water_Recycle, Staff_Train, Pest_Control, Supplier_Link]
)
# no edges to allow concurrency

# Community Engage depends on Supplier Link (assumed dependency)
community_PO = StrictPartialOrder(nodes=[Supplier_Link, Community_Engage])
community_PO.order.add_edge(Supplier_Link, Community_Engage)

# Maintenance Plan and Yield Monitor run concurrently after Community Engage
maint_yield = StrictPartialOrder(nodes=[Maintenance_Plan, Yield_Monitor])
# no edges, concurrent

# Market Setup and Logistics Plan run concurrently, after maintenance and yield monitor
market_logistics = StrictPartialOrder(nodes=[Market_Setup, Logistics_Plan])
# no edges, concurrent

# Compose the right orderings:

# Crop Select after Permit Apply
crop_select_PO = StrictPartialOrder(nodes=[Permit_Apply, Crop_Select])
crop_select_PO.order.add_edge(Permit_Apply, Crop_Select)

# System Design after Crop Select
system_design_PO = StrictPartialOrder(nodes=[Crop_Select, System_Design])
system_design_PO.order.add_edge(Crop_Select, System_Design)

# Combine community_PO after concurrent_after_design by linking Supplier_Link->Community_Engage already established inside community_PO
# To keep ordering, build a PO that includes concurrent_after_design and community_Engage such that Supplier_Link->Community_Engage edge is preserved.

# Merge concurrent and community engage into one PO with edge Supplier_Link-->Community_Engage
post_design_nodes = [Sensor_Setup, Water_Recycle, Staff_Train, Pest_Control, Supplier_Link, Community_Engage]
post_design_PO = StrictPartialOrder(nodes=post_design_nodes)
# Add concurrency by having no edges except Supplier_Link-->Community_Engage
post_design_PO.order.add_edge(Supplier_Link, Community_Engage)

# Maintenance and Yield monitor after Community Engage
maint_yield_PO = StrictPartialOrder(nodes=[Community_Engage, Maintenance_Plan, Yield_Monitor])
maint_yield_PO.order.add_edge(Community_Engage, Maintenance_Plan)
maint_yield_PO.order.add_edge(Community_Engage, Yield_Monitor)

# Market Setup and Logistics Plan after Maintenance and Yield monitor
final_PO_nodes = [Maintenance_Plan, Yield_Monitor, Market_Setup, Logistics_Plan]
final_PO = StrictPartialOrder(nodes=final_PO_nodes)
final_PO.order.add_edge(Maintenance_Plan, Market_Setup)
final_PO.order.add_edge(Maintenance_Plan, Logistics_Plan)
final_PO.order.add_edge(Yield_Monitor, Market_Setup)
final_PO.order.add_edge(Yield_Monitor, Logistics_Plan)

# Now chain PO fragments together:

# Gather all nodes:
# initial_PO: Site Survey -> Load Test -> Permit Apply
# crop_select_PO: Permit Apply -> Crop Select
# system_design_PO: Crop Select -> System Design
# post_design_PO: concurrent activities after System Design (Sensor_Setup,...,Community_Engage with Supplier_Link-->Community_Engage)
# maint_yield_PO: Community Engage -> Maintenance Plan & Yield Monitor
# final_PO: Maintenance Plan & Yield Monitor -> Market Setup & Logistics Plan

# Merge initial_PO and crop_select_PO on Permit_Apply node (shared node)
# Similarly respecting order: Permit Apply->Crop Select->System Design->post_design_PO->maint_yield_PO->final_PO

# We'll merge nodes and edges manually into one StrictPartialOrder

all_nodes = [Site_Survey, Load_Test, Permit_Apply, Crop_Select, System_Design] + \
            [Sensor_Setup, Water_Recycle, Staff_Train, Pest_Control, Supplier_Link, Community_Engage] + \
            [Maintenance_Plan, Yield_Monitor, Market_Setup, Logistics_Plan]

root = StrictPartialOrder(nodes=all_nodes)

# Add initial edges
root.order.add_edge(Site_Survey, Load_Test)
root.order.add_edge(Load_Test, Permit_Apply)

# Permit Apply -> Crop Select
root.order.add_edge(Permit_Apply, Crop_Select)

# Crop Select -> System Design
root.order.add_edge(Crop_Select, System_Design)

# System Design -> concurrent_after_design
# So System Design precedes all post_design_PO nodes except Community Engage (which depends on Supplier_Link)
for n in [Sensor_Setup, Water_Recycle, Staff_Train, Pest_Control, Supplier_Link]:
    root.order.add_edge(System_Design, n)

# Supplier_Link -> Community Engage
root.order.add_edge(Supplier_Link, Community_Engage)

# Community Engage -> Maintenance Plan and Yield Monitor
root.order.add_edge(Community_Engage, Maintenance_Plan)
root.order.add_edge(Community_Engage, Yield_Monitor)

# Maintenance Plan and Yield Monitor -> Market Setup and Logistics Plan
for mnode in [Market_Setup, Logistics_Plan]:
    root.order.add_edge(Maintenance_Plan, mnode)
    root.order.add_edge(Yield_Monitor, mnode)