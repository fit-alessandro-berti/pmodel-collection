# Generated from: abbba611-d6ff-4635-a027-a152683b7407.json
# Description: This process outlines the comprehensive setup of an urban vertical farm integrating advanced hydroponics and IoT technologies to maximize crop yield in limited city spaces. It begins with site assessment and resource analysis, followed by modular system design and procurement of specialized equipment. Installation involves precise environmental control calibration, nutrient solution formulation, and sensor network deployment. Continuous monitoring and adaptive management optimize plant growth cycles, while automated harvesting and post-harvest processing ensure quality and efficiency. The process concludes with sustainability evaluation and scalability planning to expand operations in urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey     = Transition(label='Site Survey')
resource_audit  = Transition(label='Resource Audit')
system_design   = Transition(label='System Design')
equipment_order = Transition(label='Equipment Order')
structure_build = Transition(label='Structure Build')
install_pumps   = Transition(label='Install Pumps')
calibrate_sensors = Transition(label='Calibrate Sensors')
mix_nutrients   = Transition(label='Mix Nutrients')
deploy_iot      = Transition(label='Deploy IoT')
plant_seeding   = Transition(label='Plant Seeding')
monitor_growth  = Transition(label='Monitor Growth')
adjust_lighting = Transition(label='Adjust Lighting')
harvest_crops   = Transition(label='Harvest Crops')
process_yield   = Transition(label='Process Yield')
evaluate_impact = Transition(label='Evaluate Impact')
plan_expansion  = Transition(label='Plan Expansion')

# Define the monitoring loop: Monitor Growth then optionally Adjust Lighting and repeat
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth, adjust_lighting])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, resource_audit,
    system_design, equipment_order, structure_build,
    install_pumps, calibrate_sensors, mix_nutrients, deploy_iot,
    plant_seeding, growth_loop,
    harvest_crops, process_yield,
    evaluate_impact, plan_expansion
])

# Sequence: site survey -> resource audit -> system design -> equipment order -> structure build
root.order.add_edge(site_survey, resource_audit)
root.order.add_edge(resource_audit, system_design)
root.order.add_edge(system_design, equipment_order)
root.order.add_edge(equipment_order, structure_build)

# From structure build to the four parallel installation tasks
for task in [install_pumps, calibrate_sensors, mix_nutrients, deploy_iot]:
    root.order.add_edge(structure_build, task)

# After all install tasks complete, proceed to plant seeding
for task in [install_pumps, calibrate_sensors, mix_nutrients, deploy_iot]:
    root.order.add_edge(task, plant_seeding)

# Plant seeding -> growth loop -> harvest -> processing -> evaluation -> expansion
root.order.add_edge(plant_seeding, growth_loop)
root.order.add_edge(growth_loop, harvest_crops)
root.order.add_edge(harvest_crops, process_yield)
root.order.add_edge(process_yield, evaluate_impact)
root.order.add_edge(evaluate_impact, plan_expansion)