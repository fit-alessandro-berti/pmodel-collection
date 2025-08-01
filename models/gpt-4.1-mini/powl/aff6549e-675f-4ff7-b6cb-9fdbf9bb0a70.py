# Generated from: aff6549e-675f-4ff7-b6cb-9fdbf9bb0a70.json
# Description: This process involves the multi-layered authentication of rare historical artifacts for museums and private collectors. It begins with initial provenance verification and scientific material analysis, followed by expert stylistic evaluation and forensic imaging. Subsequent steps include cross-referencing with global databases, consulting cultural heritage specialists, and conducting environmental aging simulations. The process further incorporates stakeholder interviews, legal ownership verification, and risk assessment for potential forgery. Final activities encompass preparation of detailed certification reports, digital archiving of findings, and secure artifact handover with traceability protocols to ensure authenticity and legal compliance throughout the artifact's lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

ProvenanceCheck = Transition(label='Provenance Check')
MaterialScan = Transition(label='Material Scan')
StylisticEval = Transition(label='Stylistic Eval')
ForensicImage = Transition(label='Forensic Image')
DatabaseMatch = Transition(label='Database Match')
HeritageConsult = Transition(label='Heritage Consult')
AgeSimulation = Transition(label='Age Simulation')
StakeholderTalk = Transition(label='Stakeholder Talk')
OwnershipVerify = Transition(label='Ownership Verify')
ForgeryRisk = Transition(label='Forgery Risk')
CertifyReport = Transition(label='Certify Report')
DataArchive = Transition(label='Data Archive')
SecureHandover = Transition(label='Secure Handover')
TraceProtocol = Transition(label='Trace Protocol')
LegalReview = Transition(label='Legal Review')

# First phase: initial provenance verification and scientific material analysis (both concurrent)
initial_PO = StrictPartialOrder(nodes=[ProvenanceCheck, MaterialScan])

# Second phase: expert stylistic evaluation and forensic imaging (concurrent)
eval_PO = StrictPartialOrder(nodes=[StylisticEval, ForensicImage])

# Third phase: cross-referencing with global databases, consulting heritage specialists, conducting aging simulations (concurrent)
cross_ref_PO = StrictPartialOrder(nodes=[DatabaseMatch, HeritageConsult, AgeSimulation])

# Fourth phase: stakeholder interviews, legal ownership verification, forgery risk assessment (concurrent)
risk_PO = StrictPartialOrder(nodes=[StakeholderTalk, OwnershipVerify, ForgeryRisk])

# Final phase - certification report, digital archiving, and secure handover with trace protocols (order: CertifyReport --> DataArchive --> SecureHandover concurrent with TraceProtocol)
final_PO = StrictPartialOrder(nodes=[CertifyReport, DataArchive, SecureHandover, TraceProtocol])

# Add order for final phase linear part: CertifyReport --> DataArchive --> SecureHandover
final_PO.order.add_edge(CertifyReport, DataArchive)
final_PO.order.add_edge(DataArchive, SecureHandover)

# SecureHandover and TraceProtocol can be concurrent so no order edge connecting TraceProtocol to others

# Legal Review is described as final, related to legal compliance and traceability, logically after risk phase and before final phase
# Assume LegalReview after risk_PO and before final_PO

# Combine all phases: initial_PO --> eval_PO --> cross_ref_PO --> risk_PO --> LegalReview --> final_PO

nodes = [initial_PO, eval_PO, cross_ref_PO, risk_PO, LegalReview, final_PO]
root = StrictPartialOrder(nodes=nodes)

# Add order edges to connect phases
root.order.add_edge(initial_PO, eval_PO)
root.order.add_edge(eval_PO, cross_ref_PO)
root.order.add_edge(cross_ref_PO, risk_PO)
root.order.add_edge(risk_PO, LegalReview)
root.order.add_edge(LegalReview, final_PO)