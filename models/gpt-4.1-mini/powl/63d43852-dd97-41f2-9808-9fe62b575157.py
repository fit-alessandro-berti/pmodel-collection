# Generated from: 63d43852-dd97-41f2-9808-9fe62b575157.json
# Description: This process outlines the cross-industry innovation cycle where ideas are sourced externally from unrelated sectors, filtered through multi-disciplinary teams, and then prototyped using adaptive methodologies. The process integrates continuous feedback loops from diverse stakeholders, including suppliers, customers, and regulatory bodies. It incorporates risk evaluation based on emerging trends and leverages collaborative digital platforms for knowledge sharing. The cycle culminates in scalable pilot projects before final market integration, ensuring adaptability and compliance across multiple domains while fostering sustainable competitive advantages through unconventional partnerships and resource utilization.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
IdeaSourcing = Transition(label='Idea Sourcing')
TrendScanning = Transition(label='Trend Scanning')
CrossCheck = Transition(label='Cross-Check')
FeasibilityStudy = Transition(label='Feasibility Study')
RiskAssess = Transition(label='Risk Assess')
StakeholderMap = Transition(label='Stakeholder Map')
ConceptDesign = Transition(label='Concept Design')
PrototypeBuild = Transition(label='Prototype Build')
FeedbackLoop = Transition(label='Feedback Loop')
PartnerAlign = Transition(label='Partner Align')
ResourceAllocate = Transition(label='Resource Allocate')
PilotLaunch = Transition(label='Pilot Launch')
PerformanceReview = Transition(label='Performance Review')
ComplianceCheck = Transition(label='Compliance Check')
MarketIntegrate = Transition(label='Market Integrate')
KnowledgeShare = Transition(label='Knowledge Share')
ScaleStrategy = Transition(label='Scale Strategy')

# Construct partial orders reflecting the process and parallelisms

# Phase 1: Idea Sourcing and Trend Scanning parallel activities then Cross-Check
phase1_PO = StrictPartialOrder(
    nodes=[IdeaSourcing, TrendScanning, CrossCheck]
)
phase1_PO.order.add_edge(IdeaSourcing, CrossCheck)
phase1_PO.order.add_edge(TrendScanning, CrossCheck)

# Phase 2: Feasibility Study after Cross-Check
phase2_PO = StrictPartialOrder(
    nodes=[CrossCheck, FeasibilityStudy]
)
phase2_PO.order.add_edge(CrossCheck, FeasibilityStudy)

# Phase 3: Risk Assess and Stakeholder Map in parallel before Concept Design
phase3_PO = StrictPartialOrder(
    nodes=[FeasibilityStudy, RiskAssess, StakeholderMap, ConceptDesign]
)
phase3_PO.order.add_edge(FeasibilityStudy, RiskAssess)
phase3_PO.order.add_edge(FeasibilityStudy, StakeholderMap)
phase3_PO.order.add_edge(RiskAssess, ConceptDesign)
phase3_PO.order.add_edge(StakeholderMap, ConceptDesign)

# Phase 4: Concept Design then Prototype Build
phase4_PO = StrictPartialOrder(
    nodes=[ConceptDesign, PrototypeBuild]
)
phase4_PO.order.add_edge(ConceptDesign, PrototypeBuild)

# Loop: Prototype Build followed by Feedback Loop and Partner Align, Resource Allocate in parallel
# Feedback Loop loops back to Prototype Build, modeling continuous improvement
feedback_branch_PO = StrictPartialOrder(
    nodes=[FeedbackLoop, PartnerAlign, ResourceAllocate]
)
feedback_branch_PO.order.add_edge(FeedbackLoop, PartnerAlign)
feedback_branch_PO.order.add_edge(FeedbackLoop, ResourceAllocate)

# Loop operator: First child A is Prototype Build, second child B is the parallel feedback_branch_PO
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[PrototypeBuild, feedback_branch_PO])

# Phase 5: After loop, Pilot Launch then Performance Review and Compliance Check in parallel
phase5_PO = StrictPartialOrder(
    nodes=[loop_feedback, PilotLaunch, PerformanceReview, ComplianceCheck]
)
phase5_PO.order.add_edge(loop_feedback, PilotLaunch)
phase5_PO.order.add_edge(PilotLaunch, PerformanceReview)
phase5_PO.order.add_edge(PilotLaunch, ComplianceCheck)

# Phase 6: Market Integrate after performance and compliance checks
phase6_PO = StrictPartialOrder(
    nodes=[PerformanceReview, ComplianceCheck, MarketIntegrate]
)
phase6_PO.order.add_edge(PerformanceReview, MarketIntegrate)
phase6_PO.order.add_edge(ComplianceCheck, MarketIntegrate)

# Phase 7: Knowledge Share and Scale Strategy after Market Integrate in parallel
phase7_PO = StrictPartialOrder(
    nodes=[MarketIntegrate, KnowledgeShare, ScaleStrategy]
)
phase7_PO.order.add_edge(MarketIntegrate, KnowledgeShare)
phase7_PO.order.add_edge(MarketIntegrate, ScaleStrategy)

# Merge all phases into one big PO
root = StrictPartialOrder(
    nodes=[
        IdeaSourcing, TrendScanning, CrossCheck, FeasibilityStudy, RiskAssess, StakeholderMap,
        ConceptDesign, loop_feedback, PilotLaunch, PerformanceReview, ComplianceCheck, MarketIntegrate,
        KnowledgeShare, ScaleStrategy, PartnerAlign, ResourceAllocate, FeedbackLoop, PrototypeBuild
    ]
)

# Add edges representing all order relations

# Phase 1 edges
root.order.add_edge(IdeaSourcing, CrossCheck)
root.order.add_edge(TrendScanning, CrossCheck)

# Phase 2 edges
root.order.add_edge(CrossCheck, FeasibilityStudy)

# Phase 3 edges
root.order.add_edge(FeasibilityStudy, RiskAssess)
root.order.add_edge(FeasibilityStudy, StakeholderMap)
root.order.add_edge(RiskAssess, ConceptDesign)
root.order.add_edge(StakeholderMap, ConceptDesign)

# Phase 4 edges
root.order.add_edge(ConceptDesign, PrototypeBuild)

# Loop edges:
# LOOP structure added above: Children are [PrototypeBuild, feedback_branch_PO]
# feedback_branch_PO order edges:
root.order.add_edge(FeedbackLoop, PartnerAlign)
root.order.add_edge(FeedbackLoop, ResourceAllocate)
# Loop semantics will be understood by OperatorPOWL class on execution

# Phase 5 edges
root.order.add_edge(loop_feedback, PilotLaunch)
root.order.add_edge(PilotLaunch, PerformanceReview)
root.order.add_edge(PilotLaunch, ComplianceCheck)

# Phase 6 edges
root.order.add_edge(PerformanceReview, MarketIntegrate)
root.order.add_edge(ComplianceCheck, MarketIntegrate)

# Phase 7 edges
root.order.add_edge(MarketIntegrate, KnowledgeShare)
root.order.add_edge(MarketIntegrate, ScaleStrategy)