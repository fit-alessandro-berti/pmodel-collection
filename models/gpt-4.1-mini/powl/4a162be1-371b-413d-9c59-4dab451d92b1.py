# Generated from: 4a162be1-371b-413d-9c59-4dab451d92b1.json
# Description: This process involves identifying emerging technologies from unrelated industries and systematically adapting them for novel applications within a company's core sector. It starts with cross-sector research, followed by ideation workshops that blend diverse perspectives. Prototyping leverages rapid iteration and external collaborations. Validation includes multi-disciplinary testing and market simulations. Implementation requires customized integration planning and change management. Finally, continuous feedback loops ensure scalability and sustained innovation, fostering a culture that embraces unconventional problem-solving and leverages external knowledge ecosystems to maintain competitive advantage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transition instances
TrendScan = Transition(label='Trend Scan')
TechHarvest = Transition(label='Tech Harvest')
IdeaMerge = Transition(label='Idea Merge')
ConceptSketch = Transition(label='Concept Sketch')
RapidPrototype = Transition(label='Rapid Prototype')
ExpertReview = Transition(label='Expert Review')
CrossTest = Transition(label='Cross-Test')
MarketSimulate = Transition(label='Market Simulate')
IntegrationPlan = Transition(label='Integration Plan')
ChangeAlign = Transition(label='Change Align')
PilotDeploy = Transition(label='Pilot Deploy')
FeedbackLoop = Transition(label='Feedback Loop')
ScaleUp = Transition(label='Scale Up')
KnowledgeShare = Transition(label='Knowledge Share')
CultureEmbed = Transition(label='Culture Embed')

# Step 1: (Trend Scan --> Tech Harvest)
step1 = StrictPartialOrder(nodes=[TrendScan, TechHarvest])
step1.order.add_edge(TrendScan, TechHarvest)

# Step 2: (Idea Merge --> Concept Sketch)
step2 = StrictPartialOrder(nodes=[IdeaMerge, ConceptSketch])
step2.order.add_edge(IdeaMerge, ConceptSketch)

# Step 3: Loop for prototyping and validation:
# Loop body A: Rapid Prototype
# Loop body B: (Expert Review and Cross-Test and Market Simulate)
# Because Expert Review, Cross-Test, Market Simulate are multi-disciplinary testing and market simulations = concurrent validation activities

validation = StrictPartialOrder(nodes=[ExpertReview, CrossTest, MarketSimulate])
# concurrent (no order) among ExpertReview, CrossTest, MarketSimulate

# Loop B is the validation phase, then repeat RapidPrototype
# So loop = * (Rapid Prototype, validation)

loop_prototype_validation = OperatorPOWL(operator=Operator.LOOP, children=[RapidPrototype, validation])

# Step 4: Implementation phase (Integration Plan --> Change Align --> Pilot Deploy)
implementation = StrictPartialOrder(nodes=[IntegrationPlan, ChangeAlign, PilotDeploy])
implementation.order.add_edge(IntegrationPlan, ChangeAlign)
implementation.order.add_edge(ChangeAlign, PilotDeploy)

# Step 5: Feedback and scaling:
# Feedback Loop --> Scale Up
feedback_scale = StrictPartialOrder(nodes=[FeedbackLoop, ScaleUp])
feedback_scale.order.add_edge(FeedbackLoop, ScaleUp)

# Step 6: Knowledge share and culture embedding concur with scaling
# So create concurrency of Knowledge Share and Culture Embed with feedback_scale
feedback_scale_know_culture = StrictPartialOrder(nodes=[feedback_scale, KnowledgeShare, CultureEmbed])
# feedback_scale is a PO node, so actually its nodes are feedback_scale + KShare + CEmbed
# But feedback_scale is StrictPartialOrder instance so we flatten nodes:
# We'll merge nodes of feedback_scale + KShare + CEmbed
nodes_feedback_plus = [FeedbackLoop, ScaleUp, KnowledgeShare, CultureEmbed]
feedback_plus = StrictPartialOrder(nodes=nodes_feedback_plus)
feedback_plus.order.add_edge(FeedbackLoop, ScaleUp)
# KnowledgeShare and CultureEmbed are concurrent with feedback chain, no edges added

# Define overall flow:
# trendScan --> techHarvest --> (ideaMerge --> conceptSketch) --> loop_prototype_validation --> implementation --> feedback_plus

# Link step1 and step2 concurrently, as per description ideation workshops blend diverse perspectives,
# so Tech Harvest leads to Idea Merge concurrency is less plausible,
# but natural sequence seems Trend Scan -> Tech Harvest -> Idea Merge -> Concept Sketch

# So sequential from Trend Scan to Concept Sketch via Tech Harvest and Idea Merge
# 1: TrendScan-->TechHarvest order already in step1
# Include step2 in main PO with edge TechHarvest --> IdeaMerge
main_early = StrictPartialOrder(nodes=[TrendScan, TechHarvest, IdeaMerge, ConceptSketch])
main_early.order.add_edge(TrendScan, TechHarvest)
main_early.order.add_edge(TechHarvest, IdeaMerge)
main_early.order.add_edge(IdeaMerge, ConceptSketch)

# Create the whole process StrictPartialOrder nodes
# Nodes: main_early PO, loop_prototype_validation, implementation PO, feedback_plus PO

root = StrictPartialOrder(
    nodes=[main_early, loop_prototype_validation, implementation, feedback_plus]
)
# Order edges:
# main_early --> loop_prototype_validation
root.order.add_edge(main_early, loop_prototype_validation)
# loop_prototype_validation --> implementation
root.order.add_edge(loop_prototype_validation, implementation)
# implementation --> feedback_plus
root.order.add_edge(implementation, feedback_plus)