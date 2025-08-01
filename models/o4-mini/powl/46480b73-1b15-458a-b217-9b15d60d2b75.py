# Generated from: 46480b73-1b15-458a-b217-9b15d60d2b75.json
# Description: This process manages the unique supply chain for urban beekeeping operations, integrating local environmental assessments, hive placement approvals, and specialized equipment distribution to city locations. It involves coordination with municipal authorities for permits, sourcing sustainable bee-friendly plants, monitoring hive health via IoT devices, and coordinating seasonal honey extraction and packaging. The process ensures compliance with urban regulations while supporting biodiversity and community engagement through educational workshops and local market distribution, requiring adaptive logistics and stakeholder communication in a non-traditional agricultural setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
permit_request   = Transition(label='Permit Request')
permit_approval  = Transition(label='Permit Approval')
hive_assembly    = Transition(label='Hive Assembly')
equipment_check  = Transition(label='Equipment Check')
iot_setup        = Transition(label='IoT Setup')
local_sourcing   = Transition(label='Local Sourcing')
plant_selection  = Transition(label='Plant Selection')
community_meet   = Transition(label='Community Meet')
hive_placement   = Transition(label='Hive Placement')
health_monitor   = Transition(label='Health Monitor')
seasonal_extract = Transition(label='Seasonal Extract')
honey_filter     = Transition(label='Honey Filter')
packaging_prep   = Transition(label='Packaging Prep')
market_dispatch  = Transition(label='Market Dispatch')
feedback_review  = Transition(label='Feedback Review')

# Silent transition for skips
skip = SilentTransition()

# Control-flow operators
# Optional community workshop
comm_xor = OperatorPOWL(operator=Operator.XOR, children=[community_meet, skip])
# Optional feedback at end
feedback_xor = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, skip])
# Loop for ongoing health monitoring
health_loop = OperatorPOWL(operator=Operator.LOOP, children=[health_monitor, skip])

# Build the partial-order workflow
root = StrictPartialOrder(nodes=[
    site_survey, 
    permit_request, 
    permit_approval,
    hive_assembly,
    equipment_check,
    iot_setup,
    local_sourcing,
    plant_selection,
    comm_xor,
    hive_placement,
    health_loop,
    seasonal_extract,
    honey_filter,
    packaging_prep,
    market_dispatch,
    feedback_xor
])

# Define control dependencies
root.order.add_edge(site_survey, permit_request)
root.order.add_edge(permit_request, permit_approval)

# After permit approval: two strands in parallel
root.order.add_edge(permit_approval, hive_assembly)
root.order.add_edge(permit_approval, local_sourcing)

# Hive assembly strand
root.order.add_edge(hive_assembly, equipment_check)
root.order.add_edge(equipment_check, iot_setup)
root.order.add_edge(iot_setup, hive_placement)

# Sourcing strand
root.order.add_edge(local_sourcing, plant_selection)
root.order.add_edge(plant_selection, comm_xor)
root.order.add_edge(comm_xor, hive_placement)

# Hive placement leads to monitoring loop
root.order.add_edge(hive_placement, health_loop)

# After monitoring, perform extraction and distribution
root.order.add_edge(health_loop, seasonal_extract)
root.order.add_edge(seasonal_extract, honey_filter)
root.order.add_edge(honey_filter, packaging_prep)
root.order.add_edge(packaging_prep, market_dispatch)

# Final optional feedback
root.order.add_edge(market_dispatch, feedback_xor)