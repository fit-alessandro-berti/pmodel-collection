# Generated from: 05028ada-2daf-488d-9f2d-e52627886b6e.json
# Description: This process involves the detailed authentication of antique artifacts for auction purposes. It starts with initial provenance research, followed by physical inspection using multispectral imaging and material analysis. Experts then perform stylistic comparison and historical context validation. Next, the artifact undergoes chemical composition testing to detect modern materials or restorations. Afterward, 3D scanning and digital reconstruction help in assessing craftsmanship accuracy. A collaborative review session with historians and conservators determines authenticity consensus. Finally, a detailed report is compiled, including risk assessment and valuation recommendations before the artifact is approved for auction listing.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Provenance_Check = Transition(label='Provenance Check')
Visual_Inspect = Transition(label='Visual Inspect')
Imaging_Scan = Transition(label='Imaging Scan')
Material_Test = Transition(label='Material Test')
Style_Compare = Transition(label='Style Compare')
Context_Validate = Transition(label='Context Validate')
Chemical_Analysis = Transition(label='Chemical Analysis')
Scan_3D = Transition(label='3D Scan')
Digital_Model = Transition(label='Digital Model')
Expert_Review = Transition(label='Expert Review')
Consensus_Meet = Transition(label='Consensus Meet')
Risk_Assess = Transition(label='Risk Assess')
Valuation_Prep = Transition(label='Valuation Prep')
Report_Compile = Transition(label='Report Compile')
Auction_Listing = Transition(label='Auction Listing')

# Partial orders for first inspection phase (Visual Inspect & Imaging Scan & Material Test concurrent)
inspection_phase = StrictPartialOrder(nodes=[Visual_Inspect, Imaging_Scan, Material_Test])

# Partial orders for expert analysis (Style Compare and Context Validate concurrent)
expert_analysis = StrictPartialOrder(nodes=[Style_Compare, Context_Validate])

# Partial orders for 3D scan & digital modeling (sequential)
scan_and_model = StrictPartialOrder(nodes=[Scan_3D, Digital_Model])
scan_and_model.order.add_edge(Scan_3D, Digital_Model)

# Partial order for collaborative review (Expert Review then Consensus Meet sequential)
collaborative_review = StrictPartialOrder(nodes=[Expert_Review, Consensus_Meet])
collaborative_review.order.add_edge(Expert_Review, Consensus_Meet)

# Partial order for final reporting phase (Risk Assess, Valuation Prep concurrent)
report_prep = StrictPartialOrder(nodes=[Risk_Assess, Valuation_Prep])

# Final reporting sequence: (Risk Assess + Valuation Prep) -> Report Compile
final_reporting = StrictPartialOrder(nodes=[report_prep, Report_Compile])
final_reporting.order.add_edge(report_prep, Report_Compile)

# Build the entire partial order with all nodes and edges
root = StrictPartialOrder(
    nodes=[
        Provenance_Check,
        inspection_phase,
        expert_analysis,
        Chemical_Analysis,
        scan_and_model,
        collaborative_review,
        final_reporting,
        Auction_Listing
    ]
)

# Add edges for the sequence from description:
# Provenance Check --> inspection_phase
root.order.add_edge(Provenance_Check, inspection_phase)
# inspection_phase --> expert_analysis
root.order.add_edge(inspection_phase, expert_analysis)
# expert_analysis --> Chemical Analysis
root.order.add_edge(expert_analysis, Chemical_Analysis)
# Chemical Analysis --> scan_and_model
root.order.add_edge(Chemical_Analysis, scan_and_model)
# scan_and_model --> collaborative_review
root.order.add_edge(scan_and_model, collaborative_review)
# collaborative_review --> final_reporting
root.order.add_edge(collaborative_review, final_reporting)
# final_reporting --> Auction Listing
root.order.add_edge(final_reporting, Auction_Listing)