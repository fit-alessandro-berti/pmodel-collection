# Generated from: 344c55ff-4700-4717-89e0-52da65c819f7.json
# Description: This process involves the systematic verification and authentication of rare historical artifacts for museum acquisition or private collection. It includes provenance research, material analysis, expert consultation, and legal clearance. Multiple specialists collaborate to ensure authenticity, condition assessment, and ethical compliance before final approval and documentation, integrating interdisciplinary methods and advanced technology to mitigate forgery risks and protect cultural heritage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all transitions
initialReview     = Transition(label='Initial Review')
provenanceCheck   = Transition(label='Provenance Check')
materialScan      = Transition(label='Material Scan')
carbonDating      = Transition(label='Carbon Dating')
expertConsult     = Transition(label='Expert Consult')
conditionReport   = Transition(label='Condition Report')
forgeryTest       = Transition(label='Forgery Test')
appraisalEstimate = Transition(label='Appraisal Estimate')
ethicsAudit       = Transition(label='Ethics Audit')
legalReview       = Transition(label='Legal Review')
ownershipVerify   = Transition(label='Ownership Verify')
riskAssessment    = Transition(label='Risk Assessment')
finalApproval     = Transition(label='Final Approval')
documentation     = Transition(label='Documentation')
archiveEntry      = Transition(label='Archive Entry')
clientBrief       = Transition(label='Client Brief')

# Material analysis is a small partial order: Material Scan -> Carbon Dating
matAnalysis = StrictPartialOrder(nodes=[materialScan, carbonDating])
matAnalysis.order.add_edge(materialScan, carbonDating)

# Initial parallel tasks: after Initial Review do Provenance Check and Material Analysis in parallel
p1 = StrictPartialOrder(nodes=[initialReview, provenanceCheck, matAnalysis])
p1.order.add_edge(initialReview, provenanceCheck)
p1.order.add_edge(initialReview, matAnalysis)

# Expert consultation after the initial tasks
p2 = StrictPartialOrder(nodes=[p1, expertConsult])
p2.order.add_edge(p1, expertConsult)

# Concurrent assessments after Expert Consult
p3 = StrictPartialOrder(
    nodes=[p2, conditionReport, forgeryTest, appraisalEstimate]
)
p3.order.add_edge(p2, conditionReport)
p3.order.add_edge(p2, forgeryTest)
p3.order.add_edge(p2, appraisalEstimate)

# Compliance & clearance tasks in parallel after the assessments
p4 = StrictPartialOrder(
    nodes=[p3, ethicsAudit, legalReview, ownershipVerify, riskAssessment]
)
p4.order.add_edge(p3, ethicsAudit)
p4.order.add_edge(p3, legalReview)
p4.order.add_edge(p3, ownershipVerify)
p4.order.add_edge(p3, riskAssessment)

# Final approval after all checks
p5 = StrictPartialOrder(nodes=[p4, finalApproval])
p5.order.add_edge(p4, finalApproval)

# Post‐approval deliverables in parallel
root = StrictPartialOrder(
    nodes=[p5, documentation, archiveEntry, clientBrief]
)
root.order.add_edge(p5, documentation)
root.order.add_edge(p5, archiveEntry)
root.order.add_edge(p5, clientBrief)