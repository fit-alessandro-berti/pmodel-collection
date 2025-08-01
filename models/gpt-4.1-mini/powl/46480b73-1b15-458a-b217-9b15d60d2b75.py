# Generated from: 46480b73-1b15-458a-b217-9b15d60d2b75.json
# Description: This process manages the unique supply chain for urban beekeeping operations, integrating local environmental assessments, hive placement approvals, and specialized equipment distribution to city locations. It involves coordination with municipal authorities for permits, sourcing sustainable bee-friendly plants, monitoring hive health via IoT devices, and coordinating seasonal honey extraction and packaging. The process ensures compliance with urban regulations while supporting biodiversity and community engagement through educational workshops and local market distribution, requiring adaptive logistics and stakeholder communication in a non-traditional agricultural setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
site_survey = Transition(label='Site Survey')
permit_request = Transition(label='Permit Request')
permit_approval = Transition(label='Permit Approval')

local_sourcing = Transition(label='Local Sourcing')
plant_selection = Transition(label='Plant Selection')

hive_assembly = Transition(label='Hive Assembly')
equipment_check = Transition(label='Equipment Check')

iot_setup = Transition(label='IoT Setup')
health_monitor = Transition(label='Health Monitor')

community_meet = Transition(label='Community Meet')

hive_placement = Transition(label='Hive Placement')

seasonal_extract = Transition(label='Seasonal Extract')
honey_filter = Transition(label='Honey Filter')
packaging_prep = Transition(label='Packaging Prep')

market_dispatch = Transition(label='Market Dispatch')

feedback_review = Transition(label='Feedback Review')

skip = SilentTransition()

# Permit sub-process: Permit Request --> Permit Approval
permit_seq = StrictPartialOrder(nodes=[permit_request, permit_approval])
permit_seq.order.add_edge(permit_request, permit_approval)

# Local sourcing partial order: Local Sourcing --> Plant Selection
sourcing = StrictPartialOrder(nodes=[local_sourcing, plant_selection])
sourcing.order.add_edge(local_sourcing, plant_selection)

# Hive preparation partial order: Hive Assembly --> Equipment Check
hive_prep = StrictPartialOrder(nodes=[hive_assembly, equipment_check])
hive_prep.order.add_edge(hive_assembly, equipment_check)

# Monitoring loop: Loop of Health Monitor and IoT Setup
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[health_monitor, iot_setup])

# Seasonal preparation sequence: Seasonal Extract --> Honey Filter --> Packaging Prep
seasonal_prep = StrictPartialOrder(nodes=[seasonal_extract, honey_filter, packaging_prep])
seasonal_prep.order.add_edge(seasonal_extract, honey_filter)
seasonal_prep.order.add_edge(honey_filter, packaging_prep)

# Market & feedback concurrency
market_and_feedback = StrictPartialOrder(nodes=[market_dispatch, feedback_review])

# Community meeting runs concurrently with monitoring and hive placement
# Put Community Meet and Hive Placement concurrent
community_and_hive_placement = StrictPartialOrder(nodes=[community_meet, hive_placement])

# Assemble main preparation partial order:
# Site Survey --> Permit Process
# Site Survey --> Local Sourcing
# Site Survey --> Hive Preparation
# Site Survey --> Community Meet & Hive Placement
# Permit Approval --> Hive Placement
# Local Sourcing precedes Plant Selection (already inside sourcing)
# Hive Preparation precedes IoT Setup and Health Monitor loop
# Hive Placement and Community Meet are concurrent
# After hive placement and monitoring loop, Seasonal preparation and market & feedback concurrently

main_partial_order = StrictPartialOrder(
    nodes=[
        site_survey,
        permit_seq,  # Permit Request -> Permit Approval
        sourcing,    # Local Sourcing -> Plant Selection
        hive_prep,   # Hive Assembly -> Equipment Check
        community_and_hive_placement, 
        monitor_loop, 
        seasonal_prep,
        market_and_feedback
    ]
)

# Add ordering edges per the description

# Site Survey precedes (permit request, local sourcing, hive assembly, community meet and hive placement)
main_partial_order.order.add_edge(site_survey, permit_seq)
main_partial_order.order.add_edge(site_survey, sourcing)
main_partial_order.order.add_edge(site_survey, hive_prep)
main_partial_order.order.add_edge(site_survey, community_and_hive_placement)

# Permit Approval precedes Hive Placement
main_partial_order.order.add_edge(permit_seq, community_and_hive_placement)

# Hive Preparation precedes monitoring loop
main_partial_order.order.add_edge(hive_prep, monitor_loop)

# Hive Placement and Community Meet are concurrent inside community_and_hive_placement

# After Hive Placement and Monitoring loop, seasonal prep and market&feedback run concurrently:
main_partial_order.order.add_edge(community_and_hive_placement, seasonal_prep)
main_partial_order.order.add_edge(monitor_loop, seasonal_prep)

main_partial_order.order.add_edge(community_and_hive_placement, market_and_feedback)
main_partial_order.order.add_edge(monitor_loop, market_and_feedback)

root = main_partial_order