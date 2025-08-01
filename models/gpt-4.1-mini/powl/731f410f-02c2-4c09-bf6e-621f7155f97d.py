# Generated from: 731f410f-02c2-4c09-bf6e-621f7155f97d.json
# Description: This process involves leveraging a global community to generate, evaluate, and implement innovative ideas for product development. It starts with idea crowdsourcing, followed by filtering through AI-assisted evaluation, community voting, expert refinement, and prototype creation. After field testing with select users, feedback is collected and analyzed to iterate on designs. The process incorporates rapid pivoting based on real-time data, intellectual property assessment, and strategic partnerships to scale successful innovations. Continuous monitoring and knowledge sharing ensure sustained innovation beyond the initial cycle, fostering an adaptive and collaborative environment uncommon in traditional R&D workflows.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
IdeaSourcing = Transition(label='Idea Sourcing')
AIFiltering = Transition(label='AI Filtering')
CommunityVote = Transition(label='Community Vote')
ExpertReview = Transition(label='Expert Review')
ConceptRefining = Transition(label='Concept Refining')
PrototypeBuild = Transition(label='Prototype Build')
FieldTesting = Transition(label='Field Testing')
FeedbackCollect = Transition(label='Feedback Collect')
DataAnalyze = Transition(label='Data Analyze')
DesignIterate = Transition(label='Design Iterate')
PivotDecision = Transition(label='Pivot Decision')
IPAssessment = Transition(label='IP Assessment')
PartnerAlign = Transition(label='Partner Align')
ScaleLaunch = Transition(label='Scale Launch')
KnowledgeShare = Transition(label='Knowledge Share')
MonitorTrends = Transition(label='Monitor Trends')

# Loop: iterate after feedback analysis: loop(DesignIterate, Feedback cycle)
# Feedback cycle: FeedbackCollect -> DataAnalyze -> PivotDecision (X pivot or continue)
# loop body: FeedbackCollect, DataAnalyze, PivotDecision (choice of pivot or continue to iterate)
feedback_cycle = StrictPartialOrder(
    nodes=[FeedbackCollect, DataAnalyze, PivotDecision]
)
feedback_cycle.order.add_edge(FeedbackCollect, DataAnalyze)
feedback_cycle.order.add_edge(DataAnalyze, PivotDecision)

# Loop construct: body=feedback_cycle, redo=DesignIterate
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[DesignIterate, feedback_cycle])

# Main sequence from idea to prototype + testing
main_sequence = StrictPartialOrder(
    nodes=[
        IdeaSourcing,
        AIFiltering,
        CommunityVote,
        ExpertReview,
        ConceptRefining,
        PrototypeBuild,
        FieldTesting,
        feedback_loop
    ]
)

main_sequence.order.add_edge(IdeaSourcing, AIFiltering)
main_sequence.order.add_edge(AIFiltering, CommunityVote)
main_sequence.order.add_edge(CommunityVote, ExpertReview)
main_sequence.order.add_edge(ExpertReview, ConceptRefining)
main_sequence.order.add_edge(ConceptRefining, PrototypeBuild)
main_sequence.order.add_edge(PrototypeBuild, FieldTesting)
main_sequence.order.add_edge(FieldTesting, feedback_loop)

# After pivot decision in feedback_loop we continue with IP assessment, partner alignment,
# scale launch, and monitoring in partial order, with knowledge sharing and monitoring concurrent.

post_feedback = StrictPartialOrder(
    nodes=[
        IPAssessment,
        PartnerAlign,
        ScaleLaunch,
        KnowledgeShare,
        MonitorTrends
    ]
)

# Sequence: IPAssessment -> PartnerAlign -> ScaleLaunch
post_feedback.order.add_edge(IPAssessment, PartnerAlign)
post_feedback.order.add_edge(PartnerAlign, ScaleLaunch)

# KnowledgeShare and MonitorTrends run concurrent with ScaleLaunch
# No order edges needed to express concurrency beyond their predecessors.

# Connect feedback_loop with post_feedback
root = StrictPartialOrder(
    nodes=[main_sequence, post_feedback]
)
root.order.add_edge(main_sequence, post_feedback)