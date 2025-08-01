# Generated from: a48d8095-74ea-4c4c-abc5-1e1a0bede2e0.json
# Description: This process outlines the complex steps required to establish a fully operational urban vertical farm within a constrained city environment. It involves site analysis, environmental impact assessment, modular system design, nutrient cycling integration, automation programming, stakeholder engagement, and regulatory compliance. The process demands coordination between agronomists, engineers, and city officials to ensure sustainable production of high-yield crops using limited space and resources, while maximizing energy efficiency and minimizing waste generation. Each phase requires iterative testing and optimization to adapt to local climatic conditions and market demands, ensuring profitability and ecological balance.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey    = Transition(label='Site Survey')
impact_study   = Transition(label='Impact Study')
system_design  = Transition(label='System Design')
module_build   = Transition(label='Module Build')
water_setup    = Transition(label='Water Setup')
nutrient_mix   = Transition(label='Nutrient Mix')
sensor_install = Transition(label='Sensor Install')
automation_code= Transition(label='Automation Code')
energy_audit   = Transition(label='Energy Audit')
waste_plan     = Transition(label='Waste Plan')
stakeholder_meet = Transition(label='Stakeholder Meet')
permit_apply   = Transition(label='Permit Apply')
crop_trial     = Transition(label='Crop Trial')
data_review    = Transition(label='Data Review')
market_launch  = Transition(label='Market Launch')

# Phase 1: Site Survey -> Impact Study -> System Design
phase1 = StrictPartialOrder(nodes=[site_survey, impact_study, system_design])
phase1.order.add_edge(site_survey, impact_study)
phase1.order.add_edge(impact_study, system_design)

# Loop body: Module Build -> Water Setup -> Nutrient Mix -> Sensor Install
#             -> Automation Code -> Energy Audit -> Waste Plan -> Crop Trial -> Data Review
loop_body = StrictPartialOrder(nodes=[
    module_build, water_setup, nutrient_mix, sensor_install,
    automation_code, energy_audit, waste_plan, crop_trial, data_review
])
loop_body.order.add_edge(module_build, water_setup)
loop_body.order.add_edge(water_setup, nutrient_mix)
loop_body.order.add_edge(nutrient_mix, sensor_install)
loop_body.order.add_edge(sensor_install, automation_code)
loop_body.order.add_edge(automation_code, energy_audit)
loop_body.order.add_edge(energy_audit, waste_plan)
loop_body.order.add_edge(waste_plan, crop_trial)
loop_body.order.add_edge(crop_trial, data_review)

# Iterative optimization: execute phase1, then optionally repeat loop_body + phase1
loop = OperatorPOWL(operator=Operator.LOOP, children=[phase1, loop_body])

# Final phase: Stakeholder Meet -> Permit Apply -> Market Launch
final_phase = StrictPartialOrder(nodes=[stakeholder_meet, permit_apply, market_launch])
final_phase.order.add_edge(stakeholder_meet, permit_apply)
final_phase.order.add_edge(permit_apply, market_launch)

# Root model
root = StrictPartialOrder(nodes=[loop, final_phase])
root.order.add_edge(loop, final_phase)