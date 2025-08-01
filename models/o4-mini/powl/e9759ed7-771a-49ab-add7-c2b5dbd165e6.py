# Generated from: e9759ed7-771a-49ab-add7-c2b5dbd165e6.json
# Description: This process details the intricate steps involved in creating a bespoke artisanal perfume, starting from sourcing rare natural ingredients globally, through careful extraction and blending techniques, to aging and final packaging. The workflow requires coordination between botanists, chemists, and marketing teams to ensure the scent's uniqueness, quality, and market appeal. It includes testing for allergen compliance, custom bottle design, and limited edition release scheduling, making it a complex, multi-disciplinary process that balances creativity with regulatory and commercial considerations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ing_src    = Transition(label='Ingredient Sourcing')
oil_ext    = Transition(label='Oil Extraction')
blend      = Transition(label='Blend Formulation')
allergen   = Transition(label='Allergen Check')
batch      = Transition(label='Batch Mixing')
aging      = Transition(label='Aging Process')
sample     = Transition(label='Sample Testing')
reg_review = Transition(label='Regulatory Review')
qc         = Transition(label='Quality Control')
scent      = Transition(label='Scent Profiling')
client_fb  = Transition(label='Client Feedback')
market     = Transition(label='Market Research')
bottle     = Transition(label='Bottle Design')
label_app  = Transition(label='Label Approval')
pack_setup = Transition(label='Packaging Setup')
sales      = Transition(label='Sales Training')
release    = Transition(label='Release Scheduling')

# Silent transition for optional client feedback skip
skip = SilentTransition()

# Loop: repeat blend formulation and allergen check until compliance
loop_allergen = OperatorPOWL(
    operator=Operator.LOOP,
    children=[blend, allergen]
)

# After scent profiling, optionally get client feedback
xor_feedback = OperatorPOWL(
    operator=Operator.XOR,
    children=[client_fb, skip]
)

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    ing_src, oil_ext,                # sourcing & extraction
    loop_allergen,                   # iterative formulation & allergen check
    batch, aging, sample,            # mixing, aging, testing
    reg_review, qc, scent,           # review & quality control & profiling
    xor_feedback,                    # optional client feedback
    market, bottle, label_app,       # marketing path
    pack_setup, sales, release       # final packaging, training, release
])

# Define the control‐flow dependencies
root.order.add_edge(ing_src, oil_ext)
root.order.add_edge(oil_ext, loop_allergen)
root.order.add_edge(loop_allergen, batch)
root.order.add_edge(batch, aging)
root.order.add_edge(aging, sample)
root.order.add_edge(sample, reg_review)
root.order.add_edge(reg_review, qc)
root.order.add_edge(qc, scent)
root.order.add_edge(scent, xor_feedback)

# Marketing branch starts after ingredient sourcing
root.order.add_edge(ing_src, market)
root.order.add_edge(market, bottle)
root.order.add_edge(bottle, label_app)

# Packaging requires label approval, quality control, and (optional) feedback
root.order.add_edge(label_app, pack_setup)
root.order.add_edge(qc, pack_setup)
root.order.add_edge(xor_feedback, pack_setup)

# Final steps
root.order.add_edge(pack_setup, sales)
root.order.add_edge(sales, release)