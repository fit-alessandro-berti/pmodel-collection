# Generated from: 06e0aa93-0c99-4889-a361-f7da4f69fa6b.json
# Description: This process outlines the establishment of an urban rooftop farming system on commercial buildings in densely populated areas. It involves site analysis for structural integrity, microclimate assessment, and local biodiversity considerations. The workflow includes selecting suitable crops based on sunlight exposure and pollution levels, installing modular hydroponic systems, integrating IoT sensors for real-time monitoring, and establishing water recycling loops. The process also requires community engagement for education and maintenance, regulatory compliance checks, and developing a logistics plan for produce distribution directly to local markets. Continuous performance evaluation and iterative improvements ensure sustainability and scalability of the rooftop farm over time.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Load_Test = Transition(label='Load Test')
Climate_Map = Transition(label='Climate Map')
Crop_Select = Transition(label='Crop Select')
System_Design = Transition(label='System Design')
Hydro_Install = Transition(label='Hydro Install')
Sensor_Setup = Transition(label='Sensor Setup')
Water_Loop = Transition(label='Water Loop')
Soil_Prep = Transition(label='Soil Prep')
Planting_Day = Transition(label='Planting Day')
Data_Sync = Transition(label='Data Sync')
Compliance_Check = Transition(label='Compliance Check')
Community_Meet = Transition(label='Community Meet')
Market_Plan = Transition(label='Market Plan')
Maintenance = Transition(label='Maintenance')
Performance_Eval = Transition(label='Performance Eval')

skip = SilentTransition()

# Phase 1: Site analysis 
# (Site Survey -> Load Test || Climate Map)
site_analysis = StrictPartialOrder(nodes=[Site_Survey, Load_Test, Climate_Map])
site_analysis.order.add_edge(Site_Survey, Load_Test)
# Climate_Map concurrent with Load_Test (no order edge)

# Phase 2: Crop selection based on sunlight and pollution info
crop_selection = Crop_Select

# Phase 3: System Design and Hydroponic installation and Sensor setup
# (System Design -> Hydro Install -> Sensor Setup)
sys_design_flow = StrictPartialOrder(nodes=[System_Design, Hydro_Install, Sensor_Setup])
sys_design_flow.order.add_edge(System_Design, Hydro_Install)
sys_design_flow.order.add_edge(Hydro_Install, Sensor_Setup)

# Phase 4: Water recycling loop (Water Loop)
# Water Loop is a loop node with body Water Loop activity and exit skip
water_loop = OperatorPOWL(operator=Operator.LOOP, children=[Water_Loop, skip])

# Phase 5: Soil Prep and Planting Day (ordered)
soil_planting = StrictPartialOrder(nodes=[Soil_Prep, Planting_Day])
soil_planting.order.add_edge(Soil_Prep, Planting_Day)

# Phase 6: Data sync (periodic data sync with sensors)
data_sync = Data_Sync

# Phase 7: Compliance Check (regulated check)
compliance_check = Compliance_Check

# Phase 8: Community engagement and education
community_engagement = Community_Meet

# Phase 9: Market plan and logistics
market_plan = Market_Plan

# Phase 10: Maintenance (periodic activity)
maintenance = Maintenance

# Phase 11: Performance evaluation and improvement loop
# Performance Eval loop with Maintenance
perf_loop = OperatorPOWL(operator=Operator.LOOP, children=[Performance_Eval, maintenance])

# Compose the overall partial order

# Combine system design, water_loop and crop selection partial orders with concurrency and orderings:
# site_analysis -> Crop_Select -> System Design flow -> Water Loop loop
phase1_to_4 = StrictPartialOrder(nodes=[site_analysis, crop_selection, sys_design_flow, water_loop])
phase1_to_4.order.add_edge(site_analysis, crop_selection)
phase1_to_4.order.add_edge(crop_selection, sys_design_flow)
phase1_to_4.order.add_edge(sys_design_flow, water_loop)

# Combine soil/planting and data sync with compliance check sequentially:
phase5_to_7 = StrictPartialOrder(nodes=[soil_planting, data_sync, compliance_check])
phase5_to_7.order.add_edge(soil_planting, data_sync)
phase5_to_7.order.add_edge(data_sync, compliance_check)

# Combine community engagement, market plan,
# then join maintenance and performance loop (perf_loop instead of separate maintenance)
phase8_to_11 = StrictPartialOrder(nodes=[community_engagement, market_plan, perf_loop])
phase8_to_11.order.add_edge(community_engagement, market_plan)
phase8_to_11.order.add_edge(market_plan, perf_loop)

# Combine first big block, second block, and third block in sequential order:
root = StrictPartialOrder(
    nodes=[phase1_to_4, phase5_to_7, phase8_to_11]
)
root.order.add_edge(phase1_to_4, phase5_to_7)
root.order.add_edge(phase5_to_7, phase8_to_11)