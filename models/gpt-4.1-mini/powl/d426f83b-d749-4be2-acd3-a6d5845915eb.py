# Generated from: d426f83b-d749-4be2-acd3-a6d5845915eb.json
# Description: This process involves the detailed verification and authentication of antique assets for high-value collectors and museums, incorporating provenance research, material analysis, expert consultation, and condition assessment. The process begins with initial asset intake, followed by multi-layered investigation including historical document cross-checking, scientific testing such as radiocarbon dating or spectroscopy, and comparative stylistic evaluation. Findings are then compiled into a detailed authentication report, which undergoes peer review by external specialists. The final step involves certification issuance and digital archiving of the asset’s verified profile. This atypical but realistic process ensures the legitimacy and value preservation of rare antiques in a market fraught with forgery risks.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions (activities)
AssetIntake = Transition(label='Asset Intake')
ProvenanceCheck = Transition(label='Provenance Check')
MaterialSampling = Transition(label='Material Sampling')
RadiocarbonTest = Transition(label='Radiocarbon Test')
StyleCompare = Transition(label='Style Compare')
HistoricalSearch = Transition(label='Historical Search')
ExpertConsult = Transition(label='Expert Consult')
ConditionReview = Transition(label='Condition Review')
ScientificAnalysis = Transition(label='Scientific Analysis')
DataCompilation = Transition(label='Data Compilation')
PeerReview = Transition(label='Peer Review')
ReportDraft = Transition(label='Report Draft')
Certification = Transition(label='Certification')
DigitalArchive = Transition(label='Digital Archive')
ClientDelivery = Transition(label='Client Delivery')

# Multi-layered investigation partial order:
# Historical document cross-checking: ProvenanceCheck, HistoricalSearch
# Scientific testing: MaterialSampling -> ScientificAnalysis with RadiocarbonTest and StyleCompare as parallel subtasks after MaterialSampling
# Expert consultation (ExpertConsult) and condition assessment (ConditionReview) done concurrently (parallel)
# Structure:

# Scientific testing branch:
# MaterialSampling --> (RadiocarbonTest, StyleCompare) in parallel --> ScientificAnalysis

scientific_subPO = StrictPartialOrder(
    nodes=[MaterialSampling, RadiocarbonTest, StyleCompare, ScientificAnalysis]
)
scientific_subPO.order.add_edge(MaterialSampling, RadiocarbonTest)
scientific_subPO.order.add_edge(MaterialSampling, StyleCompare)
scientific_subPO.order.add_edge(RadiocarbonTest, ScientificAnalysis)
scientific_subPO.order.add_edge(StyleCompare, ScientificAnalysis)

# Historical investigation branch (ProvenanceCheck and HistoricalSearch concurrent)
historical_subPO = StrictPartialOrder(
    nodes=[ProvenanceCheck, HistoricalSearch]
)
# no order edges: concurrent

# ExpertConsult and ConditionReview concurrent
expert_condition_PO = StrictPartialOrder(
    nodes=[ExpertConsult, ConditionReview]
)
# no order edges: concurrent

# Combine all investigation tasks in partial order:
# ProvenanceCheck and HistoricalSearch concurrent
# MaterialSampling branch from scientific_subPO
# ExpertConsult and ConditionReview concurrent
# All these four groups (ProvenanceCheck, HistoricalSearch, scientific_subPO, ExpertConsult, ConditionReview) concurrent with each other at this level
# So overall nodes = provenance, historical, scientific_subPO, expert_condition_PO flattened into single PO with only the internal edges

# To represent this: create a PO combining all nodes; the orders inside scientific_subPO remain, other nodes concurrent.

investigation_nodes = [
    ProvenanceCheck,
    HistoricalSearch,
    MaterialSampling,
    RadiocarbonTest,
    StyleCompare,
    ScientificAnalysis,
    ExpertConsult,
    ConditionReview,
]

investigation_PO = StrictPartialOrder(nodes=investigation_nodes)
# add scientific_subPO edges
investigation_PO.order.add_edge(MaterialSampling, RadiocarbonTest)
investigation_PO.order.add_edge(MaterialSampling, StyleCompare)
investigation_PO.order.add_edge(RadiocarbonTest, ScientificAnalysis)
investigation_PO.order.add_edge(StyleCompare, ScientificAnalysis)
# no other order edges, so:
# ProvenanceCheck, HistoricalSearch concurrent with the scientific tasks and expert_condition tasks

# Now model process flow:

# 1. Asset Intake --> investigation_PO
# 2. investigation_PO --> DataCompilation
# 3. DataCompilation --> PeerReview --> ReportDraft
# 4. ReportDraft --> Certification --> DigitalArchive --> ClientDelivery

root = StrictPartialOrder(
    nodes=[
        AssetIntake,
        investigation_PO,
        DataCompilation,
        PeerReview,
        ReportDraft,
        Certification,
        DigitalArchive,
        ClientDelivery,
    ]
)

# Add order edges

root.order.add_edge(AssetIntake, investigation_PO)    # intake before investigation
root.order.add_edge(investigation_PO, DataCompilation)  # investigation before compile
root.order.add_edge(DataCompilation, PeerReview)
root.order.add_edge(PeerReview, ReportDraft)
root.order.add_edge(ReportDraft, Certification)
root.order.add_edge(Certification, DigitalArchive)
root.order.add_edge(DigitalArchive, ClientDelivery)