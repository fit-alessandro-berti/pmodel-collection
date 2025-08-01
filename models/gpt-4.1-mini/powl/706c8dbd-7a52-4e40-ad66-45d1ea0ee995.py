# Generated from: 706c8dbd-7a52-4e40-ad66-45d1ea0ee995.json
# Description: This process involves the intricate steps required to authenticate historical artifacts for museum acquisition or private collection. It begins with preliminary visual inspection followed by material composition analysis using non-invasive techniques. Provenance research is conducted through archival record comparison and expert interviews. Scientific dating methods such as radiocarbon or thermoluminescence are applied to determine age. Microbial and residue analysis identify environmental exposure and usage patterns. A risk assessment for forgery indicators is completed, including stylistic evaluation by art historians. Legal clearance ensures compliance with cultural heritage laws. Finally, a comprehensive authenticity report is compiled and peer-reviewed before final approval and acquisition decision.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities as Transitions
VisualCheck = Transition(label='Visual Check')
MaterialScan = Transition(label='Material Scan')

ArchivalSearch = Transition(label='Archival Search')
ExpertInterview = Transition(label='Expert Interview')

RadiocarbonTest = Transition(label='Radiocarbon Test')
Thermoluminescence = Transition(label='Thermoluminescence')

ResidueAnalysis = Transition(label='Residue Analysis')
MicrobialTest = Transition(label='Microbial Test')

StyleReview = Transition(label='Style Review')
ForgeryRisk = Transition(label='Forgery Risk')

LegalReview = Transition(label='Legal Review')
ComplianceCheck = Transition(label='Compliance Check')

ReportDraft = Transition(label='Report Draft')
PeerReview = Transition(label='Peer Review')

FinalApproval = Transition(label='Final Approval')

# Construct provenance research partial order: Archival Search and Expert Interview concurrent
provenance_research = StrictPartialOrder(nodes=[ArchivalSearch, ExpertInterview])
# No order edges between ArchivalSearch and ExpertInterview so concurrent

# Construct scientific dating choice: either Radiocarbon Test or Thermoluminescence
scientific_dating = OperatorPOWL(operator=Operator.XOR, children=[RadiocarbonTest, Thermoluminescence])

# Construct microbial and residue tests concurrent
microbial_residue = StrictPartialOrder(nodes=[ResidueAnalysis, MicrobialTest])
# no edges, concurrent

# Construct forgery risk partial order: Style Review --> Forgery Risk
forgery_risk = StrictPartialOrder(nodes=[StyleReview, ForgeryRisk])
forgery_risk.order.add_edge(StyleReview, ForgeryRisk)

# Construct legal clearance partial order: Legal Review --> Compliance Check
legal_clearance = StrictPartialOrder(nodes=[LegalReview, ComplianceCheck])
legal_clearance.order.add_edge(LegalReview, ComplianceCheck)

# Construct report and review partial order: Report Draft --> Peer Review
report_review = StrictPartialOrder(nodes=[ReportDraft, PeerReview])
report_review.order.add_edge(ReportDraft, PeerReview)

# Compose the process partial order step by step following the description order with edges:

# Step 1 and 2 sequential: Visual Check --> Material Scan
step1_2 = StrictPartialOrder(nodes=[VisualCheck, MaterialScan])
step1_2.order.add_edge(VisualCheck, MaterialScan)

# Step 3 provenance research after material scan
step1_3 = StrictPartialOrder(nodes=[step1_2, provenance_research])
step1_3.order.add_edge(step1_2, provenance_research)

# Step 4 scientific dating after provenance research
step1_4 = StrictPartialOrder(nodes=[step1_3, scientific_dating])
step1_4.order.add_edge(step1_3, scientific_dating)

# Step 5 microbial & residue analysis after scientific dating
step1_5 = StrictPartialOrder(nodes=[step1_4, microbial_residue])
step1_5.order.add_edge(step1_4, microbial_residue)

# Step 6 forgery risk after microbial & residue
step1_6 = StrictPartialOrder(nodes=[step1_5, forgery_risk])
step1_6.order.add_edge(step1_5, forgery_risk)

# Step 7 legal clearance after forgery risk
step1_7 = StrictPartialOrder(nodes=[step1_6, legal_clearance])
step1_7.order.add_edge(step1_6, legal_clearance)

# Step 8 report draft and peer review after legal clearance
step1_8 = StrictPartialOrder(nodes=[step1_7, report_review])
step1_8.order.add_edge(step1_7, report_review)

# Step 9 final approval after peer review (i.e. after report_review)
root = StrictPartialOrder(nodes=[step1_8, FinalApproval])
root.order.add_edge(step1_8, FinalApproval)