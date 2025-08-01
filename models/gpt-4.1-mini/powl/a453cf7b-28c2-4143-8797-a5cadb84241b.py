# Generated from: a453cf7b-28c2-4143-8797-a5cadb84241b.json
# Description: This process involves the meticulous crafting of bespoke artisanal perfumes, combining traditional techniques with modern sensory analysis. Starting from raw botanical sourcing, the process moves through extraction, blending, maturation, and iterative scent testing. Each batch undergoes quality validation and customer profiling to tailor unique fragrance profiles. Packaging incorporates sustainable materials, followed by marketing strategy alignment and distribution to select boutiques. Post-launch feedback collection ensures continuous refinement of formulas, maintaining exclusivity and brand heritage in a niche luxury market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
Botanical_Sourcing = Transition(label='Botanical Sourcing')
Extract_Oils = Transition(label='Extract Oils')
Blend_Scents = Transition(label='Blend Scents')
Mature_Blend = Transition(label='Mature Blend')
Scent_Testing = Transition(label='Scent Testing')
Quality_Check = Transition(label='Quality Check')
Profile_Customer = Transition(label='Profile Customer')
Adjust_Formula = Transition(label='Adjust Formula')
Design_Bottle = Transition(label='Design Bottle')
Select_Packaging = Transition(label='Select Packaging')
Print_Labels = Transition(label='Print Labels')
Market_Strategy = Transition(label='Market Strategy')
Distribute_Stock = Transition(label='Distribute Stock')
Collect_Feedback = Transition(label='Collect Feedback')
Refine_Formula = Transition(label='Refine Formula')
Launch_Campaign = Transition(label='Launch Campaign')

# Loop for iterative scent testing and adjusting formula:
# Loop body: Scent_Testing then Quality_Check then Profile_Customer then adjust formula then repeat
# The loop execute A then choose exit or execute B then A again:
# Let A = Quality_Check --> Profile_Customer (partial order)
# Let B = Adjust_Formula
# Outer loop is: Scent_Testing then LOOP(Quality_Profile, Adjust_Formula)

# Define partial order Quality_Profile = Quality_Check-->Profile_Customer
Quality_Profile = StrictPartialOrder(nodes=[Quality_Check, Profile_Customer])
Quality_Profile.order.add_edge(Quality_Check, Profile_Customer)

# Construct loop node: LOOP(Quality_Profile, Adjust_Formula)
loop = OperatorPOWL(operator=Operator.LOOP, children=[Quality_Profile, Adjust_Formula])

# Partial order for raw material processing: Botanical_Sourcing --> Extract_Oils --> Blend_Scents --> Mature_Blend
raw_mat_po = StrictPartialOrder(nodes=[Botanical_Sourcing, Extract_Oils, Blend_Scents, Mature_Blend])
raw_mat_po.order.add_edge(Botanical_Sourcing, Extract_Oils)
raw_mat_po.order.add_edge(Extract_Oils, Blend_Scents)
raw_mat_po.order.add_edge(Blend_Scents, Mature_Blend)

# After maturation, Scent_Testing happens, followed by loop
raw_mat_and_testing = StrictPartialOrder(nodes=[raw_mat_po, Scent_Testing, loop])
raw_mat_and_testing.order.add_edge(raw_mat_po, Scent_Testing)
raw_mat_and_testing.order.add_edge(Scent_Testing, loop)

# Packaging steps: Design_Bottle --> Select_Packaging --> Print_Labels
packaging_po = StrictPartialOrder(nodes=[Design_Bottle, Select_Packaging, Print_Labels])
packaging_po.order.add_edge(Design_Bottle, Select_Packaging)
packaging_po.order.add_edge(Select_Packaging, Print_Labels)

# Marketing and distribution partial order: Market_Strategy --> Launch_Campaign --> Distribute_Stock
marketing_po = StrictPartialOrder(nodes=[Market_Strategy, Launch_Campaign, Distribute_Stock])
marketing_po.order.add_edge(Market_Strategy, Launch_Campaign)
marketing_po.order.add_edge(Launch_Campaign, Distribute_Stock)

# Post-launch refinement loop: Collect_Feedback --> Refine_Formula (loop back to Collect_Feedback)
# Model with a loop: LOOP(Collect_Feedback, Refine_Formula)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Collect_Feedback, Refine_Formula])

# Combine packaging, marketing, distribution, and feedback loop partial orders into a partial order
# Packaging --> Marketing (assumption: packaging finishes before marketing)
post_process = StrictPartialOrder(nodes=[packaging_po, marketing_po, feedback_loop])
post_process.order.add_edge(packaging_po, marketing_po)

# Finally chain: raw_mat_and_testing --> post_process
root = StrictPartialOrder(nodes=[raw_mat_and_testing, post_process])
root.order.add_edge(raw_mat_and_testing, post_process)