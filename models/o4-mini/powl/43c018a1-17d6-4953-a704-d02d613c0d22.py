# Generated from: 43c018a1-17d6-4953-a704-d02d613c0d22.json
# Description: This process governs the detailed authentication of historical artifacts prior to acquisition by a museum or private collector. It involves multidisciplinary examination including provenance research, material analysis, and expert validation. The workflow integrates scientific testing methods such as radiocarbon dating and spectroscopy, alongside archival investigation and comparative stylistic analysis. Stakeholders coordinate through iterative reviews to confirm authenticity, assess conservation needs, and finalize acquisition terms. This atypical yet realistic business process ensures artifacts meet strict cultural and legal standards while minimizing risks of forgery or misattribution, ultimately preserving historical integrity and value.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
InitialReview       = Transition(label='Initial Review')
ProvenanceCheck     = Transition(label='Provenance Check')
MaterialSampling    = Transition(label='Material Sampling')
RadiocarbonTest     = Transition(label='Radiocarbon Test')
SpectroscopyScan    = Transition(label='Spectroscopy Scan')
StylisticCompare    = Transition(label='Stylistic Compare')
ArchivalSearch      = Transition(label='Archival Search')
ExpertConsult       = Transition(label='Expert Consult')
ConditionAssess     = Transition(label='Condition Assess')
ConservationPlan    = Transition(label='Conservation Plan')
RiskAnalysis        = Transition(label='Risk Analysis')
LegalVerify         = Transition(label='Legal Verify')
StakeholderReview   = Transition(label='Stakeholder Review')
AcquisitionOffer    = Transition(label='Acquisition Offer')
FinalApproval       = Transition(label='Final Approval')

# Sub-workflow for iterative review loop (B)
B = StrictPartialOrder(nodes=[ConditionAssess, ConservationPlan, RiskAnalysis, LegalVerify])
B.order.add_edge(ConditionAssess, ConservationPlan)
B.order.add_edge(ConservationPlan, RiskAnalysis)
B.order.add_edge(RiskAnalysis, LegalVerify)

# Loop operator: StakeholderReview is A, B is the refinement block
review_loop = OperatorPOWL(operator=Operator.LOOP, children=[StakeholderReview, B])

# Root partial order
root = StrictPartialOrder(nodes=[
    InitialReview,
    ProvenanceCheck,
    MaterialSampling,
    RadiocarbonTest,
    SpectroscopyScan,
    StylisticCompare,
    ArchivalSearch,
    ExpertConsult,
    review_loop,
    AcquisitionOffer,
    FinalApproval
])

# Define concurrency and sequencing
root.order.add_edge(InitialReview, ProvenanceCheck)
root.order.add_edge(InitialReview, MaterialSampling)
root.order.add_edge(InitialReview, ArchivalSearch)
root.order.add_edge(InitialReview, StylisticCompare)

root.order.add_edge(MaterialSampling, RadiocarbonTest)
root.order.add_edge(MaterialSampling, SpectroscopyScan)

root.order.add_edge(ProvenanceCheck, ExpertConsult)
root.order.add_edge(RadiocarbonTest,   ExpertConsult)
root.order.add_edge(SpectroscopyScan,  ExpertConsult)
root.order.add_edge(StylisticCompare,  ExpertConsult)
root.order.add_edge(ArchivalSearch,    ExpertConsult)

root.order.add_edge(ExpertConsult, review_loop)
root.order.add_edge(review_loop,   AcquisitionOffer)
root.order.add_edge(AcquisitionOffer, FinalApproval)