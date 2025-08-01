# Generated from: b8dd283d-41a3-4002-aeb5-4f49919ccda2.json
# Description: This process outlines an atypical yet realistic approach to foster innovation by integrating knowledge and resources from multiple unrelated industries. It begins with trend spotting across sectors, followed by opportunity mapping and collaborative ideation sessions with diverse expert teams. Prototypes are rapidly developed using cross-functional agile squads, then assessed through multi-criteria evaluation including sustainability, market fit, and technological feasibility. Feedback loops involve external stakeholders such as regulators and end-users to ensure compliance and practical relevance. Final concepts undergo iterative refinement before handoff to specialized commercialization units. This cyclical process encourages continuous learning and adaptability, ensuring that innovations remain relevant in dynamic markets and leverage unconventional synergies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions with labels exactly as requested
TrendSpotting = Transition(label='Trend Spotting')
OpportunityMap = Transition(label='Opportunity Map')
IdeaWorkshop = Transition(label='Idea Workshop')
TeamAssemble = Transition(label='Team Assemble')
RapidPrototype = Transition(label='Rapid Prototype')
FeasibilityCheck = Transition(label='Feasibility Check')
SustainabilityScan = Transition(label='Sustainability Scan')
MarketTesting = Transition(label='Market Testing')
StakeholderReview = Transition(label='Stakeholder Review')
RegulatorConsult = Transition(label='Regulator Consult')
UserFeedback = Transition(label='User Feedback')
IterationLoop = Transition(label='Iteration Loop')
RiskAssessment = Transition(label='Risk Assessment')
ConceptFinalize = Transition(label='Concept Finalize')
CommercialHandoff = Transition(label='Commercial Handoff')
PerformanceAudit = Transition(label='Performance Audit')

# Construct the multi-criteria evaluation partial order:
# FeasibilityCheck, SustainabilityScan, MarketTesting are done concurrently
MultiCriteriaEvaluation = StrictPartialOrder(nodes=[FeasibilityCheck, SustainabilityScan, MarketTesting])

# Stakeholder feedback loop involves RegulatorConsult and UserFeedback, then StakeholderReview
StakeholderFeedbackOrder = StrictPartialOrder(
    nodes=[RegulatorConsult, UserFeedback, StakeholderReview],
    # RegulatorConsult and UserFeedback concurrent, both precede StakeholderReview
)
StakeholderFeedbackOrder.order.add_edge(RegulatorConsult, StakeholderReview)
StakeholderFeedbackOrder.order.add_edge(UserFeedback, StakeholderReview)

# Iteration Loop is a loop on 'Iteration Loop' activity and after Stakeholder Review & Risk Assessment
# The iterative refinement is implied as a loop containing:
#   A: Iteration Loop (initial action in loop)
#   B: partial order of StakeholderReview and RiskAssessment before next iteration

# We consider Risk Assessment after Stakeholder Review as part of refinement
RefinementPart = StrictPartialOrder(nodes=[StakeholderReview, RiskAssessment])
RefinementPart.order.add_edge(StakeholderReview, RiskAssessment)

# Loop structure: first do Iteration Loop, then either exit or do RefinementPart then Iteration Loop again
Iteration = OperatorPOWL(operator=Operator.LOOP, children=[IterationLoop, RefinementPart])

# Agile protoyping partial order: Team Assemble --> Rapid Prototype --> MultiCriteriaEvaluation
AgileProtoPO = StrictPartialOrder(nodes=[TeamAssemble, RapidPrototype, MultiCriteriaEvaluation])
AgileProtoPO.order.add_edge(TeamAssemble, RapidPrototype)
AgileProtoPO.order.add_edge(RapidPrototype, MultiCriteriaEvaluation)

# Feedback loop - from MultiCriteriaEvaluation through StakeholderFeedbackOrder
FeedbackFlowPO = StrictPartialOrder(nodes=[MultiCriteriaEvaluation, StakeholderFeedbackOrder])
FeedbackFlowPO.order.add_edge(MultiCriteriaEvaluation, StakeholderFeedbackOrder)

# After feedback, go into Iteration loop
AfterFeedbackPO = StrictPartialOrder(
    nodes=[FeedbackFlowPO, Iteration]
)
AfterFeedbackPO.order.add_edge(FeedbackFlowPO, Iteration)

# Final sequence after iteration: Concept Finalize --> Commercial Handoff --> Performance Audit
FinalSeqPO = StrictPartialOrder(
    nodes=[ConceptFinalize, CommercialHandoff, PerformanceAudit]
)
FinalSeqPO.order.add_edge(ConceptFinalize, CommercialHandoff)
FinalSeqPO.order.add_edge(CommercialHandoff, PerformanceAudit)

# Connect flow from Iteration to final sequence 
IterToFinalPO = StrictPartialOrder(nodes=[Iteration, FinalSeqPO])
IterToFinalPO.order.add_edge(Iteration, FinalSeqPO)

# Initial three steps sequence: Trend Spotting --> Opportunity Map --> Idea Workshop
InitialSeq = StrictPartialOrder(nodes=[TrendSpotting, OpportunityMap, IdeaWorkshop])
InitialSeq.order.add_edge(TrendSpotting, OpportunityMap)
InitialSeq.order.add_edge(OpportunityMap, IdeaWorkshop)

# Idea Workshop --> Agile Proto (Team Assemble start)
InitialToAgilePO = StrictPartialOrder(nodes=[IdeaWorkshop, AgileProtoPO])
InitialToAgilePO.order.add_edge(IdeaWorkshop, AgileProtoPO)

# Aggregate model: 
# Initial sequence --> AgileProto --> FeedbackFlow --> Iteration Loop --> Final Sequence
# We connect these partial orders by edges:
root = StrictPartialOrder(
    nodes=[InitialSeq, InitialToAgilePO, AgileProtoPO, FeedbackFlowPO, AfterFeedbackPO, Iteration, FinalSeqPO, IterToFinalPO]
)

# Add edges if not implicit in the nested partial orders:
# These Composite partial orders embed parts, so we only add top-level edges:
# Link InitialSeq -> IdeaWorkshop to AgileProtoPO
root.order.add_edge(InitialSeq, AgileProtoPO)
# AgileProtoPO -> FeedbackFlowPO already connected inside, but to be sure:
root.order.add_edge(AgileProtoPO, FeedbackFlowPO)
# FeedbackFlowPO -> Iteration (via AfterFeedbackPO)
root.order.add_edge(FeedbackFlowPO, Iteration)
# Iteration -> FinalSeqPO
root.order.add_edge(Iteration, FinalSeqPO)