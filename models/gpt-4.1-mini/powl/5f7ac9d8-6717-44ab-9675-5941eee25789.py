# Generated from: 5f7ac9d8-6717-44ab-9675-5941eee25789.json
# Description: This complex process involves verifying the authenticity of rare historical artifacts through a multi-disciplinary approach. It includes initial provenance research, material composition analysis using spectroscopy, expert visual examination, cross-referencing with global databases, and legal ownership validation. The process also incorporates risk assessment for potential forgeries, condition reporting, digital archiving of findings, and final certification issuance. Communication with stakeholders is maintained throughout to ensure transparency and compliance with international trade regulations, culminating in secure storage or exhibition preparation depending on the artifact's status.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Provenance_Check = Transition(label='Provenance Check')
Material_Scan = Transition(label='Material Scan')
Visual_Audit = Transition(label='Visual Audit')
Database_Match = Transition(label='Database Match')
Ownership_Verify = Transition(label='Ownership Verify')
Forgery_Risk = Transition(label='Forgery Risk')
Condition_Report = Transition(label='Condition Report')
Stakeholder_Sync = Transition(label='Stakeholder Sync')
Legal_Review = Transition(label='Legal Review')
Digital_Archive = Transition(label='Digital Archive')
Expert_Consultation = Transition(label='Expert Consultation')
Certification_Issue = Transition(label='Certification Issue')
Storage_Prep = Transition(label='Storage Prep')
Exhibit_Plan = Transition(label='Exhibit Plan')
Compliance_Audit = Transition(label='Compliance Audit')

# Expert review includes Legal Review, Expert Consultation, Compliance Audit in partial order (concurrent)
expert_review = StrictPartialOrder(nodes=[Legal_Review, Expert_Consultation, Compliance_Audit])
# no order edges, all concurrent

# Verification phase partial order: Material Scan --> Visual Audit --> Database Match --> Ownership Verify --> expert_review
verification = StrictPartialOrder(
    nodes=[Material_Scan, Visual_Audit, Database_Match, Ownership_Verify, expert_review]
)
verification.order.add_edge(Material_Scan, Visual_Audit)
verification.order.add_edge(Visual_Audit, Database_Match)
verification.order.add_edge(Database_Match, Ownership_Verify)
verification.order.add_edge(Ownership_Verify, expert_review)

# Initial phase partial order: Provenance Check --> verification
initial_phase = StrictPartialOrder(nodes=[Provenance_Check, verification])
initial_phase.order.add_edge(Provenance_Check, verification)

# Risk assessment and condition reporting can proceed concurrently after verification
risk_and_condition = StrictPartialOrder(nodes=[Forgery_Risk, Condition_Report])
# no order edges (concurrent)

# Archive after risk and condition report finishes
archive_phase = StrictPartialOrder(nodes=[Digital_Archive])
# will be ordered after risk_and_condition but we add order edge at higher level

# Stakeholder Sync can happen concurrently anytime from verification end to final certification
# To include Stakeholder Sync overlapping with latter phases, place it in parallel at root

# Certification phase: Expert Review (reuse expert_review), Certification Issue
certification_phase = StrictPartialOrder(nodes=[Certification_Issue])
# will add order edge expert_review-->Certification_Issue at higher or combined level

# After Certification Issue, choice between Storage Prep or Exhibit Plan
storage_or_exhibit = OperatorPOWL(operator=Operator.XOR, children=[Storage_Prep, Exhibit_Plan])

# Build full certification segment including expert_review and cert plus choice
certification_block = StrictPartialOrder(nodes=[expert_review, Certification_Issue, storage_or_exhibit])
certification_block.order.add_edge(expert_review, Certification_Issue)
certification_block.order.add_edge(Certification_Issue, storage_or_exhibit)

# Build post-verification phase combining risk, condition report, archive
post_verification = StrictPartialOrder(nodes=[risk_and_condition, archive_phase])
post_verification.order.add_edge(risk_and_condition, archive_phase)

# Combine all after verification: post_verification and certification_block can run sequentially (risk+cond -> archive -> certification)
# but Stakeholder Sync runs concurrently with these
# So Stakeholder Sync stays parallel at top level

post_verification_and_cert = StrictPartialOrder(nodes=[post_verification, certification_block])
post_verification_and_cert.order.add_edge(post_verification, certification_block)

# The partial order combining verification and the following steps
verification_and_followup = StrictPartialOrder(nodes=[verification, post_verification_and_cert])
verification_and_followup.order.add_edge(verification, post_verification_and_cert)

# Finally, the root partial order: Provenance_Check --> verification_and_followup
root = StrictPartialOrder(nodes=[Provenance_Check, verification_and_followup, Stakeholder_Sync])
root.order.add_edge(Provenance_Check, verification_and_followup)
# Stakeholder_Sync concurrent with verification_and_followup and Provenance_Check

# The root contains all activities embedded within above partial orders