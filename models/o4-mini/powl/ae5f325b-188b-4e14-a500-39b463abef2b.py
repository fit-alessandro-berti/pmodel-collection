# Generated from: ae5f325b-188b-4e14-a500-39b463abef2b.json
# Description: This process governs the loaning of rare artworks between international museums involving complex logistics, legal compliance, condition verification, and insurance arrangements. It begins with curator selection, followed by provenance validation and conservation assessment. Customs clearance and specialized packaging are coordinated alongside climate-controlled transport planning. Upon arrival, condition re-verification, installation setup, and security calibration occur. The process concludes with public unveiling, ongoing condition monitoring during display, and final repatriation with detailed reporting to all stakeholders.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL Transitions
curator_select    = Transition(label='Curator Select')
provenance_check  = Transition(label='Provenance Check')
condition_assess  = Transition(label='Condition Assess')
legal_review      = Transition(label='Legal Review')
insurance_setup   = Transition(label='Insurance Setup')
packaging_plan    = Transition(label='Packaging Plan')
customs_clear     = Transition(label='Customs Clear')
transport_book    = Transition(label='Transport Book')
climate_control   = Transition(label='Climate Control')
arrival_inspect   = Transition(label='Arrival Inspect')
install_setup     = Transition(label='Install Setup')
security_calibrate= Transition(label='Security Calibrate')
public_unveil     = Transition(label='Public Unveil')
condition_monitor = Transition(label='Condition Monitor')
return_arrange    = Transition(label='Return Arrange')
final_report      = Transition(label='Final Report')

# Create the root partial order with all nodes
nodes = [
    curator_select, provenance_check, condition_assess,
    legal_review, insurance_setup,
    packaging_plan, customs_clear, transport_book, climate_control,
    arrival_inspect, install_setup, security_calibrate,
    public_unveil, condition_monitor, return_arrange, final_report
]
root = StrictPartialOrder(nodes=nodes)

# Define dependencies (-->)
# 1. Curator Select precedes provenance check and condition assessment
root.order.add_edge(curator_select, provenance_check)
root.order.add_edge(curator_select, condition_assess)

# 2. After provenance & condition assessments, do legal review & insurance setup
root.order.add_edge(provenance_check, legal_review)
root.order.add_edge(provenance_check, insurance_setup)
root.order.add_edge(condition_assess, insurance_setup)

# 3. Once legal & insurance are done, coordinate packaging, customs, transport & climate
for prep in (packaging_plan, customs_clear, transport_book, climate_control):
    root.order.add_edge(legal_review, prep)
    root.order.add_edge(insurance_setup, prep)

# 4. Logistics tasks precede arrival inspection
for prep in (packaging_plan, customs_clear, transport_book, climate_control):
    root.order.add_edge(prep, arrival_inspect)

# 5. Arrival inspection precedes installation & security calibration
root.order.add_edge(arrival_inspect, install_setup)
root.order.add_edge(arrival_inspect, security_calibrate)

# 6. Installation & security precede the public unveiling
root.order.add_edge(install_setup, public_unveil)
root.order.add_edge(security_calibrate, public_unveil)

# 7. After unveiling: condition monitoring, then return arrangement, then final report
root.order.add_edge(public_unveil, condition_monitor)
root.order.add_edge(condition_monitor, return_arrange)
root.order.add_edge(return_arrange, final_report)