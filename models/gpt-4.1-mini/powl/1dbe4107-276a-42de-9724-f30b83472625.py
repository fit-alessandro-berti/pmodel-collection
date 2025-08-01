# Generated from: 1dbe4107-276a-42de-9724-f30b83472625.json
# Description: This process involves a multi-stage verification and validation of rare artifacts submitted by private collectors for authentication and provenance certification. Starting with initial documentation review, the artifact undergoes physical inspection, material analysis, and stylistic comparison with known exemplars. Parallel background checks on ownership history and cross-referencing with global databases are performed to detect forgeries or illegal acquisitions. Expert panels are convened for consensus opinions, followed by risk assessment for market impact. Finally, a digital certificate is issued, embedding blockchain-based authenticity records. This atypical process ensures trust and legal compliance in high-value artifact trading.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Doc_Review = Transition(label='Doc Review')
Artifact_Scan = Transition(label='Artifact Scan')
Material_Test = Transition(label='Material Test')
Style_Match = Transition(label='Style Match')
Owner_Check = Transition(label='Owner Check')
Database_Cross = Transition(label='Database Cross')
Forgery_Detect = Transition(label='Forgery Detect')
Legal_Verify = Transition(label='Legal Verify')
Expert_Panel = Transition(label='Expert Panel')
Consensus_Vote = Transition(label='Consensus Vote')
Risk_Assess = Transition(label='Risk Assess')
Market_Impact = Transition(label='Market Impact')
Cert_Generate = Transition(label='Cert Generate')
Blockchain_Link = Transition(label='Blockchain Link')
Client_Notify = Transition(label='Client Notify')
Archive_Store = Transition(label='Archive Store')

# Physical inspection sequence: Artifact Scan -> Material Test -> Style Match
physical_inspection = StrictPartialOrder(
    nodes=[Artifact_Scan, Material_Test, Style_Match]
)
physical_inspection.order.add_edge(Artifact_Scan, Material_Test)
physical_inspection.order.add_edge(Material_Test, Style_Match)

# Background checks partial order:
# Owner Check and Database Cross in parallel, both lead to Forgery Detect then Legal Verify
background_checks = StrictPartialOrder(
    nodes=[Owner_Check, Database_Cross, Forgery_Detect, Legal_Verify]
)
background_checks.order.add_edge(Owner_Check, Forgery_Detect)
background_checks.order.add_edge(Database_Cross, Forgery_Detect)
background_checks.order.add_edge(Forgery_Detect, Legal_Verify)

# Expert panel followed by consensus vote sequentially
expert_consensus = StrictPartialOrder(
    nodes=[Expert_Panel, Consensus_Vote]
)
expert_consensus.order.add_edge(Expert_Panel, Consensus_Vote)

# Risk assessment sequence: Risk Assess -> Market Impact
risk_assessment = StrictPartialOrder(
    nodes=[Risk_Assess, Market_Impact]
)
risk_assessment.order.add_edge(Risk_Assess, Market_Impact)

# Final certificate generation and blockchain linking in parallel
certification = StrictPartialOrder(
    nodes=[Cert_Generate, Blockchain_Link]
)

# Notification and archival in parallel after all above completed
final_steps = StrictPartialOrder(
    nodes=[Client_Notify, Archive_Store]
)

# Create the main workflow partial order
# Nodes:
# Doc Review --> physical_inspection
# Doc Review --> background_checks
# After physical_inspection and background_checks finish, continue to:
# expert_consensus
# after expert_consensus, risk_assessment
# after risk_assessment, certification
# after certification, final_steps

root = StrictPartialOrder(
    nodes=[
        Doc_Review,
        physical_inspection,
        background_checks,
        expert_consensus,
        risk_assessment,
        certification,
        final_steps
    ]
)

# Define edges

# Doc Review --> physical_inspection, background_checks concurrently start after Doc Review
root.order.add_edge(Doc_Review, physical_inspection)
root.order.add_edge(Doc_Review, background_checks)

# physical_inspection and background_checks must complete before expert_consensus
root.order.add_edge(physical_inspection, expert_consensus)
root.order.add_edge(background_checks, expert_consensus)

# expert_consensus --> risk_assessment
root.order.add_edge(expert_consensus, risk_assessment)

# risk_assessment --> certification
root.order.add_edge(risk_assessment, certification)

# certification --> final_steps
root.order.add_edge(certification, final_steps)