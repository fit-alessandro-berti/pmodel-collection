# Generated from: be0b62e2-82e7-4e22-8b94-36e4c60eb095.json
# Description: This process describes a cyclical approach where multiple industries collaborate to innovate a shared technology platform. It begins with trend spotting in diverse sectors, followed by ideation sessions that mix domain experts. Prototypes are co-developed and tested in controlled pilot environments across industries. Feedback loops involve multi-disciplinary review boards, adapting the product for specific market needs. Parallel regulatory assessments ensure compliance across jurisdictions. After iterative refinement, a joint go-to-market strategy is launched, including synchronized branding and distribution channels. Post-launch monitoring collects cross-sector data to inform the next innovation cycle, fostering sustainable competitive advantage through continuous, collaborative evolution.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Trend_Spotting = Transition(label='Trend Spotting')
Idea_Harvest = Transition(label='Idea Harvest')
Expert_Sync = Transition(label='Expert Sync')
Concept_Sketch = Transition(label='Concept Sketch')
Feasibility_Check = Transition(label='Feasibility Check')
Prototype_Build = Transition(label='Prototype Build')
Pilot_Deploy = Transition(label='Pilot Deploy')
Multisector_Test = Transition(label='Multisector Test')
Compliance_Audit = Transition(label='Compliance Audit')
Review_Board = Transition(label='Review Board')
Market_Adapt = Transition(label='Market Adapt')
Strategy_Plan = Transition(label='Strategy Plan')
Brand_Align = Transition(label='Brand Align')
Launch_Sync = Transition(label='Launch Sync')
Performance_Track = Transition(label='Performance Track')
Feedback_Loop = Transition(label='Feedback Loop')
Cycle_Review = Transition(label='Cycle Review')

# Model the Feedback Loop with Review Board, Market Adapt, and Feedback Loop activities
# They are sequentially ordered, forming the iterative refinement
feedback_seq = StrictPartialOrder(nodes=[Review_Board, Market_Adapt, Feedback_Loop])
feedback_seq.order.add_edge(Review_Board, Market_Adapt)
feedback_seq.order.add_edge(Market_Adapt, Feedback_Loop)

# Parallel regulatory assessments: Compliance Audit is parallel with feedback_seq activities
# We model these as a PO with no edges between Compliance_Audit and feedback_seq nodes => concurrent
regulatory_parallel = StrictPartialOrder(
    nodes=[Compliance_Audit, feedback_seq]
)
# no edges between Compliance_Audit and feedback_seq -> concurrent

# Prototype Build and Pilot Deploy and Multisector Test form a sequence before regulatory parallelism
prototype_seq = StrictPartialOrder(nodes=[Prototype_Build, Pilot_Deploy, Multisector_Test])
prototype_seq.order.add_edge(Prototype_Build, Pilot_Deploy)
prototype_seq.order.add_edge(Pilot_Deploy, Multisector_Test)

# Concept Sketch and Feasibility Check sequence before Prototype Build
concept_seq = StrictPartialOrder(nodes=[Concept_Sketch, Feasibility_Check])
concept_seq.order.add_edge(Concept_Sketch, Feasibility_Check)

# Ideation session mixing domain experts: Idea Harvest and Expert Sync can be concurrent
ideation_parallel = StrictPartialOrder(nodes=[Idea_Harvest, Expert_Sync])
# no edges -> concurrent

# Trend Spotting leads to ideation_parallel
trend_to_ideation = StrictPartialOrder(nodes=[Trend_Spotting, ideation_parallel])
trend_to_ideation.order.add_edge(Trend_Spotting, ideation_parallel)

# Ideation leads to Concept and Feasibility check
ideation_to_concept = StrictPartialOrder(nodes=[ideation_parallel, concept_seq])
ideation_to_concept.order.add_edge(ideation_parallel, concept_seq)

# Concept seq leads to prototype seq
concept_to_prototype = StrictPartialOrder(nodes=[concept_seq, prototype_seq])
concept_to_prototype.order.add_edge(concept_seq, prototype_seq)

# After prototype seq, regulatory parallel (Compliance audit + feedback_seq)
prototype_to_parallel = StrictPartialOrder(nodes=[prototype_seq, regulatory_parallel])
prototype_to_parallel.order.add_edge(prototype_seq, regulatory_parallel)

# After regulatory parallel, Strategy Plan sequence
strategy_seq = StrictPartialOrder(nodes=[Strategy_Plan, Brand_Align, Launch_Sync])
strategy_seq.order.add_edge(Strategy_Plan, Brand_Align)
strategy_seq.order.add_edge(Brand_Align, Launch_Sync)

# Then Performance Track, Cycle Review follow sequentially
post_launch_seq = StrictPartialOrder(nodes=[Performance_Track, Cycle_Review])
post_launch_seq.order.add_edge(Performance_Track, Cycle_Review)

# Strategy seq leads to post_launch seq
strategy_to_post = StrictPartialOrder(nodes=[strategy_seq, post_launch_seq])
strategy_to_post.order.add_edge(strategy_seq, post_launch_seq)

# The whole forward flow up to post-launch: 
# trend_to_ideation -> ideation_to_concept -> concept_to_prototype -> prototype_to_parallel -> strategy_to_post
first_part = StrictPartialOrder(
    nodes=[trend_to_ideation, ideation_to_concept]
)
first_part.order.add_edge(trend_to_ideation, ideation_to_concept)

second_part = StrictPartialOrder(
    nodes=[first_part, concept_to_prototype]
)
second_part.order.add_edge(first_part, concept_to_prototype)

third_part = StrictPartialOrder(
    nodes=[second_part, prototype_to_parallel]
)
third_part.order.add_edge(second_part, prototype_to_parallel)

fourth_part = StrictPartialOrder(
    nodes=[third_part, strategy_to_post]
)
fourth_part.order.add_edge(third_part, strategy_to_post)

# Loop structure:
# After cycle review (Cycle_Review), loop back to Trend_Spotting as the next innovation cycle
# Model loop with LOOP operator:
# LOOP(body=A, redo=B) where:
# A = full forward process from Trend_Spotting to Cycle_Review
# B = silent transition + optional (we can consider the silent transition representing the decision to redo iteration)
# but to avoid complexity, just loop body is the whole process and redo their feedback/adjustment
# We use silent transition to decide to either exit or redo.

# The loop structure is: 
# Execute the whole process (fourth_part), then choose to exit or redo (cycle repeats)

skip = SilentTransition()  # to model exit from the loop

loop_body = fourth_part

# Loop child 1: body (full process)
# Loop child 2: redo (feedback and cycle)
# Our process has integrated feedback loops inside, so redo is effectively another iteration of the whole

root = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, skip])