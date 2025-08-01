# Generated from: 1903c760-a8d4-4847-b920-e6d340dcca85.json
# Description: This process involves the comprehensive authentication of antiques for high-end auction houses. It starts with initial artifact intake and condition review, followed by provenance verification through archival research and expert interviews. Scientific testing includes material composition analysis and radiocarbon dating to validate age. Parallelly, stylistic comparison against known period examples is performed by art historians. Legal clearance ensures no illicit trade history. Finally, a detailed report is generated combining all findings to inform auction valuation and marketing strategies. This workflow mitigates fraud and enhances buyer confidence in rare artifact transactions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ArtifactIntake = Transition(label='Artifact Intake')
ConditionCheck = Transition(label='Condition Check')

ProvenanceResearch = Transition(label='Provenance Research')
ExpertInterview = Transition(label='Expert Interview')

MaterialTesting = Transition(label='Material Testing')
RadiocarbonDate = Transition(label='Radiocarbon Date')

StylisticCompare = Transition(label='Stylistic Compare')
ForgeryAnalysis = Transition(label='Forgery Analysis')

LegalClearance = Transition(label='Legal Clearance')

HistoricalContext = Transition(label='Historical Context')
DocumentationReview = Transition(label='Documentation Review')

ReportDrafting = Transition(label='Report Drafting')
ValuationMeeting = Transition(label='Valuation Meeting')
MarketingPrep = Transition(label='Marketing Prep')

FinalApproval = Transition(label='Final Approval')

# Provenance verification: choice of Provenance Research OR Expert Interview
ProvenanceChoice = OperatorPOWL(operator=Operator.XOR, children=[ProvenanceResearch, ExpertInterview])

# Scientific testing (Material Testing and Radiocarbon Date in parallel)
ScientificTesting = StrictPartialOrder(nodes=[MaterialTesting, RadiocarbonDate])  # no order => parallel

# Stylistic comparison and Forgery Analysis in parallel
Stylistic = StrictPartialOrder(nodes=[StylisticCompare, ForgeryAnalysis])  # no order => parallel

# Combine all provenance, scientific testing, and stylistic branches in parallel
# We put ProvenanceChoice as a single node,
# ScientificTesting and Stylistic as StrictPartialOrder nodes.

# As POWL nodes must be inside StrictPartialOrder, we build a single PO for parallel:
ParallelBranches = StrictPartialOrder(
    nodes=[ProvenanceChoice, ScientificTesting, Stylistic]
)  # no order edges => parallel

# Historical Context and Documentation Review in sequence
HistDoc = StrictPartialOrder(
    nodes=[HistoricalContext, DocumentationReview]
)
HistDoc.order.add_edge(HistoricalContext, DocumentationReview)

# After parallel branches finish, join and then Legal Clearance, then HistDoc
JoinAndClearance = StrictPartialOrder(
    nodes=[ParallelBranches, LegalClearance, HistDoc]
)
JoinAndClearance.order.add_edge(ParallelBranches, LegalClearance)
JoinAndClearance.order.add_edge(LegalClearance, HistDoc)

# After HistDoc: Report Drafting -> Valuation Meeting -> Marketing Prep -> Final Approval
FinalSeq = StrictPartialOrder(
    nodes=[ReportDrafting, ValuationMeeting, MarketingPrep, FinalApproval]
)
FinalSeq.order.add_edge(ReportDrafting, ValuationMeeting)
FinalSeq.order.add_edge(ValuationMeeting, MarketingPrep)
FinalSeq.order.add_edge(MarketingPrep, FinalApproval)

# Now build the full process: Initial Intake and ConditionCheck, then ParallelBranches etc.

root = StrictPartialOrder(
    nodes=[ArtifactIntake, ConditionCheck, JoinAndClearance, FinalSeq]
)
root.order.add_edge(ArtifactIntake, ConditionCheck)
root.order.add_edge(ConditionCheck, JoinAndClearance)
root.order.add_edge(JoinAndClearance, FinalSeq)