# Generated from: f1f85d4b-aebb-4ec4-a34b-b20ca6b8c502.json
# Description: This process involves the comprehensive authentication of historical artifacts before acquisition by a museum. It includes provenance verification, material analysis, expert consultation, digital archiving, and legal compliance checks. The workflow ensures that each artifact is authentic, legally obtainable, and properly documented for future research and exhibition. It integrates multidisciplinary expertise and advanced technology, enabling the museum to maintain collection integrity and public trust. The process also involves negotiation with sellers, risk assessment related to artifact condition and origin, and final approval by the acquisition committee.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Initial_Review = Transition(label='Initial Review')
Provenance_Check = Transition(label='Provenance Check')
Material_Testing = Transition(label='Material Testing')
Expert_Survey = Transition(label='Expert Survey')
Digital_Scan = Transition(label='Digital Scan')
Condition_Report = Transition(label='Condition Report')
Legal_Review = Transition(label='Legal Review')
Risk_Analysis = Transition(label='Risk Analysis')
Seller_Negotiation = Transition(label='Seller Negotiation')
Documentation = Transition(label='Documentation')
Archival_Entry = Transition(label='Archival Entry')
Committee_Review = Transition(label='Committee Review')
Final_Approval = Transition(label='Final Approval')
Acquisition_Setup = Transition(label='Acquisition Setup')
Exhibit_Planning = Transition(label='Exhibit Planning')

# Construct provenance verification partial order 
# Provenance Check, Material Testing, Expert Survey run in parallel after Initial Review,
# then all synchronize and move to Digital Scan
provenance_pos = StrictPartialOrder(
    nodes=[Initial_Review, Provenance_Check, Material_Testing, Expert_Survey, Digital_Scan]
)
provenance_pos.order.add_edge(Initial_Review, Provenance_Check)
provenance_pos.order.add_edge(Initial_Review, Material_Testing)
provenance_pos.order.add_edge(Initial_Review, Expert_Survey)
provenance_pos.order.add_edge(Provenance_Check, Digital_Scan)
provenance_pos.order.add_edge(Material_Testing, Digital_Scan)
provenance_pos.order.add_edge(Expert_Survey, Digital_Scan)

# Condition Report, Legal Review, Risk Analysis run concurrently after Digital Scan
# Then all must complete before Seller Negotiation
mid_pos = StrictPartialOrder(
    nodes=[Digital_Scan, Condition_Report, Legal_Review, Risk_Analysis, Seller_Negotiation]
)
mid_pos.order.add_edge(Digital_Scan, Condition_Report)
mid_pos.order.add_edge(Digital_Scan, Legal_Review)
mid_pos.order.add_edge(Digital_Scan, Risk_Analysis)
mid_pos.order.add_edge(Condition_Report, Seller_Negotiation)
mid_pos.order.add_edge(Legal_Review, Seller_Negotiation)
mid_pos.order.add_edge(Risk_Analysis, Seller_Negotiation)

# After Seller Negotiation, Documentation and Archival Entry run in parallel
post_negotiation_pos = StrictPartialOrder(
    nodes=[Seller_Negotiation, Documentation, Archival_Entry]
)
post_negotiation_pos.order.add_edge(Seller_Negotiation, Documentation)
post_negotiation_pos.order.add_edge(Seller_Negotiation, Archival_Entry)

# Committee Review follows Documentation and Archival Entry
committee_pos = StrictPartialOrder(
    nodes=[Documentation, Archival_Entry, Committee_Review]
)
committee_pos.order.add_edge(Documentation, Committee_Review)
committee_pos.order.add_edge(Archival_Entry, Committee_Review)

# Final Approval follows Committee Review
final_approval_pos = StrictPartialOrder(
    nodes=[Committee_Review, Final_Approval]
)
final_approval_pos.order.add_edge(Committee_Review, Final_Approval)

# Acquisition Setup and Exhibit Planning run concurrently after Final Approval
final_pos = StrictPartialOrder(
    nodes=[Final_Approval, Acquisition_Setup, Exhibit_Planning]
)
final_pos.order.add_edge(Final_Approval, Acquisition_Setup)
final_pos.order.add_edge(Final_Approval, Exhibit_Planning)

# Combine all parts in sequence, linking the end of each part to the start of the next
root = StrictPartialOrder(
    nodes=[provenance_pos, mid_pos, post_negotiation_pos, committee_pos, final_approval_pos, final_pos]
)
root.order.add_edge(provenance_pos, mid_pos)
root.order.add_edge(mid_pos, post_negotiation_pos)
root.order.add_edge(post_negotiation_pos, committee_pos)
root.order.add_edge(committee_pos, final_approval_pos)
root.order.add_edge(final_approval_pos, final_pos)