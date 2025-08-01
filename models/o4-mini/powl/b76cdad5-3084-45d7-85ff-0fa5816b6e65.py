# Generated from: b76cdad5-3084-45d7-85ff-0fa5816b6e65.json
# Description: This process outlines the establishment of an urban vertical farming system within a dense metropolitan area. It includes site analysis for optimal sunlight and structural integrity, modular rack design to maximize yield per square meter, integration of hydroponic and aeroponic systems for nutrient delivery, implementation of IoT sensors for real-time monitoring, pest control using biological agents, and energy optimization through renewable sources. The process also covers regulatory compliance checks, community engagement for local sourcing, and iterative yield assessments to refine crop selection and farming techniques, ensuring sustainability and economic viability in an unconventional agricultural environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
site_survey = Transition(label='Site Survey')
light_analysis = Transition(label='Light Analysis')
structure_check = Transition(label='Structure Check')
rack_design = Transition(label='Rack Design')
system_setup = Transition(label='System Setup')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_install = Transition(label='Sensor Install')
data_sync = Transition(label='Data Sync')
pest_control = Transition(label='Pest Control')
energy_audit = Transition(label='Energy Audit')
compliance_review = Transition(label='Compliance Review')
community_meet = Transition(label='Community Meet')
crop_select = Transition(label='Crop Select')
yield_test = Transition(label='Yield Test')
feedback_loop = Transition(label='Feedback Loop')

# Define the loop body for iterative yield assessment
body = StrictPartialOrder(nodes=[yield_test, feedback_loop])
body.order.add_edge(yield_test, feedback_loop)

# Loop operator: Crop Select followed by Yield Test+Feedback Loop, repeating until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_select, body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, light_analysis, structure_check, rack_design,
    system_setup, nutrient_mix,
    sensor_install, data_sync,
    pest_control, energy_audit, compliance_review, community_meet,
    loop
])

# Site analysis
root.order.add_edge(site_survey, light_analysis)
root.order.add_edge(site_survey, structure_check)
root.order.add_edge(light_analysis, rack_design)
root.order.add_edge(structure_check, rack_design)

# Rack design to system setup and nutrient mix
root.order.add_edge(rack_design, system_setup)
root.order.add_edge(system_setup, nutrient_mix)

# After nutrient mix: install sensors, pest control, energy audit, compliance, community meet
root.order.add_edge(nutrient_mix, sensor_install)
root.order.add_edge(nutrient_mix, pest_control)
root.order.add_edge(nutrient_mix, energy_audit)
root.order.add_edge(nutrient_mix, compliance_review)
root.order.add_edge(nutrient_mix, community_meet)

# Sensor installation to data synchronization
root.order.add_edge(sensor_install, data_sync)

# All preparatory tasks must complete before starting the yield assessment loop
root.order.add_edge(data_sync, loop)
root.order.add_edge(pest_control, loop)
root.order.add_edge(energy_audit, loop)
root.order.add_edge(compliance_review, loop)
root.order.add_edge(community_meet, loop)