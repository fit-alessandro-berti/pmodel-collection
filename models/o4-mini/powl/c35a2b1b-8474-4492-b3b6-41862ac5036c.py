# Generated from: c35a2b1b-8474-4492-b3b6-41862ac5036c.json
# Description: This process involves the meticulous examination and validation of antique artifacts to verify authenticity and provenance. It includes initial physical inspection, material composition analysis, historical cross-referencing, expert consultations, and provenance documentation. The process integrates advanced imaging techniques, such as X-ray fluorescence and infrared spectroscopy, to detect restorations or forgeries. Additionally, market trend analysis and auction history reviews are conducted to assess value fluctuations. The final stage consolidates all findings into a comprehensive authenticity report, which is then approved by a certification board before the artifact is released for sale or exhibition. Throughout the process, strict chain-of-custody protocols are maintained to ensure integrity and prevent tampering or misplacement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define the activities as POWL transitions
InitialInspect   = Transition(label='Initial Inspect')
MaterialTest     = Transition(label='Material Test')
ImagingScan      = Transition(label='Imaging Scan')
ForgeryDetect    = Transition(label='Forgery Detect')
RestorationMap   = Transition(label='Restoration Map')
HistoricalCheck  = Transition(label='Historical Check')
ProvenanceTrace  = Transition(label='Provenance Trace')
ExpertConsult    = Transition(label='Expert Consult')
MarketAnalyze    = Transition(label='Market Analyze')
AuctionReview    = Transition(label='Auction Review')
ValueAssess      = Transition(label='Value Assess')
ReportDraft      = Transition(label='Report Draft')
BoardReview      = Transition(label='Board Review')
Certification    = Transition(label='Certification')
ReleaseArtifact  = Transition(label='Release Artifact')
ChainCustody     = Transition(label='Chain Custody')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    ChainCustody,
    InitialInspect, MaterialTest, ImagingScan,
    ForgeryDetect, RestorationMap,
    HistoricalCheck, ProvenanceTrace, ExpertConsult,
    MarketAnalyze, AuctionReview,
    ValueAssess, ReportDraft, BoardReview,
    Certification, ReleaseArtifact
])

# Enforce that chain‐of‐custody is established before anything else
root.order.add_edge(ChainCustody, InitialInspect)

# Core sequential flow
root.order.add_edge(InitialInspect, MaterialTest)
root.order.add_edge(MaterialTest, ImagingScan)

# After imaging, fork into two parallel subprocesses
root.order.add_edge(ImagingScan, ForgeryDetect)
root.order.add_edge(ImagingScan, RestorationMap)

# Join back to the historical check once both imaging analyses complete
root.order.add_edge(ForgeryDetect, HistoricalCheck)
root.order.add_edge(RestorationMap, HistoricalCheck)

# Continue the linear history/provenance flow
root.order.add_edge(HistoricalCheck, ProvenanceTrace)
root.order.add_edge(ProvenanceTrace, ExpertConsult)

# Parallel market/auction analysis after expert consultation
root.order.add_edge(ExpertConsult, MarketAnalyze)
root.order.add_edge(ExpertConsult, AuctionReview)

# Join to value assessment
root.order.add_edge(MarketAnalyze, ValueAssess)
root.order.add_edge(AuctionReview, ValueAssess)

# Final consolidation and approval
root.order.add_edge(ValueAssess, ReportDraft)
root.order.add_edge(ReportDraft, BoardReview)
root.order.add_edge(BoardReview, Certification)
root.order.add_edge(Certification, ReleaseArtifact)