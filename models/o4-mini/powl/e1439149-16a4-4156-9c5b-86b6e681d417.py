# Generated from: e1439149-16a4-4156-9c5b-86b6e681d417.json
# Description: This process involves systematically sourcing ideas from unrelated industries to foster breakthrough innovations. It begins with environmental scanning to identify emerging trends outside the core market, followed by cross-functional ideation workshops. Concepts are refined through rapid prototyping and iterative feedback loops involving external experts. Parallel feasibility assessments ensure resource alignment and risk mitigation. The process culminates with pilot deployments in controlled environments, capturing performance data to inform scaling decisions. Continuous learning and knowledge sharing across departments embed innovation into the organizational culture, enabling sustained competitive advantage through unconventional approaches.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
TrendScan = Transition(label='Trend Scan')
IdeaHarvest = Transition(label='Idea Harvest')
WorkshopHost = Transition(label='Workshop Host')
ConceptFilter = Transition(label='Concept Filter')
PrototypeBuild = Transition(label='Prototype Build')
ExpertReview = Transition(label='Expert Review')
FeasibilityCheck = Transition(label='Feasibility Check')
RiskAssess = Transition(label='Risk Assess')
ResourceAlign = Transition(label='Resource Align')
PilotLaunch = Transition(label='Pilot Launch')
DataCapture = Transition(label='Data Capture')
PerformanceReview = Transition(label='Performance Review')
ScalePlan = Transition(label='Scale Plan')
LearnShare = Transition(label='Learn Share')
CultureEmbed = Transition(label='Culture Embed')

# Loop for prototyping + expert review
loop = OperatorPOWL(operator=Operator.LOOP, children=[PrototypeBuild, ExpertReview])

# Build the partial order
root = StrictPartialOrder(nodes=[
    TrendScan, IdeaHarvest, WorkshopHost, ConceptFilter,
    PrototypeBuild, ExpertReview, loop,
    FeasibilityCheck, RiskAssess, ResourceAlign,
    PilotLaunch, DataCapture, PerformanceReview, ScalePlan,
    LearnShare, CultureEmbed
])

# Define ordering constraints
# 1. Start: TrendScan -> {IdeaHarvest, WorkshopHost}
root.order.add_edge(TrendScan, IdeaHarvest)
root.order.add_edge(TrendScan, WorkshopHost)

# 2. Workshops finish before filtering
root.order.add_edge(IdeaHarvest, ConceptFilter)
root.order.add_edge(WorkshopHost, ConceptFilter)

# 3. After filtering, enter prototyping loop
root.order.add_edge(ConceptFilter, loop)

# 4. After loop, parallel feasibility and risk
root.order.add_edge(loop, FeasibilityCheck)
root.order.add_edge(loop, RiskAssess)

# 5. Resource alignment follows feasibility
root.order.add_edge(FeasibilityCheck, ResourceAlign)

# 6. Both risk and resource alignment must complete before pilot launch
root.order.add_edge(RiskAssess, PilotLaunch)
root.order.add_edge(ResourceAlign, PilotLaunch)

# 7. Pilot launch -> data capture -> performance review -> scale planning
root.order.add_edge(PilotLaunch, DataCapture)
root.order.add_edge(DataCapture, PerformanceReview)
root.order.add_edge(PerformanceReview, ScalePlan)

# 8. Scale plan -> learning & sharing -> embedding culture
root.order.add_edge(ScalePlan, LearnShare)
root.order.add_edge(LearnShare, CultureEmbed)