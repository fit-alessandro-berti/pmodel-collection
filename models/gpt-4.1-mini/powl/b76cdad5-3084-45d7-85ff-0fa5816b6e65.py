# Generated from: b76cdad5-3084-45d7-85ff-0fa5816b6e65.json
# Description: This process outlines the establishment of an urban vertical farming system within a dense metropolitan area. It includes site analysis for optimal sunlight and structural integrity, modular rack design to maximize yield per square meter, integration of hydroponic and aeroponic systems for nutrient delivery, implementation of IoT sensors for real-time monitoring, pest control using biological agents, and energy optimization through renewable sources. The process also covers regulatory compliance checks, community engagement for local sourcing, and iterative yield assessments to refine crop selection and farming techniques, ensuring sustainability and economic viability in an unconventional agricultural environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
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

# Site analysis partial order: Site Survey --> Light Analysis and Structure Check concurrently
site_analysis = StrictPartialOrder(nodes=[site_survey, light_analysis, structure_check])
site_analysis.order.add_edge(site_survey, light_analysis)
site_analysis.order.add_edge(site_survey, structure_check)

# Modular rack design after site analysis
rack_design_seq = StrictPartialOrder(nodes=[site_analysis, rack_design])
rack_design_seq.order.add_edge(site_analysis, rack_design)

# System setup after rack design
system_setup_seq = StrictPartialOrder(nodes=[rack_design_seq, system_setup])
system_setup_seq.order.add_edge(rack_design_seq, system_setup)

# Nutrient systems partial order: Nutrient Mix --> Sensor Install --> Data Sync (linear)
nutrient_sys = StrictPartialOrder(nodes=[nutrient_mix, sensor_install, data_sync])
nutrient_sys.order.add_edge(nutrient_mix, sensor_install)
nutrient_sys.order.add_edge(sensor_install, data_sync)

# Pest control and energy audit concurrent after system setup
pest_energy = StrictPartialOrder(nodes=[pest_control, energy_audit])

# Regulatory & community partial order: Compliance Review --> Community Meet
regulatory_community = StrictPartialOrder(nodes=[compliance_review, community_meet])
regulatory_community.order.add_edge(compliance_review, community_meet)

# Yield assessment loop: *(Crop Select, Yield Test + Feedback Loop)
yield_test_feedback = StrictPartialOrder(nodes=[yield_test, feedback_loop])
yield_test_feedback.order.add_edge(yield_test, feedback_loop)
yield_assessment_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_select, yield_test_feedback])

# Combine pest energy with regulatory community concurrently after system setup and nutrient system
pest_energy_reg_comm = StrictPartialOrder(nodes=[pest_energy, regulatory_community])
# No order edges inside, concurrent

# Combine nutrient system and pest/energy/reg/community concurrently (all start after system setup)
nutrient_pest_energy_reg_comm = StrictPartialOrder(nodes=[nutrient_sys, pest_energy_reg_comm])
# No intra edges, concurrent

# Now sequence: system_setup --> (nutrient + pest/energy/reg/community)
sys_and_followup = StrictPartialOrder(nodes=[system_setup, nutrient_pest_energy_reg_comm])
sys_and_followup.order.add_edge(system_setup, nutrient_pest_energy_reg_comm)

# Final root partial order: 
# (site analysis + rack design) -> system setup -> (nutrient etc.) -> yield assessment loop

root = StrictPartialOrder(
    nodes=[rack_design_seq, sys_and_followup, yield_assessment_loop]
)
root.order.add_edge(rack_design_seq, sys_and_followup)
root.order.add_edge(sys_and_followup, yield_assessment_loop)