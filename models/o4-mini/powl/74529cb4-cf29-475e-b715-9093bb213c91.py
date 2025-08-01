# Generated from: 74529cb4-cf29-475e-b715-9093bb213c91.json
# Description: This process governs the comprehensive management of urban beekeeping operations within city limits, balancing ecological sustainability, regulatory compliance, and community engagement. It includes site evaluation, hive installation, periodic health inspections, pest control, honey extraction, and data reporting. The process integrates stakeholder communication, emergency response for hive disturbances, and educational outreach programs to promote awareness and support for urban pollinators. Each step is designed to minimize environmental impact while maximizing hive productivity and public safety, adapting dynamically to seasonal changes and urban challenges such as pollution and limited green spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label="Site Survey")
permit_review    = Transition(label="Permit Review")
hive_setup       = Transition(label="Hive Setup")
colony_transfer  = Transition(label="Colony Transfer")
health_check     = Transition(label="Health Check")
pest_control     = Transition(label="Pest Control")
honey_harvest    = Transition(label="Honey Harvest")
wax_processing   = Transition(label="Wax Processing")
data_logging     = Transition(label="Data Logging")
community_alert  = Transition(label="Community Alert")
education_plan   = Transition(label="Education Plan")
stakeholder_meet = Transition(label="Stakeholder Meet")
emergency_response = Transition(label="Emergency Response")
seasonal_audit   = Transition(label="Seasonal Audit")
equipment_clean  = Transition(label="Equipment Clean")
waste_disposal   = Transition(label="Waste Disposal")

# 1) Initial setup sequence: Site Survey -> Permit Review -> Hive Setup -> Colony Transfer
setup = StrictPartialOrder(nodes=[
    site_survey, permit_review, hive_setup, colony_transfer
])
setup.order.add_edge(site_survey,    permit_review)
setup.order.add_edge(permit_review,  hive_setup)
setup.order.add_edge(hive_setup,     colony_transfer)

# 2) Main periodic cycle: Health Check -> Pest Control -> Honey Harvest -> Wax Processing -> Data Logging
#    then concurrently Community Alert, Education Plan, Stakeholder Meet, Seasonal Audit
cycle = StrictPartialOrder(nodes=[
    health_check, pest_control, honey_harvest, wax_processing, data_logging,
    community_alert, education_plan, stakeholder_meet, seasonal_audit
])
cycle.order.add_edge(health_check,  pest_control)
cycle.order.add_edge(pest_control,  honey_harvest)
cycle.order.add_edge(honey_harvest, wax_processing)
cycle.order.add_edge(wax_processing, data_logging)
for nxt in [community_alert, education_plan, stakeholder_meet, seasonal_audit]:
    cycle.order.add_edge(data_logging, nxt)

# 3) Emergency response subprocess (triggered optionally in the loop)
emergency = StrictPartialOrder(nodes=[emergency_response])
# (no internal ordering needed for a single-step subprocess)

# 4) Loop: repeat the 'cycle' until exit; if an emergency occurs, handle it then repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle, emergency])

# 5) Final cleanup: Equipment Clean -> Waste Disposal
cleanup = StrictPartialOrder(nodes=[equipment_clean, waste_disposal])
cleanup.order.add_edge(equipment_clean, waste_disposal)

# 6) Assemble the root POWL: setup -> loop -> cleanup
root = StrictPartialOrder(nodes=[setup, loop, cleanup])
root.order.add_edge(setup, loop)
root.order.add_edge(loop, cleanup)