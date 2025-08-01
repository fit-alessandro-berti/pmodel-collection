# Generated from: 20c75e7c-d1c0-4c5c-a0b8-90ec024c899c.json
# Description: This process outlines the end-to-end setup of an urban vertical farm in a repurposed industrial building. It involves site assessment, structural modifications, environmental system installation, crop selection based on microclimate analysis, automated irrigation programming, nutrient solution formulation, pest control integration using biocontrol agents, staff training on hydroponic techniques, ongoing yield monitoring through IoT sensors, energy consumption optimization, waste recycling protocols, market distribution planning, regulatory compliance verification, and continuous improvement feedback loops to ensure sustainability and profitability in an atypical urban agricultural context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_assess      = Transition(label='Site Assess')
structure_mod    = Transition(label='Structure Mod')
enviro_install   = Transition(label='Enviro Install')
crop_select      = Transition(label='Crop Select')
irrigation_set   = Transition(label='Irrigation Set')
nutrient_mix     = Transition(label='Nutrient Mix')
pest_control     = Transition(label='Pest Control')
staff_train      = Transition(label='Staff Train')
yield_monitor    = Transition(label='Yield Monitor')
energy_audit     = Transition(label='Energy Audit')
waste_recycle    = Transition(label='Waste Recycle')
market_plan      = Transition(label='Market Plan')
compliance_check = Transition(label='Compliance Check')
feedback_loop    = Transition(label='Feedback Loop')
tech_upgrade     = Transition(label='Tech Upgrade')

# Build the initial sequential + concurrent phase:
#  Site Assess -> Structure Mod -> Enviro Install -> Crop Select
#    -> Irrigation Set -> Nutrient Mix -> Pest Control -> Staff Train
# After Staff Train, the five monitoring/planning tasks can run in parallel
initial_and_monitor = StrictPartialOrder(nodes=[
    site_assess, structure_mod, enviro_install, crop_select,
    irrigation_set, nutrient_mix, pest_control, staff_train,
    yield_monitor, energy_audit, waste_recycle, market_plan, compliance_check
])
# sequential chain for setup
initial_and_monitor.order.add_edge(site_assess,   structure_mod)
initial_and_monitor.order.add_edge(structure_mod, enviro_install)
initial_and_monitor.order.add_edge(enviro_install, crop_select)
initial_and_monitor.order.add_edge(crop_select,    irrigation_set)
initial_and_monitor.order.add_edge(irrigation_set, nutrient_mix)
initial_and_monitor.order.add_edge(nutrient_mix,   pest_control)
initial_and_monitor.order.add_edge(pest_control,   staff_train)
# after staff training, the five tasks proceed concurrently
for m in [yield_monitor, energy_audit, waste_recycle, market_plan, compliance_check]:
    initial_and_monitor.order.add_edge(staff_train, m)

# Build the feedback/upgrade body of the loop
feedback_body = StrictPartialOrder(nodes=[feedback_loop, tech_upgrade])
feedback_body.order.add_edge(feedback_loop, tech_upgrade)

# Combine into a LOOP: do the setup+monitor phase once, 
# then iteratively do feedback -> tech upgrade -> back
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[initial_and_monitor, feedback_body]
)