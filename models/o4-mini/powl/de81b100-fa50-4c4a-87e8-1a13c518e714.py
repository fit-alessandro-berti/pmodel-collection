# Generated from: de81b100-fa50-4c4a-87e8-1a13c518e714.json
# Description: This process describes the establishment of a sustainable urban vertical farming system within a repurposed city warehouse. It involves steps such as environmental assessment, modular rack design, nutrient solution formulation, automated lighting calibration, and integration of IoT sensors for real-time monitoring. The process also includes obtaining necessary permits, recruiting specialized agronomists, establishing supply chains for organic seeds, implementing waste recycling protocols, and training staff on hydroponic and aeroponic techniques. The goal is to create a scalable, energy-efficient food production system that reduces urban food deserts and promotes local sourcing with minimal environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey    = Transition(label='Site Survey')
permit_acquire = Transition(label='Permit Acquire')
rack_design    = Transition(label='Rack Design')
seed_selection = Transition(label='Seed Selection')
nutrient_mix   = Transition(label='Nutrient Mix')
lighting_setup = Transition(label='Lighting Setup')
sensor_install = Transition(label='Sensor Install')
system_test    = Transition(label='System Test')
staff_hire     = Transition(label='Staff Hire')
training_lead  = Transition(label='Training Lead')
waste_manage   = Transition(label='Waste Manage')
supply_chain   = Transition(label='Supply Chain')
harvest_plan   = Transition(label='Harvest Plan')
distribution   = Transition(label='Distribution')

# Define loop for crop cycles with monitoring
crop_cycle     = Transition(label='Crop Cycle')
data_monitor   = Transition(label='Data Monitor')
cycle_loop     = OperatorPOWL(operator=Operator.LOOP, children=[crop_cycle, data_monitor])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    site_survey, permit_acquire, rack_design, seed_selection, nutrient_mix,
    lighting_setup, sensor_install, system_test, staff_hire, training_lead,
    waste_manage, supply_chain, harvest_plan, cycle_loop, distribution
])

# Define control-flow dependencies
# Initial survey and permit
root.order.add_edge(site_survey, permit_acquire)

# After permit, parallel branches: design, selection, mixing, waste protocol, hiring
for nxt in [rack_design, seed_selection, nutrient_mix, waste_manage, staff_hire]:
    root.order.add_edge(permit_acquire, nxt)

# Design path: rack → lighting → sensors → system test
root.order.add_edge(rack_design, lighting_setup)
root.order.add_edge(lighting_setup, sensor_install)
root.order.add_edge(sensor_install, system_test)

# Waste management also tested
root.order.add_edge(waste_manage, system_test)

# Seed & nutrient feed supply chain
root.order.add_edge(seed_selection, supply_chain)
root.order.add_edge(nutrient_mix, supply_chain)

# Hiring path: staff hire → training
root.order.add_edge(staff_hire, training_lead)

# After system test and training, plan harvest
root.order.add_edge(system_test, harvest_plan)
root.order.add_edge(training_lead, harvest_plan)

# Harvest plan precedes the crop-cycle loop; supply chain must be ready before looping
root.order.add_edge(harvest_plan, cycle_loop)
root.order.add_edge(supply_chain, cycle_loop)

# After loop exit, distribute
root.order.add_edge(cycle_loop, distribution)