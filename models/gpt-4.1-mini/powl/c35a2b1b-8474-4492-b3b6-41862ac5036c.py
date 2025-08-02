# Generated from: c35a2b1b-8474-4492-b3b6-41862ac5036c.json
# Description: This process involves the meticulous examination and validation of antique artifacts to verify authenticity and provenance. It includes initial physical inspection, material composition analysis, historical cross-referencing, expert consultations, and provenance documentation. The process integrates advanced imaging techniques, such as X-ray fluorescence and infrared spectroscopy, to detect restorations or forgeries. Additionally, market trend analysis and auction history reviews are conducted to assess value fluctuations. The final stage consolidates all findings into a comprehensive authenticity report, which is then approved by a certification board before the artifact is released for sale or exhibition. Throughout the process, strict chain-of-custody protocols are maintained to ensure integrity and prevent tampering or misplacement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Initial_Inspect = Transition(label='Initial Inspect')
Material_Test = Transition(label='Material Test')
Imaging_Scan = Transition(label='Imaging Scan')
Historical_Check = Transition(label='Historical Check')
Expert_Consult = Transition(label='Expert Consult')
Provenance_Trace = Transition(label='Provenance Trace')
Forgery_Detect = Transition(label='Forgery Detect')
Restoration_Map = Transition(label='Restoration Map')
Market_Analyze = Transition(label='Market Analyze')
Auction_Review = Transition(label='Auction Review')
Value_Assess = Transition(label='Value Assess')
Report_Draft = Transition(label='Report Draft')
Board_Review = Transition(label='Board Review')
Certification = Transition(label='Certification')
Release_Artifact = Transition(label='Release Artifact')
Chain_Custody = Transition(label='Chain Custody')

# Chain Custody protocol maintained throughout,
# so model Chain_Custody concurrent with all main activities or 
# as a partial order with all activities depending on Chain_Custody start

# Group the imaging techniques as a partial order (can be concurrent or sequential),
# since these are advanced scans to detect restorations or forgery:
# Imaging activities: Imaging_Scan, Forgery_Detect, Restoration_Map
imaging_PO = StrictPartialOrder(nodes=[Imaging_Scan, Forgery_Detect, Restoration_Map])
# Assume Imaging_Scan --> Forgery_Detect and Imaging_Scan --> Restoration_Map (scanning first, then analysis)
imaging_PO.order.add_edge(Imaging_Scan, Forgery_Detect)
imaging_PO.order.add_edge(Imaging_Scan, Restoration_Map)

# Group market assessments activities: Market_Analyze, Auction_Review, Value_Assess
market_PO = StrictPartialOrder(nodes=[Market_Analyze, Auction_Review, Value_Assess])
# Assume Market_Analyze --> Auction_Review --> Value_Assess sequentially
market_PO.order.add_edge(Market_Analyze, Auction_Review)
market_PO.order.add_edge(Auction_Review, Value_Assess)

# Group the provenance and historical research: Historical_Check, Expert_Consult, Provenance_Trace
# Model as partial order with historical check branching to expert consult and provenance trace concurrently
hist_PO = StrictPartialOrder(nodes=[Historical_Check, Expert_Consult, Provenance_Trace])
hist_PO.order.add_edge(Historical_Check, Expert_Consult)
hist_PO.order.add_edge(Historical_Check, Provenance_Trace)

# Model initial inspection and material test as sequential steps at the start
initial_PO = StrictPartialOrder(nodes=[Initial_Inspect, Material_Test])
initial_PO.order.add_edge(Initial_Inspect, Material_Test)

# All these investigations (initial_PO, hist_PO, imaging_PO, market_PO) can be partially ordered:
# Let's consider that material test precedes historical check, imaging scan, and market analyses
# So Material_Test --> Historical_Check, Material_Test --> Imaging_Scan, Material_Test --> Market_Analyze
# We'll construct a larger PO including all nodes and submodels as nodes

# Create the main partial order with all nodes (using the submodels as nodes where appropriate)
# For final linearity, chain control flow for final report:
# Report_Draft -> Board_Review -> Certification -> Release_Artifact

# Construct a combined partial order that respects all dependencies

# Combine all activity nodes and the sub-POWL nodes into a single PO

# Nodes to include:
# - initial_PO (composed of Initial_Inspect and Material_Test)
# - hist_PO (Historical_Check, Expert_Consult, Provenance_Trace)
# - imaging_PO (Imaging_Scan, Forgery_Detect, Restoration_Map)
# - market_PO (Market_Analyze, Auction_Review, Value_Assess)
# - Report_Draft
# - Board_Review
# - Certification
# - Release_Artifact
# - Chain_Custody

# Because StrictPartialOrder nodes must be atomic POWL models (Transition or OperatorPOWL or StrictPartialOrder)

# To connect initial_PO to others, initial_PO and hist_PO etc. have to be embedded as nodes at top-level PO

# So define top-level root PO with nodes:
# initial_PO, hist_PO, imaging_PO, market_PO, Report_Draft, Board_Review, Certification, Release_Artifact, Chain_Custody

# Edges:
# initial_PO --> hist_PO
# initial_PO --> imaging_PO
# initial_PO --> market_PO
# hist_PO, imaging_PO, market_PO --> Report_Draft
# Report_Draft --> Board_Review --> Certification --> Release_Artifact

# Finally, Chain_Custody runs concurrently but conceptually spans entire process
# Model Chain_Custody concurrent with initial_PO (start) and as predecessor of Report_Draft
# To model strict chain custody, add edges Chain_Custody --> initial_PO and Chain_Custody --> Report_Draft
# to ensure it starts early and still occurs before final report

root = StrictPartialOrder(
    nodes=[
        initial_PO,
        hist_PO,
        imaging_PO,
        market_PO,
        Report_Draft,
        Board_Review,
        Certification,
        Release_Artifact,
        Chain_Custody
    ]
)

# add edges to root PO
root.order.add_edge(Chain_Custody, initial_PO)
root.order.add_edge(Chain_Custody, Report_Draft)

root.order.add_edge(initial_PO, hist_PO)
root.order.add_edge(initial_PO, imaging_PO)
root.order.add_edge(initial_PO, market_PO)

root.order.add_edge(hist_PO, Report_Draft)
root.order.add_edge(imaging_PO, Report_Draft)
root.order.add_edge(market_PO, Report_Draft)

root.order.add_edge(Report_Draft, Board_Review)
root.order.add_edge(Board_Review, Certification)
root.order.add_edge(Certification, Release_Artifact)