# Generated from: fe65b80d-f315-41b1-b671-103c71030659.json
# Description: This process describes the intricate and atypical workflow involved in creating bespoke artisan perfumes. It includes sourcing rare natural ingredients from multiple continents, testing scent combinations in micro-batches, performing sensory evaluations with expert panels, adapting formulas based on feedback, and finally crafting limited edition bottles. The process also integrates regulatory compliance checks for ingredient safety, sustainable packaging design, and personalized marketing strategies targeted at niche luxury markets, ensuring each perfume is unique and aligned with client preferences and environmental standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
ingredient_sourcing = Transition(label='Ingredient Sourcing')
quality_testing = Transition(label='Quality Testing')
scent_blending = Transition(label='Scent Blending')
micro_batch = Transition(label='Micro Batch')
sensory_panel = Transition(label='Sensory Panel')
formula_adjust = Transition(label='Formula Adjust')
safety_review = Transition(label='Safety Review')
sustainability_check = Transition(label='Sustainability Check')
packaging_design = Transition(label='Packaging Design')
prototype_creation = Transition(label='Prototype Creation')
client_feedback = Transition(label='Client Feedback')
label_approval = Transition(label='Label Approval')
final_production = Transition(label='Final Production')
marketing_plan = Transition(label='Marketing Plan')
distribution_prep = Transition(label='Distribution Prep')
sales_launch = Transition(label='Sales Launch')

# Create the loop for iterative adjustment after sensory panel feedback
# Loop structure:  
# A = Formula Adjust 
# B = Client Feedback + Sensory Panel (partial order)
client_sensory = StrictPartialOrder(nodes=[client_feedback, sensory_panel])
client_sensory.order.add_edge(client_feedback, sensory_panel)  # client feedback before sensory panel
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[formula_adjust, client_sensory])

# Partial order for scent blending and micro batch which are concurrent steps after ingredient sourcing and quality testing
blending_and_microbatch = StrictPartialOrder(nodes=[scent_blending, micro_batch])
# No order edges -> concurrent

# Safety Review and Sustainability Check happen after Quality Testing, can be concurrent
safety_sustainability = StrictPartialOrder(nodes=[safety_review, sustainability_check])
# No order edges -> concurrent

# Packaging Design depends on Sustainability Check
# Prototype Creation depends on Packaging Design
packaging_and_proto = StrictPartialOrder(nodes=[packaging_design, prototype_creation])
packaging_and_proto.order.add_edge(packaging_design, prototype_creation)

# Label Approval depends on Prototype Creation and Safety Review
label_approval_po = StrictPartialOrder(nodes=[label_approval, prototype_creation, safety_review])
label_approval_po.order.add_edge(prototype_creation, label_approval)
label_approval_po.order.add_edge(safety_review, label_approval)

# After Label Approval, Final Production happens
final_prod_po = StrictPartialOrder(nodes=[final_production, label_approval])
final_prod_po.order.add_edge(label_approval, final_production)

# Marketing Plan and Distribution Prep can run concurrently after Final Production
marketing_and_distribution = StrictPartialOrder(nodes=[marketing_plan, distribution_prep])
# No order edges -> concurrent

# Sales Launch depends on Marketing Plan and Distribution Prep
sales_launch_po = StrictPartialOrder(nodes=[sales_launch, marketing_plan, distribution_prep])
sales_launch_po.order.add_edge(marketing_plan, sales_launch)
sales_launch_po.order.add_edge(distribution_prep, sales_launch)

# Compose the main partial order
root = StrictPartialOrder(
    nodes=[
        ingredient_sourcing,
        quality_testing,
        blending_and_microbatch,
        feedback_loop,
        sensory_panel,  # note sensory_panel included in client_sensory already, no need to add here separately
        safety_sustainability,
        packaging_and_proto,
        label_approval_po,
        final_prod_po,
        marketing_and_distribution,
        sales_launch_po
    ]
)

# Add edges defining the control flow order

# Ingredient Sourcing -> Quality Testing
root.order.add_edge(ingredient_sourcing, quality_testing)

# Quality Testing -> (Scent Blending || Micro Batch)
root.order.add_edge(quality_testing, blending_and_microbatch)

# After blending and micro batch -> Sensory Panel (but sensory_panel is inside the loop, so we link blending_and_microbatch to feedback_loop root for trigger)
root.order.add_edge(blending_and_microbatch, feedback_loop)

# Feedback loop contains formula_adjust and client_feedback -> sensory_panel happens inside loop, no extra edges needed here.

# Sensory Panel completion enables safety and sustainability checks
root.order.add_edge(feedback_loop, safety_sustainability)

# Safety and sustainability -> Packaging Design and Prototype Creation (packaging_and_proto)
root.order.add_edge(safety_sustainability, packaging_and_proto)

# Packaging and Prototype Creation -> Label Approval
root.order.add_edge(packaging_and_proto, label_approval_po)

# Label Approval -> Final Production
root.order.add_edge(label_approval_po, final_prod_po)

# Final Production -> Marketing and Distribution prep
root.order.add_edge(final_prod_po, marketing_and_distribution)

# Marketing and Distribution -> Sales Launch
root.order.add_edge(marketing_and_distribution, sales_launch_po)