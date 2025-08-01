# Generated from: 69b8d756-8b4a-4843-ad68-5d07c066f17a.json
# Description: This process outlines the complex and multidisciplinary steps required to establish a sustainable urban rooftop farm. It involves site assessment, structural analysis, soil preparation, ecosystem integration, irrigation system design, seed selection, crop rotation planning, pest management, community engagement, and ongoing monitoring to ensure optimal yield and environmental benefits. The process also incorporates regulatory compliance, safety measures, and logistics coordination for material delivery and waste management, reflecting the unique challenges of transforming urban spaces into productive agricultural sites.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey       = Transition(label='Site Survey')
regulation_check  = Transition(label='Regulation Check')
load_test         = Transition(label='Load Test')
safety_drill      = Transition(label='Safety Drill')
logistics_setup   = Transition(label='Logistics Setup')
soil_mix          = Transition(label='Soil Mix')
irrigation_plan   = Transition(label='Irrigation Plan')
water_testing     = Transition(label='Water Testing')
seed_selection    = Transition(label='Seed Selection')
planting_grid     = Transition(label='Planting Grid')
crop_rotation     = Transition(label='Crop Rotation')
pest_control      = Transition(label='Pest Control')
growth_monitor    = Transition(label='Growth Monitor')
harvest_schedule  = Transition(label='Harvest Schedule')
waste_removal     = Transition(label='Waste Removal')
tool_sterilize    = Transition(label='Tool Sterilize')
community_meet    = Transition(label='Community Meet')

# Loop structure: monitor growth, then either exit or do pest control and monitor again
monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, pest_control]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    regulation_check,
    load_test,
    safety_drill,
    logistics_setup,
    soil_mix,
    irrigation_plan,
    water_testing,
    seed_selection,
    planting_grid,
    crop_rotation,
    monitoring_loop,
    harvest_schedule,
    waste_removal,
    tool_sterilize,
    community_meet
])

# Define the control-flow dependencies
root.order.add_edge(site_survey,      regulation_check)
root.order.add_edge(regulation_check, load_test)
root.order.add_edge(load_test,        safety_drill)
root.order.add_edge(safety_drill,     logistics_setup)
root.order.add_edge(logistics_setup,  soil_mix)
root.order.add_edge(soil_mix,         irrigation_plan)
root.order.add_edge(irrigation_plan,  water_testing)
root.order.add_edge(water_testing,    seed_selection)
root.order.add_edge(seed_selection,   planting_grid)
root.order.add_edge(planting_grid,    crop_rotation)
root.order.add_edge(crop_rotation,    monitoring_loop)
root.order.add_edge(monitoring_loop,  harvest_schedule)
root.order.add_edge(harvest_schedule, waste_removal)
root.order.add_edge(waste_removal,    tool_sterilize)
root.order.add_edge(tool_sterilize,   community_meet)