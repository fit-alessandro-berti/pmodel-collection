# Generated from: 4cfad4ae-b22b-44ff-8612-a97da54e7574.json
# Description: This process outlines the end-to-end supply chain of urban beekeeping equipment and honey distribution. It begins with sourcing sustainable materials from local artisans, followed by custom manufacturing of eco-friendly hives. The process includes hive assembly, quality inspections, and seasonal bee colony integration. Parallel activities involve urban apiary site selection, environmental impact assessments, and regulatory compliance verification. Once hives are deployed, ongoing monitoring of bee health and hive conditions is conducted using IoT sensors. Honey extraction, purification, and packaging occur in small batches to maintain artisanal quality. The process concludes with direct-to-consumer marketing, urban farmer collaborations, and feedback loops for continuous product and process improvement, emphasizing sustainability and community engagement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Material_Sourcing = Transition(label='Material Sourcing')
Custom_Fabrication = Transition(label='Custom Fabrication')
Hive_Assembly = Transition(label='Hive Assembly')
Quality_Check = Transition(label='Quality Check')
Colony_Integration = Transition(label='Colony Integration')

Site_Selection = Transition(label='Site Selection')
Impact_Assess = Transition(label='Impact Assess')
Compliance_Review = Transition(label='Compliance Review')

Sensor_Setup = Transition(label='Sensor Setup')
Health_Monitoring = Transition(label='Health Monitoring')

Honey_Extract = Transition(label='Honey Extract')
Purify_Batch = Transition(label='Purify Batch')
Package_Goods = Transition(label='Package Goods')

Direct_Marketing = Transition(label='Direct Marketing')
Farmer_Partner = Transition(label='Farmer Partner')
Feedback_Loop = Transition(label='Feedback Loop')

# Partial order for the initial linear supply chain steps before parallel activities:
supply_chain_seq = StrictPartialOrder(
    nodes=[Material_Sourcing, Custom_Fabrication, Hive_Assembly, Quality_Check, Colony_Integration]
)
supply_chain_seq.order.add_edge(Material_Sourcing, Custom_Fabrication)
supply_chain_seq.order.add_edge(Custom_Fabrication, Hive_Assembly)
supply_chain_seq.order.add_edge(Hive_Assembly, Quality_Check)
supply_chain_seq.order.add_edge(Quality_Check, Colony_Integration)

# Parallel activities: Site Selection, Impact Assess, Compliance Review (concurrent)
parallel_activities = StrictPartialOrder(
    nodes=[Site_Selection, Impact_Assess, Compliance_Review],
    # no order edges - all concurrent
)

# After hive deployment (assumed after Colony Integration and parallel activities), setup sensors and monitor hive:
monitoring_seq = StrictPartialOrder(
    nodes=[Sensor_Setup, Health_Monitoring]
)
monitoring_seq.order.add_edge(Sensor_Setup, Health_Monitoring)

# Honey processing sequence:
honey_processing = StrictPartialOrder(
    nodes=[Honey_Extract, Purify_Batch, Package_Goods]
)
honey_processing.order.add_edge(Honey_Extract, Purify_Batch)
honey_processing.order.add_edge(Purify_Batch, Package_Goods)

# Marketing and feedback parallel activities:
marketing_feedback = StrictPartialOrder(
    nodes=[Direct_Marketing, Farmer_Partner, Feedback_Loop],
    # all concurrent, no order edges
)

# Combine the end sequences (monitoring, honey processing, marketing/feedback) in parallel
end_parallel = StrictPartialOrder(
    nodes=[monitoring_seq, honey_processing, marketing_feedback]
    # no order edges - all concurrent
)

# Combine the early supply chain and the parallel activities (site selection etc.) in partial order:
early_part = StrictPartialOrder(
    nodes=[supply_chain_seq, parallel_activities]
)
early_part.order.add_edge(supply_chain_seq, parallel_activities)

# Combine early part and end parallel activities in partial order:
root = StrictPartialOrder(
    nodes=[early_part, end_parallel]
)
root.order.add_edge(early_part, end_parallel)