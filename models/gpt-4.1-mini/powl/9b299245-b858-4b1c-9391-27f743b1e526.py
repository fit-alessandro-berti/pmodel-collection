# Generated from: 9b299245-b858-4b1c-9391-27f743b1e526.json
# Description: This process outlines the establishment of a vertical farming facility in an urban environment, integrating advanced hydroponic systems with IoT monitoring and renewable energy sources. It involves site selection considering zoning laws, procuring modular grow units, installing climate control, and integrating AI-driven nutrient delivery. The workflow includes stakeholder coordination, regulatory compliance verification, staff training for automated systems, and launching pilot crop cycles. Continuous monitoring and iterative adjustments optimize yield and energy usage, while waste recycling strategies enhance sustainability. The process culminates in establishing distribution partnerships for fresh produce within local markets, ensuring a closed-loop urban agriculture model that addresses food security and environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities
site_survey = Transition(label='Site Survey')
permit_check = Transition(label='Permit Check')
module_order = Transition(label='Module Order')
foundation_prep = Transition(label='Foundation Prep')
unit_install = Transition(label='Unit Install')
hydro_setup = Transition(label='Hydro Setup')
climate_config = Transition(label='Climate Config')
iot_deploy = Transition(label='IoT Deploy')
ai_integrate = Transition(label='AI Integrate')
system_test = Transition(label='System Test')
staff_train = Transition(label='Staff Train')
pilot_plant = Transition(label='Pilot Plant')
monitor_data = Transition(label='Monitor Data')
yield_adjust = Transition(label='Yield Adjust')
waste_cycle = Transition(label='Waste Cycle')
market_link = Transition(label='Market Link')
report_review = Transition(label='Report Review')

# Step 1: Site selection and approval
site_and_permit = StrictPartialOrder(nodes=[site_survey, permit_check])
site_and_permit.order.add_edge(site_survey, permit_check)

# Step 2: Procurement and installation preparation
prep = StrictPartialOrder(nodes=[module_order, foundation_prep])
# module_order and foundation_prep can be concurrent (e.g. order modules while prepping foundation)

# Step 3: Installation and setup sequence after prep
install_seq = StrictPartialOrder(nodes=[unit_install, hydro_setup, climate_config, iot_deploy, ai_integrate, system_test])
install_seq.order.add_edge(unit_install, hydro_setup)
install_seq.order.add_edge(hydro_setup, climate_config)
install_seq.order.add_edge(climate_config, iot_deploy)
install_seq.order.add_edge(iot_deploy, ai_integrate)
install_seq.order.add_edge(ai_integrate, system_test)

# Step 4: Staff training after system test
staff_and_pilot = StrictPartialOrder(nodes=[staff_train, pilot_plant])
staff_and_pilot.order.add_edge(staff_train, pilot_plant)

# Step 5: Monitoring loop: Monitor data followed by yield adjustment and waste recycling, repeat or exit
# Represent the loop as loop = *(A,B) where:
#   A = Monitor Data
#   B = StrictPartialOrder([Yield Adjust, Waste Cycle])
yield_waste = StrictPartialOrder(nodes=[yield_adjust, waste_cycle])
# they are concurrent (no edges)
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[monitor_data, yield_waste])

# Step 6: Reporting and market linkage after pilot plant and loop
post_pilot = StrictPartialOrder(nodes=[pilot_plant, loop_monitor, report_review, market_link])
post_pilot.order.add_edge(pilot_plant, loop_monitor)
post_pilot.order.add_edge(loop_monitor, report_review)
post_pilot.order.add_edge(report_review, market_link)

# Now combine all partial orders in sequence with possible concurrency:

# Combine step1 and step2: permit_check must finish before foundation_prep/module_order start?
# They can be partially ordered: site_survey -> permit_check -> prep

step1_2 = StrictPartialOrder(nodes=[site_and_permit, prep])
step1_2.order.add_edge(site_and_permit, prep)

# Combine step1_2 and install_seq: foundation_prep/order modules must finish before install starts
# We must enforce install_seq after prep (install_seq depends on foundation_prep and module_order)
step1_2_install = StrictPartialOrder(nodes=[step1_2, install_seq])
step1_2_install.order.add_edge(step1_2, install_seq)

# Combine with staff and pilot after system test
install_staff = StrictPartialOrder(nodes=[step1_2_install, staff_and_pilot])
install_staff.order.add_edge(step1_2_install, staff_and_pilot)

# Combine with monitoring loop and reporting after pilot_plant
final_po = StrictPartialOrder(nodes=[install_staff, post_pilot])
final_po.order.add_edge(install_staff, post_pilot)

# Final root
root = final_po