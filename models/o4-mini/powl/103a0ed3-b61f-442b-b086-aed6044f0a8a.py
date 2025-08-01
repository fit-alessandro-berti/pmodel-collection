# Generated from: 103a0ed3-b61f-442b-b086-aed6044f0a8a.json
# Description: This process involves the intricate steps of crafting bespoke perfumes using rare and natural ingredients sourced globally. It begins with ingredient selection and testing, followed by precise blending and maturation phases. The process includes sensory evaluations, iterative reformulations based on feedback, and finally, bespoke packaging tailored to client preferences. This atypical process blends art, chemistry, and logistics, requiring coordination between botanists, chemists, and designers to ensure each perfume is unique and meets high-quality standards. The entire workflow emphasizes sustainability and exclusivity, making it suitable for luxury niche markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
ing             = Transition(label="Ingredient Sourcing")
sample_test     = Transition(label="Sample Testing")
blend_creation  = Transition(label="Blend Creation")
initial_mat     = Transition(label="Initial Maturation")
sensory_review  = Transition(label="Sensory Review")
formula_adjust  = Transition(label="Formula Adjust")
secondary_mat   = Transition(label="Secondary Maturation")
quality_check   = Transition(label="Quality Check")
client_feedback = Transition(label="Client Feedback")
final_adjust    = Transition(label="Final Adjust")
bottle_design   = Transition(label="Bottle Design")
label_printing  = Transition(label="Label Printing")
pack_prep       = Transition(label="Packaging Prep")
custom_assembly = Transition(label="Custom Assembly")
dispatch_arr    = Transition(label="Dispatch Arrange")

# Silent skip for optional branches
skip = SilentTransition()

# Loop body: Formula Adjust -> Secondary Maturation
loop_body = StrictPartialOrder(
    nodes=[formula_adjust, secondary_mat]
)
loop_body.order.add_edge(formula_adjust, secondary_mat)

# LOOP: Sensory Review, then either exit or perform (Formula Adjust -> Secondary Maturation) then back
perfume_refine_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[sensory_review, loop_body]
)

# XOR for optional final adjustment after client feedback
fb_xor = OperatorPOWL(
    operator=Operator.XOR,
    children=[skip, final_adjust]
)

# Packaging subprocess:
#   Bottle Design and Label Printing in parallel,
#   then Packaging Prep, Custom Assembly, Dispatch Arrange in sequence
packaging_po = StrictPartialOrder(
    nodes=[bottle_design, label_printing, pack_prep, custom_assembly, dispatch_arr]
)
# parallel constraints
packaging_po.order.add_edge(bottle_design, pack_prep)
packaging_po.order.add_edge(label_printing, pack_prep)
# sequential constraints
packaging_po.order.add_edge(pack_prep, custom_assembly)
packaging_po.order.add_edge(custom_assembly, dispatch_arr)

# Root partial order stitching everything together
root = StrictPartialOrder(
    nodes=[
        ing,
        sample_test,
        blend_creation,
        initial_mat,
        perfume_refine_loop,
        quality_check,
        client_feedback,
        fb_xor,
        packaging_po
    ]
)

# Sequential flow edges
root.order.add_edge(ing, sample_test)
root.order.add_edge(sample_test, blend_creation)
root.order.add_edge(blend_creation, initial_mat)
root.order.add_edge(initial_mat, perfume_refine_loop)
root.order.add_edge(perfume_refine_loop, quality_check)
root.order.add_edge(quality_check, client_feedback)
root.order.add_edge(client_feedback, fb_xor)
root.order.add_edge(fb_xor, packaging_po)