# Generated from: 5c0964cc-03e8-438b-9125-153d34538c78.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming facility within a densely populated city. It includes site selection based on sunlight and accessibility, modular system design for space optimization, installation of controlled environment agriculture technologies such as LED lighting and hydroponic systems, integration of IoT sensors for real-time monitoring of humidity, temperature, and nutrient levels, and development of automated irrigation and nutrient delivery schedules. The process further covers staff training for specialized urban farming techniques, implementation of waste recycling protocols, coordination with local suppliers for organic inputs, compliance with municipal agricultural regulations, and marketing strategies tailored for urban consumers. Finally, it involves continuous performance evaluation and system upgrades to maximize yield and sustainability in a challenging urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
light_analysis   = Transition(label='Light Analysis')
system_design    = Transition(label='System Design')
tech_install     = Transition(label='Tech Install')
sensor_setup     = Transition(label='Sensor Setup')
irrigation_plan  = Transition(label='Irrigation Plan')
nutrient_mix     = Transition(label='Nutrient Mix')
staff_training   = Transition(label='Staff Training')
waste_protocol   = Transition(label='Waste Protocol')
supplier_sync    = Transition(label='Supplier Sync')
regulation_check = Transition(label='Regulation Check')
market_study     = Transition(label='Market Study')
launch_event     = Transition(label='Launch Event')
performance_audit= Transition(label='Performance Audit')
system_upgrade   = Transition(label='System Upgrade')

# Define the loop for continuous evaluation and upgrade
audit_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[performance_audit, system_upgrade]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_survey, light_analysis, system_design, tech_install, sensor_setup,
    irrigation_plan, nutrient_mix, staff_training, waste_protocol,
    supplier_sync, regulation_check, market_study, launch_event, audit_loop
])

# Add control‐flow edges
root.order.add_edge(site_survey, light_analysis)
root.order.add_edge(light_analysis, system_design)
root.order.add_edge(system_design, tech_install)
root.order.add_edge(tech_install, sensor_setup)

# After sensors are in place, multiple preparatory tasks can run in parallel
for task in [irrigation_plan, nutrient_mix, staff_training,
             waste_protocol, supplier_sync, regulation_check, market_study]:
    root.order.add_edge(sensor_setup, task)
    root.order.add_edge(task, launch_event)

# Launch event precedes the continuous audit‐upgrade loop
root.order.add_edge(launch_event, audit_loop)