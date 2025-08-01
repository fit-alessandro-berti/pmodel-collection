# Generated from: e425f41a-416a-491d-8642-2f5bf6427ce6.json
# Description: This process outlines the creation of bespoke artisanal perfumes combining traditional crafting techniques with modern sensory analysis. It begins with ingredient sourcing from rare botanicals, followed by extraction and initial blending. Multiple rounds of sensory evaluation and chemical refinement ensure a balanced, unique scent profile. Packaging is customized per client preferences, including hand-labeling and bespoke containers. Throughout, quality control and regulatory compliance are maintained, culminating in limited edition releases that blend craftsmanship with innovation for luxury markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Ingredient_Sourcing = Transition(label='Ingredient Sourcing')
Botanical_Extraction = Transition(label='Botanical Extraction')
Initial_Blending = Transition(label='Initial Blending')
Sensory_Testing = Transition(label='Sensory Testing')
Chemical_Analysis = Transition(label='Chemical Analysis')
Recipe_Refinement = Transition(label='Recipe Refinement')
Stability_Check = Transition(label='Stability Check')
Client_Sampling = Transition(label='Client Sampling')
Feedback_Review = Transition(label='Feedback Review')
Final_Adjustment = Transition(label='Final Adjustment')
Custom_Packaging = Transition(label='Custom Packaging')
Label_Design = Transition(label='Label Design')
Hand_Labeling = Transition(label='Hand Labeling')
Regulatory_Audit = Transition(label='Regulatory Audit')
Batch_Documentation = Transition(label='Batch Documentation')
Limited_Release = Transition(label='Limited Release')
Market_Launch = Transition(label='Market Launch')

# Loop body: (Sensory Testing -> Chemical Analysis -> Recipe Refinement)
loop_body_order = StrictPartialOrder(nodes=[Sensory_Testing, Chemical_Analysis, Recipe_Refinement])
loop_body_order.order.add_edge(Sensory_Testing, Chemical_Analysis)
loop_body_order.order.add_edge(Chemical_Analysis, Recipe_Refinement)

# The loop:
# First do Sensory Testing, Chemical Analysis, Recipe Refinement (loop_body_order),
# then choose either to exit or repeat loop_body_order again.
# According to POWL loop: *(A,B) means execute A then loop choosing exit or B then A again.
# Here, A = loop_body_order, B = loop_body_order again.
# But since loop_body_order contains multiple nodes, and loop B should be "body again",
# we can model the loop as:
# LOOP(A=Sensory Testing->Chemical Analysis->Recipe Refinement, B=Sensory Testing->Chemical Analysis->Recipe Refinement)
# i.e. executing the loop body at least once, then repeatedly if chosen.

loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body_order, loop_body_order])

# Packaging partial order: Custom Packaging -> (Label Design & Hand Labeling in parallel)
packaging_po = StrictPartialOrder(
    nodes=[Custom_Packaging, Label_Design, Hand_Labeling]
)
packaging_po.order.add_edge(Custom_Packaging, Label_Design)
packaging_po.order.add_edge(Custom_Packaging, Hand_Labeling)

# Quality/control parallel activities (Regulatory Audit and Batch Documentation)
quality_po = StrictPartialOrder(
    nodes=[Regulatory_Audit, Batch_Documentation]
)

# Final release and market launch sequence
final_po = StrictPartialOrder(
    nodes=[Limited_Release, Market_Launch]
)
final_po.order.add_edge(Limited_Release, Market_Launch)

# Feedback-related partial order: Client Sampling -> Feedback Review -> Final Adjustment
feedback_po = StrictPartialOrder(
    nodes=[Client_Sampling, Feedback_Review, Final_Adjustment]
)
feedback_po.order.add_edge(Client_Sampling, Feedback_Review)
feedback_po.order.add_edge(Feedback_Review, Final_Adjustment)

# Source to initial blending
initial_sequence = StrictPartialOrder(
    nodes=[
        Ingredient_Sourcing,
        Botanical_Extraction,
        Initial_Blending
    ]
)
initial_sequence.order.add_edge(Ingredient_Sourcing, Botanical_Extraction)
initial_sequence.order.add_edge(Botanical_Extraction, Initial_Blending)

# Build the main partial order

# nodes:
# initial_sequence nodes + loop + feedback_po + Stability_Check + packaging_po + quality_po + final_po

# We form a top level PO with all these nodes:

root_nodes = [
    Ingredient_Sourcing,
    Botanical_Extraction,
    Initial_Blending,
    loop,
    feedback_po,
    Stability_Check,
    packaging_po,
    quality_po,
    final_po
]

root = StrictPartialOrder(nodes=root_nodes)

# Add dependencies (edges) between these nodes to reflect overall process order

# Initial blending before loop
root.order.add_edge(Initial_Blending, loop)

# Loop before stability check
root.order.add_edge(loop, Stability_Check)

# Stability check before feedback cycle starts
root.order.add_edge(Stability_Check, feedback_po)

# Feedback involved, after final adjustment we do packaging
root.order.add_edge(feedback_po, packaging_po)

# Packaging before quality checks
root.order.add_edge(packaging_po, quality_po)

# Quality control before limited release
root.order.add_edge(quality_po, final_po)