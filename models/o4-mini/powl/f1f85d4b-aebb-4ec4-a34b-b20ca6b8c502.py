# Generated from: f1f85d4b-aebb-4ec4-a34b-b20ca6b8c502.json
# Description: This process involves the comprehensive authentication of historical artifacts before acquisition by a museum. It includes provenance verification, material analysis, expert consultation, digital archiving, and legal compliance checks. The workflow ensures that each artifact is authentic, legally obtainable, and properly documented for future research and exhibition. It integrates multidisciplinary expertise and advanced technology, enabling the museum to maintain collection integrity and public trust. The process also involves negotiation with sellers, risk assessment related to artifact condition and origin, and final approval by the acquisition committee.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
initial_review    = Transition(label='Initial Review')
provenance_check  = Transition(label='Provenance Check')
material_testing  = Transition(label='Material Testing')
expert_survey     = Transition(label='Expert Survey')
digital_scan      = Transition(label='Digital Scan')
condition_report  = Transition(label='Condition Report')
legal_review      = Transition(label='Legal Review')
seller_negotiation= Transition(label='Seller Negotiation')
risk_analysis     = Transition(label='Risk Analysis')
documentation     = Transition(label='Documentation')
archival_entry    = Transition(label='Archival Entry')
committee_review  = Transition(label='Committee Review')
final_approval    = Transition(label='Final Approval')
acquisition_setup = Transition(label='Acquisition Setup')
exhibit_planning  = Transition(label='Exhibit Planning')

# Loop for negotiation and risk assessment
negotiation_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[seller_negotiation, risk_analysis]
)

# Build the partial order
root = StrictPartialOrder(
    nodes=[
        initial_review,
        provenance_check,
        material_testing,
        expert_survey,
        digital_scan,
        condition_report,
        legal_review,
        negotiation_loop,
        documentation,
        archival_entry,
        committee_review,
        final_approval,
        acquisition_setup,
        exhibit_planning
    ]
)

# Control‐flow dependencies
# 1) Initial Review, then three parallel analyses
root.order.add_edge(initial_review, provenance_check)
root.order.add_edge(initial_review, material_testing)
root.order.add_edge(initial_review, expert_survey)

# 2) Expert Survey → Digital Scan → Condition Report
root.order.add_edge(expert_survey, digital_scan)
root.order.add_edge(digital_scan, condition_report)

# 3) Provenance Check → Legal Review
root.order.add_edge(provenance_check, legal_review)

# 4) Once both legal_review and condition_report are done, start the negotiation loop
root.order.add_edge(legal_review, negotiation_loop)
root.order.add_edge(condition_report, negotiation_loop)

# 5) After negotiation loop finishes → Documentation and Archival Entry in parallel
root.order.add_edge(negotiation_loop, documentation)
root.order.add_edge(negotiation_loop, archival_entry)

# 6) Documentation & Archival Entry → Committee Review → Final Approval
root.order.add_edge(documentation, committee_review)
root.order.add_edge(archival_entry, committee_review)
root.order.add_edge(committee_review, final_approval)

# 7) After final approval → Acquisition Setup and Exhibit Planning in parallel
root.order.add_edge(final_approval, acquisition_setup)
root.order.add_edge(final_approval, exhibit_planning)