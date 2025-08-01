# Generated from: fe65b80d-f315-41b1-b671-103c71030659.json
# Description: This process describes the intricate and atypical workflow involved in creating bespoke artisan perfumes. It includes sourcing rare natural ingredients from multiple continents, testing scent combinations in micro-batches, performing sensory evaluations with expert panels, adapting formulas based on feedback, and finally crafting limited edition bottles. The process also integrates regulatory compliance checks for ingredient safety, sustainable packaging design, and personalized marketing strategies targeted at niche luxury markets, ensuring each perfume is unique and aligned with client preferences and environmental standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
t_sourcing       = Transition(label='Ingredient Sourcing')
t_safety         = Transition(label='Safety Review')
t_sustain        = Transition(label='Sustainability Check')
t_scent          = Transition(label='Scent Blending')
t_batch          = Transition(label='Micro Batch')
t_quality        = Transition(label='Quality Testing')
t_panel          = Transition(label='Sensory Panel')
t_adjust         = Transition(label='Formula Adjust')
t_client         = Transition(label='Client Feedback')
t_packaging      = Transition(label='Packaging Design')
t_prototype      = Transition(label='Prototype Creation')
t_label          = Transition(label='Label Approval')
t_production     = Transition(label='Final Production')
t_marketing      = Transition(label='Marketing Plan')
t_distribution   = Transition(label='Distribution Prep')
t_launch         = Transition(label='Sales Launch')

# Build the loop: (Scent Blending -> Micro Batch -> Quality Testing -> Sensory Panel),
# with Formula Adjust as the rework step
loop_body = StrictPartialOrder(nodes=[t_scent, t_batch, t_quality, t_panel])
loop_body.order.add_edge(t_scent,  t_batch)
loop_body.order.add_edge(t_batch,  t_quality)
loop_body.order.add_edge(t_quality, t_panel)

loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, t_adjust])

# Build the overall workflow as a partial order
root = StrictPartialOrder(nodes=[
    t_sourcing, t_safety, t_sustain,
    loop, t_client,
    t_packaging, t_prototype, t_label, t_production,
    t_marketing, t_distribution, t_launch
])

# Sequence: Ingredient Sourcing -> Safety & Sustainability checks
root.order.add_edge(t_sourcing, t_safety)
root.order.add_edge(t_sourcing, t_sustain)
# After both checks, enter the scent-testing loop
root.order.add_edge(t_safety,  loop)
root.order.add_edge(t_sustain, loop)
# Once loop completes (exit), get client feedback
root.order.add_edge(loop, t_client)
# Then sequential design & approval & production
root.order.add_edge(t_client,    t_packaging)
root.order.add_edge(t_packaging, t_prototype)
root.order.add_edge(t_prototype, t_label)
root.order.add_edge(t_label,     t_production)
# After production, marketing and distribution prep can run in parallel
root.order.add_edge(t_production,   t_marketing)
root.order.add_edge(t_production,   t_distribution)
# Both marketing and distribution must finish before launch
root.order.add_edge(t_marketing,    t_launch)
root.order.add_edge(t_distribution, t_launch)