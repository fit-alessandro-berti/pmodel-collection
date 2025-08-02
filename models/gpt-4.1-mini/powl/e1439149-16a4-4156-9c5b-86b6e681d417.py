# Generated from: e1439149-16a4-4156-9c5b-86b6e681d417.json
# Description: This process involves systematically sourcing ideas from unrelated industries to foster breakthrough innovations. It begins with environmental scanning to identify emerging trends outside the core market, followed by cross-functional ideation workshops. Concepts are refined through rapid prototyping and iterative feedback loops involving external experts. Parallel feasibility assessments ensure resource alignment and risk mitigation. The process culminates with pilot deployments in controlled environments, capturing performance data to inform scaling decisions. Continuous learning and knowledge sharing across departments embed innovation into the organizational culture, enabling sustained competitive advantage through unconventional approaches.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
TrendScan = Transition(label='Trend Scan')
IdeaHarvest = Transition(label='Idea Harvest')
WorkshopHost = Transition(label='Workshop Host')
ConceptFilter = Transition(label='Concept Filter')
PrototypeBuild = Transition(label='Prototype Build')
ExpertReview = Transition(label='Expert Review')
FeasibilityCheck = Transition(label='Feasibility Check')
RiskAssess = Transition(label='Risk Assess')
PilotLaunch = Transition(label='Pilot Launch')
DataCapture = Transition(label='Data Capture')
PerformanceReview = Transition(label='Performance Review')
ScalePlan = Transition(label='Scale Plan')
ResourceAlign = Transition(label='Resource Align')
LearnShare = Transition(label='Learn Share')
CultureEmbed = Transition(label='Culture Embed')

# Build loop: Prototype Build + Expert Review repeated until done
loopIterativeFeedback = OperatorPOWL(operator=Operator.LOOP, children=[PrototypeBuild, ExpertReview])

# Parallel feasibility assessments: Feasibility Check and Risk Assess concurrent
feasibilityPO = StrictPartialOrder(nodes=[FeasibilityCheck, RiskAssess])

# Pilot deployment sequence and capturing data, then performance review and scale plan
pilotSeq = StrictPartialOrder(
    nodes=[PilotLaunch, DataCapture, PerformanceReview, ScalePlan]
)
pilotSeq.order.add_edge(PilotLaunch, DataCapture)
pilotSeq.order.add_edge(DataCapture, PerformanceReview)
pilotSeq.order.add_edge(PerformanceReview, ScalePlan)

# Final learning and embedding loop: Learn Share then Culture Embed concurrently means partial order with LearnShare --> CultureEmbed
learnEmbed = StrictPartialOrder(nodes=[LearnShare, CultureEmbed])
learnEmbed.order.add_edge(LearnShare, CultureEmbed)

# First sequence: Trend Scan --> Idea Harvest --> Workshop Host --> Concept Filter
firstSeq = StrictPartialOrder(
    nodes=[TrendScan, IdeaHarvest, WorkshopHost, ConceptFilter]
)
firstSeq.order.add_edge(TrendScan, IdeaHarvest)
firstSeq.order.add_edge(IdeaHarvest, WorkshopHost)
firstSeq.order.add_edge(WorkshopHost, ConceptFilter)

# Connect Concept Filter to loopIterativeFeedback then to feasibilityPO
conceptToLoop = StrictPartialOrder(
    nodes=[ConceptFilter, loopIterativeFeedback, feasibilityPO]
)
conceptToLoop.order.add_edge(ConceptFilter, loopIterativeFeedback)
conceptToLoop.order.add_edge(ConceptFilter, feasibilityPO)

# After loop and feasibility, pilot sequence
afterLoopAndFeasibility = StrictPartialOrder(
    nodes=[loopIterativeFeedback, feasibilityPO, pilotSeq]
)
afterLoopAndFeasibility.order.add_edge(loopIterativeFeedback, pilotSeq)
afterLoopAndFeasibility.order.add_edge(feasibilityPO, pilotSeq)

# After pilotSeq, resource align and then learning embedding (learnShare -> cultureEmbed)
resourceAndLearning = StrictPartialOrder(
    nodes=[pilotSeq, ResourceAlign, learnEmbed]
)
resourceAndLearning.order.add_edge(pilotSeq, ResourceAlign)
resourceAndLearning.order.add_edge(ResourceAlign, learnEmbed)

# Combine all together: firstSeq --> conceptToLoop --> afterLoopAndFeasibility --> resourceAndLearning
root = StrictPartialOrder(
    nodes=[firstSeq, conceptToLoop, afterLoopAndFeasibility, resourceAndLearning]
)
root.order.add_edge(firstSeq, conceptToLoop)
root.order.add_edge(conceptToLoop, afterLoopAndFeasibility)
root.order.add_edge(afterLoopAndFeasibility, resourceAndLearning)