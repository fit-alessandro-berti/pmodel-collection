# Generated from: b8dd283d-41a3-4002-aeb5-4f49919ccda2.json
# Description: This process outlines an atypical yet realistic approach to foster innovation by integrating knowledge and resources from multiple unrelated industries. It begins with trend spotting across sectors, followed by opportunity mapping and collaborative ideation sessions with diverse expert teams. Prototypes are rapidly developed using cross-functional agile squads, then assessed through multi-criteria evaluation including sustainability, market fit, and technological feasibility. Feedback loops involve external stakeholders such as regulators and end-users to ensure compliance and practical relevance. Final concepts undergo iterative refinement before handoff to specialized commercialization units. This cyclical process encourages continuous learning and adaptability, ensuring that innovations remain relevant in dynamic markets and leverage unconventional synergies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
TrendSpotting     = Transition(label='Trend Spotting')
OpportunityMap    = Transition(label='Opportunity Map')
TeamAssemble      = Transition(label='Team Assemble')
IdeaWorkshop      = Transition(label='Idea Workshop')
RapidPrototype    = Transition(label='Rapid Prototype')
FeasibilityCheck  = Transition(label='Feasibility Check')
SustainabilityScan= Transition(label='Sustainability Scan')
MarketTesting     = Transition(label='Market Testing')
StakeholderReview = Transition(label='Stakeholder Review')
RegulatorConsult  = Transition(label='Regulator Consult')
UserFeedback      = Transition(label='User Feedback')
IterationLoop     = Transition(label='Iteration Loop')
RiskAssessment    = Transition(label='Risk Assessment')
ConceptFinalize   = Transition(label='Concept Finalize')
CommercialHandoff = Transition(label='Commercial Handoff')
PerformanceAudit  = Transition(label='Performance Audit')

# 1) Multi‐criteria evaluation (Feasibility, Sustainability, Market) in parallel
evaluation = StrictPartialOrder(
    nodes=[
        FeasibilityCheck,
        SustainabilityScan,
        MarketTesting
    ]
)
# no ordering edges → fully concurrent

# 2) Stakeholder feedback subprocess: one review, then parallel regulator & user feedback
stakeholder = StrictPartialOrder(
    nodes=[
        StakeholderReview,
        RegulatorConsult,
        UserFeedback
    ]
)
stakeholder.order.add_edge(StakeholderReview, RegulatorConsult)
stakeholder.order.add_edge(StakeholderReview, UserFeedback)

# 3) Body of the iteration loop: prototype → evaluation → stakeholder → risk assessment
bodyA = StrictPartialOrder(
    nodes=[
        RapidPrototype,
        evaluation,
        stakeholder,
        RiskAssessment
    ]
)
bodyA.order.add_edge(RapidPrototype, evaluation)
bodyA.order.add_edge(evaluation, stakeholder)
bodyA.order.add_edge(stakeholder, RiskAssessment)

# 4) Loop operator: repeat bodyA or exit on IterationLoop
iteration_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[bodyA, IterationLoop]
)

# 5) Main process partial order
root = StrictPartialOrder(
    nodes=[
        TrendSpotting,
        OpportunityMap,
        TeamAssemble,
        IdeaWorkshop,
        iteration_loop,
        ConceptFinalize,
        CommercialHandoff,
        PerformanceAudit
    ]
)
root.order.add_edge(TrendSpotting, OpportunityMap)
root.order.add_edge(OpportunityMap, TeamAssemble)
root.order.add_edge(TeamAssemble, IdeaWorkshop)
root.order.add_edge(IdeaWorkshop, iteration_loop)
root.order.add_edge(iteration_loop, ConceptFinalize)
root.order.add_edge(ConceptFinalize, CommercialHandoff)
root.order.add_edge(CommercialHandoff, PerformanceAudit)