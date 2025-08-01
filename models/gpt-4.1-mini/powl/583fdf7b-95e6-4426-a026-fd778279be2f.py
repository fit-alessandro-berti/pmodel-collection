# Generated from: 583fdf7b-95e6-4426-a026-fd778279be2f.json
# Description: This process involves the systematic examination and validation of historical artifacts to determine authenticity and provenance. It includes detailed multi-disciplinary analyses such as material composition testing, stylistic comparison, and provenance verification through archival research. The workflow also requires coordination with external experts, legal compliance checks, and secure documentation. Final steps involve digital cataloging and controlled storage recommendations, ensuring artifacts are preserved and their history accurately recorded to support museum acquisitions or private collections. The entire process demands meticulous attention to detail and cross-functional collaboration to mitigate risks of forgery and ensure cultural heritage integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
InitialReview = Transition(label='Initial Review')
MaterialScan = Transition(label='Material Scan')
StylisticMatch = Transition(label='Stylistic Match')
ProvenanceCheck = Transition(label='Provenance Check')
ExpertConsult = Transition(label='Expert Consult')
LegalVerify = Transition(label='Legal Verify')
ArchivalSearch = Transition(label='Archival Search')
RadiocarbonTest = Transition(label='Radiocarbon Test')
XRayAnalysis = Transition(label='XRay Analysis')
Documentation = Transition(label='Documentation')
DigitalCatalog = Transition(label='Digital Catalog')
ConditionReport = Transition(label='Condition Report')
StoragePlan = Transition(label='Storage Plan')
FinalApproval = Transition(label='Final Approval')
ClientBrief = Transition(label='Client Brief')

# The process:
# 1) Initial Review
# 2) Parallel detailed analyses consisting of:
#    - MaterialScan
#    - StylisticMatch
#    - ProvenanceCheck, which itself depends on 
#       ArchivalSearch, RadiocarbonTest, XRayAnalysis
# 3) ExpertConsult and LegalVerify (in parallel, after analyses)
# 4) Documentation
# 5) DigitalCatalog and ConditionReport (parallel after Documentation)
# 6) StoragePlan
# 7) FinalApproval
# 8) ClientBrief

# Model critical analysis partial order: ArchivalSearch, RadiocarbonTest, XRayAnalysis are parallel
archivalSearch = ArchivalSearch
radiocarbonTest = RadiocarbonTest
xrayAnalysis = XRayAnalysis

# ProvenanceCheck depends on these three (all completed first)
provenanceCheckPO = StrictPartialOrder(
    nodes=[ArchivalSearch, RadiocarbonTest, XRayAnalysis, ProvenanceCheck])
provenanceCheckPO.order.add_edge(ArchivalSearch, ProvenanceCheck)
provenanceCheckPO.order.add_edge(RadiocarbonTest, ProvenanceCheck)
provenanceCheckPO.order.add_edge(XRayAnalysis, ProvenanceCheck)

# Detailed analyses partial order: MaterialScan, StylisticMatch, ProvenanceCheckPO.parallel
detailedAnalyses = StrictPartialOrder(
    nodes=[MaterialScan, StylisticMatch, provenanceCheckPO])
# no order edges - all three concurrent after ProvenanceCheckPO considered a node

# Actually provenanceCheckPO must complete before detailedAnalyses considered complete,
# but detailedAnalyses contains provenanceCheckPO as a node, so they are concurrent.
# We want MaterialScan and StylisticMatch concurrent with ProvenanceCheckPO.

# After detailedAnalyses comes ExpertConsult and LegalVerify in parallel
expertLegal = StrictPartialOrder(nodes=[ExpertConsult, LegalVerify])  # parallel

# After expertLegal, Documentation
# Following Documentation, DigitalCatalog and ConditionReport in parallel
digitalCondition = StrictPartialOrder(nodes=[DigitalCatalog, ConditionReport])  # parallel

# Then StoragePlan, then FinalApproval, then ClientBrief sequentially
# We thus create a PO connecting them sequentially

# Build the main partial order
root = StrictPartialOrder(
    nodes=[InitialReview, detailedAnalyses, expertLegal, Documentation,
           digitalCondition, StoragePlan, FinalApproval, ClientBrief])

# Edges for the main sequence of process steps:
root.order.add_edge(InitialReview, detailedAnalyses)
root.order.add_edge(detailedAnalyses, expertLegal)
root.order.add_edge(expertLegal, Documentation)
root.order.add_edge(Documentation, digitalCondition)
root.order.add_edge(digitalCondition, StoragePlan)
root.order.add_edge(StoragePlan, FinalApproval)
root.order.add_edge(FinalApproval, ClientBrief)