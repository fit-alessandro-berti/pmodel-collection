# Generated from: 2975a843-6c5b-4be2-9e86-eb8f39c8e600.json
# Description: This process involves the establishment and operationalization of an urban vertical farming system within a densely populated city environment. It begins with site selection based on environmental assessments and zoning regulations, proceeds through modular infrastructure assembly, and integrates IoT sensor deployment for real-time monitoring. Nutrient solution preparation and seed germination are carefully coordinated with automated lighting and climate controls to optimize plant growth cycles. The process further includes pest management via biological controls, waste recycling for sustainability, and periodic data analysis to refine growth algorithms. Harvesting is synchronized with distribution logistics to ensure freshness, while customer feedback loops inform continuous improvement of crop varieties and system efficiency. Overall, the process emphasizes sustainability, technology integration, and urban resource optimization to deliver fresh produce with minimal environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
site_select      = Transition(label='Site Select')
env_assess       = Transition(label='Env Assess')
zoning_check     = Transition(label='Zoning Check')
modular_build    = Transition(label='Modular Build')
sensor_deploy    = Transition(label='Sensor Deploy')
nutrient_prep    = Transition(label='Nutrient Prep')
seed_germinate   = Transition(label='Seed Germinate')
light_control    = Transition(label='Light Control')
climate_adjust   = Transition(label='Climate Adjust')
pest_manage      = Transition(label='Pest Manage')
waste_recycle    = Transition(label='Waste Recycle')
data_analyze     = Transition(label='Data Analyze')
feedback_loop    = Transition(label='Feedback Loop')
harvest_sync     = Transition(label='Harvest Sync')
logistics_plan   = Transition(label='Logistics Plan')

# Core growth operations: run in parallel each cycle
core_growth = StrictPartialOrder(nodes=[
    light_control, climate_adjust, pest_manage, waste_recycle
])
# Periodic analysis & feedback before next cycle
analyze_and_feedback = StrictPartialOrder(nodes=[
    data_analyze, feedback_loop
])
analyze_and_feedback.order.add_edge(data_analyze, feedback_loop)

# Loop structure: each iteration = core growth, then analysis&feedback, then maybe repeat
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[core_growth, analyze_and_feedback]
)

# Build the top‐level process as a partial order
root = StrictPartialOrder(nodes=[
    env_assess, zoning_check, site_select,
    modular_build, sensor_deploy,
    nutrient_prep, seed_germinate,
    growth_loop,
    harvest_sync, logistics_plan
])

# Dependencies
root.order.add_edge(env_assess, site_select)
root.order.add_edge(zoning_check, site_select)
root.order.add_edge(site_select, modular_build)
root.order.add_edge(modular_build, sensor_deploy)
root.order.add_edge(sensor_deploy, nutrient_prep)
root.order.add_edge(nutrient_prep, seed_germinate)
root.order.add_edge(seed_germinate, growth_loop)
root.order.add_edge(growth_loop, harvest_sync)
root.order.add_edge(harvest_sync, logistics_plan)