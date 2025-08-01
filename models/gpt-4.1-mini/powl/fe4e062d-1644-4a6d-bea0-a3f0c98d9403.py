# Generated from: fe4e062d-1644-4a6d-bea0-a3f0c98d9403.json
# Description: This process involves the intricate creation of custom artisan perfumes tailored to individual client preferences. Starting from scent profiling, raw ingredient sourcing, and quality assessment, it moves through experimental blending, maturation cycles, and sensory evaluation by expert panels. The process incorporates iterative refinement and stability testing to ensure product consistency. Packaging design and limited edition batch coordination add exclusivity, while compliance checks and market feedback loops optimize the final offering. This atypical process merges creativity, chemistry, and customer collaboration to deliver unique fragrance experiences.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Client_Profiling = Transition(label='Client Profiling')
Ingredient_Sourcing = Transition(label='Ingredient Sourcing')
Quality_Check = Transition(label='Quality Check')
Blend_Experiment = Transition(label='Blend Experiment')
Maturation_Cycle = Transition(label='Maturation Cycle')
Sensory_Panel = Transition(label='Sensory Panel')
Refinement_Loop = Transition(label='Refinement Loop')
Stability_Test = Transition(label='Stability Test')
Packaging_Design = Transition(label='Packaging Design')
Batch_Coordination = Transition(label='Batch Coordination')
Compliance_Audit = Transition(label='Compliance Audit')
Market_Survey = Transition(label='Market Survey')
Feedback_Review = Transition(label='Feedback Review')
Order_Finalize = Transition(label='Order Finalize')
Distribution_Plan = Transition(label='Distribution Plan')
Inventory_Update = Transition(label='Inventory Update')

# The process description indicates:

# 1) Start with Client Profiling -> Ingredient Sourcing -> Quality Check (linear)
# 2) Then Blend Experiment -> Maturation Cycle -> Sensory Panel (linear)
# 3) Refinement and stability testing is iterative:
#    Refinement Loop and Stability Test form a loop on Blend Experiment and Maturation Cycle area.
#    We consider Refinement Loop as the looping condition after Sensory Panel.
#    Model the loop as (Sensory Panel, Refinement Loop + Stability Test)
#    Loop body: Refinement Loop followed by Stability Test then back to Blend Experiment and Maturation Cycle

# But since Refinement_Loop is an activity, we put it in the loop body.

# Let's model the loop separately to capture the refinement/testing iteration:

# Loop model:
# First child A: Sensory_Panel
# Second child B: StrictPartialOrder with Refinement_Loop and Stability_Test in parallel maybe?
# But refinement likely precedes stability test
# Let's sequence Refinement_Loop --> Stability_Test

refine_and_stability = StrictPartialOrder(nodes=[Refinement_Loop, Stability_Test])
refine_and_stability.order.add_edge(Refinement_Loop, Stability_Test)

loop_refinement = OperatorPOWL(operator=Operator.LOOP, children=[Sensory_Panel, refine_and_stability])

# Full initial sequence including loop:
# Client Profiling --> Ingredient Sourcing --> Quality Check --> Blend Experiment --> Maturation Cycle --> loop_refinement

initial_sequence_nodes = [
    Client_Profiling,
    Ingredient_Sourcing,
    Quality_Check,
    Blend_Experiment,
    Maturation_Cycle,
    loop_refinement,
]

initial_sequence = StrictPartialOrder(nodes=initial_sequence_nodes)

initial_sequence.order.add_edge(Client_Profiling, Ingredient_Sourcing)
initial_sequence.order.add_edge(Ingredient_Sourcing, Quality_Check)
initial_sequence.order.add_edge(Quality_Check, Blend_Experiment)
initial_sequence.order.add_edge(Blend_Experiment, Maturation_Cycle)
initial_sequence.order.add_edge(Maturation_Cycle, loop_refinement)

# After loop_refinement, the process continues with:

# Packaging Design and Batch Coordination add exclusivity
# They can be concurrent after the loop, likely (packaging and batch coordination)
packaging_and_batch = StrictPartialOrder(nodes=[Packaging_Design, Batch_Coordination])
# no order edges => concurrent

# Compliance Audit and Market Feedback loops optimize final offering
# Market feedback includes Market Survey and Feedback Review (sequential)

market_feedback = StrictPartialOrder(nodes=[Market_Survey, Feedback_Review])
market_feedback.order.add_edge(Market_Survey, Feedback_Review)

# Compliance Audit occurs likely before or concurrent with market feedback
# For safety put Compliance Audit concurrent with market_feedback

compliance_and_feedback = StrictPartialOrder(
    nodes=[Compliance_Audit, market_feedback]
)
# no order edges => Compliance Audit concurrent with market feedback order inside market_feedback itself

# After these, final activities:
# Order Finalize -> Distribution Plan -> Inventory Update (linear)

finalization_sequence = StrictPartialOrder(
    nodes=[Order_Finalize, Distribution_Plan, Inventory_Update]
)
finalization_sequence.order.add_edge(Order_Finalize, Distribution_Plan)
finalization_sequence.order.add_edge(Distribution_Plan, Inventory_Update)

# Now combine packaging_and_batch and compliance_and_feedback in parallel, then all before finalization_sequence

# Combine packaging_and_batch and compliance_and_feedback in a StrictPartialOrder where they are concurrent

post_loop_parallel = StrictPartialOrder(
    nodes=[packaging_and_batch, compliance_and_feedback]
)
# no order edges => concurrent

# Connect initial_sequence --> post_loop_parallel --> finalization_sequence:

root = StrictPartialOrder(
    nodes=[initial_sequence, post_loop_parallel, finalization_sequence]
)
root.order.add_edge(initial_sequence, post_loop_parallel)
root.order.add_edge(post_loop_parallel, finalization_sequence)