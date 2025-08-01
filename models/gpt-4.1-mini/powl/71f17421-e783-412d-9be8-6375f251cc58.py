# Generated from: 71f17421-e783-412d-9be8-6375f251cc58.json
# Description: This process details the artisanal cheese supply chain involving small-scale farm production, quality fermentation, aging, and niche market distribution. It starts with milk sourcing from rare breed cows, followed by precise curd formation and hand-pressing techniques. The cheeses undergo microclimate-controlled aging, with periodic manual inspections and flavor profiling. Packaging uses biodegradable materials with custom labeling. The distribution leverages local gourmet shops and direct farmer-to-chef deliveries, requiring coordination with logistics providers for temperature-controlled transport. Feedback loops involve tasting panels and customer surveys to refine future batches, ensuring a consistent premium product that preserves traditional methods while meeting modern sustainability standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities
milk_sourcing = Transition(label='Milk Sourcing')
breed_selection = Transition(label='Breed Selection')
curd_formation = Transition(label='Curd Formation')
hand_pressing = Transition(label='Hand Pressing')
salt_rubbing = Transition(label='Salt Rubbing')
batch_labeling = Transition(label='Batch Labeling')
fermentation_test = Transition(label='Fermentation Test')
microclimate_aging = Transition(label='Microclimate Aging')
manual_inspection = Transition(label='Manual Inspection')
flavor_profiling = Transition(label='Flavor Profiling')
packaging_prep = Transition(label='Packaging Prep')
eco_packaging = Transition(label='Eco Packaging')
logistics_planning = Transition(label='Logistics Planning')
cold_transport = Transition(label='Cold Transport')
retail_delivery = Transition(label='Retail Delivery')
chef_coordination = Transition(label='Chef Coordination')
tasting_panels = Transition(label='Tasting Panels')
customer_survey = Transition(label='Customer Survey')

# Pre-processing steps (farm-related)
preparation = StrictPartialOrder(nodes=[milk_sourcing, breed_selection])
preparation.order.add_edge(milk_sourcing, breed_selection)

# Production steps in partial order (curd formation, hand pressing, salt rubbing)
production = StrictPartialOrder(
    nodes=[curd_formation, hand_pressing, salt_rubbing]
)
production.order.add_edge(curd_formation, hand_pressing)
production.order.add_edge(hand_pressing, salt_rubbing)

# Quality checks during aging: fermentation test before aging
quality_checks = StrictPartialOrder(
    nodes=[fermentation_test, microclimate_aging, manual_inspection, flavor_profiling]
)
quality_checks.order.add_edge(fermentation_test, microclimate_aging)
quality_checks.order.add_edge(microclimate_aging, manual_inspection)
quality_checks.order.add_edge(manual_inspection, flavor_profiling)

# Packaging steps: packaging prep then eco packaging and batch labeling in parallel (partial order)
packaging = StrictPartialOrder(nodes=[packaging_prep, eco_packaging, batch_labeling])
packaging.order.add_edge(packaging_prep, eco_packaging)
packaging.order.add_edge(packaging_prep, batch_labeling)
# eco_packaging and batch_labeling are concurrent (no order between them)

# Distribution steps with partial order: logistics planning then cold transport and chef coordination in parallel,
# then retail delivery
distribution_inner = StrictPartialOrder(nodes=[cold_transport, chef_coordination])
# cold_transport and chef_coordination are concurrent (their interleaving is flexible)
distribution = StrictPartialOrder(
    nodes=[logistics_planning, distribution_inner, retail_delivery]
)
distribution.order.add_edge(logistics_planning, distribution_inner)
distribution.order.add_edge(distribution_inner, retail_delivery)

# Feedback loop body: tasting panels and customer survey in parallel (partial order)
feedback_body = StrictPartialOrder(nodes=[tasting_panels, customer_survey])
# No ordering between tasting panels and customer survey

# Feedback loop: loop(feedback_body, production + quality_checks + packaging + distribution)
# To define the loop we must combine the body of the loop (feedback step) and the "do again" part

# The loop carries the refinement of future batches (production -> quality -> packaging -> distribution),
# so the "B" branch of the loop executes the sequence again.

# The do-again body is the whole process after initial farm prep:
# production -> quality_checks -> packaging -> distribution

# Build the sequential order of production -> quality_checks -> packaging -> distribution
post_prep = StrictPartialOrder(
    nodes=[production, quality_checks, packaging, distribution]
)
post_prep.order.add_edge(production, quality_checks)
post_prep.order.add_edge(quality_checks, packaging)
post_prep.order.add_edge(packaging, distribution)

# The loop node: execute feedback_body, then either exit or execute post_prep then feedback_body again.

loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_body, post_prep])

# The full root is prep (milk sourcing and breed) then production with feedback loop.

root = StrictPartialOrder(nodes=[preparation, loop])
root.order.add_edge(preparation, loop)