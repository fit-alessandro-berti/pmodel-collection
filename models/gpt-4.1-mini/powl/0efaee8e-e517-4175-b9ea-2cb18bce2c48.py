# Generated from: 0efaee8e-e517-4175-b9ea-2cb18bce2c48.json
# Description: This process involves collaboratively developing a new artisan cheese recipe by engaging a global community of cheese enthusiasts, dairy farmers, and food scientists. It begins with ideation where participants submit flavor profiles and ingredient suggestions, followed by crowd voting to select the top concepts. Selected concepts undergo prototype development by local cheesemakers, with iterative feedback collected through virtual tastings. Quality control experts analyze feedback and adjust processes accordingly. Legal teams ensure compliance with food safety standards and intellectual property rights. Marketing specialists then craft storytelling campaigns highlighting the collaborative nature of the cheese creation. Finally, distribution partners coordinate limited release shipments to backers and specialty retailers, maintaining traceability and customer engagement throughout the launch phase.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as labeled transitions
IdeaSubmit = Transition(label='Idea Submit')
FlavorVote = Transition(label='Flavor Vote')
ConceptSelect = Transition(label='Concept Select')
PrototypeMake = Transition(label='Prototype Make')
FeedbackGather = Transition(label='Feedback Gather')
TasteTest = Transition(label='Taste Test')
AdjustRecipe = Transition(label='Adjust Recipe')
QualityCheck = Transition(label='Quality Check')
RegulationReview = Transition(label='Regulation Review')
IPRegister = Transition(label='IP Register')
StoryCraft = Transition(label='Story Craft')
CampaignLaunch = Transition(label='Campaign Launch')
OrderManage = Transition(label='Order Manage')
ShipmentPlan = Transition(label='Shipment Plan')
CustomerEngage = Transition(label='Customer Engage')
TraceabilityLog = Transition(label='Traceability Log')

# Define the iterative feedback loop: PrototypeMake -> (FeedbackGather -> TasteTest -> AdjustRecipe) repeated
# Loop operator: body: PrototypeMake; redo: FeedbackGather->TasteTest->AdjustRecipe (then back to PrototypeMake)
feedback_loop_body = PrototypeMake
feedback_loop_redo_po = StrictPartialOrder(nodes=[FeedbackGather, TasteTest, AdjustRecipe])
feedback_loop_redo_po.order.add_edge(FeedbackGather, TasteTest)
feedback_loop_redo_po.order.add_edge(TasteTest, AdjustRecipe)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop_body, feedback_loop_redo_po])

# Parallel QC and Legal steps after the feedback loop:
# QualityCheck
# RegulationReview -> IPRegister (legal compliance chain)
legal_po = StrictPartialOrder(nodes=[RegulationReview, IPRegister])
legal_po.order.add_edge(RegulationReview, IPRegister)

# Parallel QC and Legal group
qc_legal_po = StrictPartialOrder(nodes=[QualityCheck, legal_po])
qc_legal_po.order.add_edge(QualityCheck, legal_po)  # To ensure the QC and Legal group follows feedback loop

# Technically, the nodes of StrictPartialOrder are directly transitions or OperatorPOWL, but the example shows nodes can be OperatorPOWL. 
# So legal_po can be a node inside qc_legal_po nodes.

# However, edge from QualityCheck to legal_po (which is an OperatorPOWL) might work as per example.
# But to avoid confusion, let's flatten legal_po nodes into qc_legal_po, ordering them properly.

qc_legal_nodes = [QualityCheck, RegulationReview, IPRegister]
qc_legal_po = StrictPartialOrder(nodes=qc_legal_nodes)
qc_legal_po.order.add_edge(RegulationReview, IPRegister)
# No direct ordering between QualityCheck and legal nodes, so they are concurrent after feedback_loop

# After QC and Legal, Marketing steps: StoryCraft -> CampaignLaunch
marketing_po = StrictPartialOrder(nodes=[StoryCraft, CampaignLaunch])
marketing_po.order.add_edge(StoryCraft, CampaignLaunch)

# Finally Distribution: OrderManage -> ShipmentPlan -> (CustomerEngage & TraceabilityLog concurrent)
distribution_po = StrictPartialOrder(
    nodes=[OrderManage, ShipmentPlan, CustomerEngage, TraceabilityLog]
)
distribution_po.order.add_edge(OrderManage, ShipmentPlan)
distribution_po.order.add_edge(ShipmentPlan, CustomerEngage)
distribution_po.order.add_edge(ShipmentPlan, TraceabilityLog)
# CustomerEngage and TraceabilityLog are concurrent (no edge between them)

# Now build the entire process partial order as:
# IdeaSubmit -> FlavorVote -> ConceptSelect -> feedback_loop -> qc_legal_po -> marketing_po -> distribution_po

root_nodes = [
    IdeaSubmit,
    FlavorVote,
    ConceptSelect,
    feedback_loop,
    qc_legal_po,
    marketing_po,
    distribution_po
]

root = StrictPartialOrder(nodes=root_nodes)

# Define the ordering edges

root.order.add_edge(IdeaSubmit, FlavorVote)
root.order.add_edge(FlavorVote, ConceptSelect)
root.order.add_edge(ConceptSelect, feedback_loop)
root.order.add_edge(feedback_loop, qc_legal_po)
root.order.add_edge(qc_legal_po, marketing_po)
root.order.add_edge(marketing_po, distribution_po)