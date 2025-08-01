# Generated from: 25709a84-1e3f-42fd-aea0-c5f61beabd29.json
# Description: This process outlines the workflow for managing bespoke art commissions from initial client inquiry through to final delivery and post-sale support. It includes client consultation, concept development, iterative feedback cycles, material sourcing, creation phases, quality assurance, and coordinating logistics with specialized packaging and shipping. Additionally, it covers the management of intellectual property rights, final invoicing, and securing client testimonials to support future commissions. The process ensures transparency, client satisfaction, and efficient turnaround times for unique, high-value art pieces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities
ci = Transition(label="Client Inquiry")
ib = Transition(label="Initial Brief")
cd = Transition(label="Concept Draft")
fb = Transition(label="Feedback Loop")
ms = Transition(label="Material Sourcing")
ws = Transition(label="Work Scheduling")
pr = Transition(label="Prototype Review")
ac = Transition(label="Art Creation")
dp = Transition(label="Detailing Phase")
qc = Transition(label="Quality Check")
pp = Transition(label="Packaging Prep")
ss = Transition(label="Shipping Setup")
ipa = Transition(label="IP Agreement")
fi = Transition(label="Final Invoice")
cf = Transition(label="Client Followup")
tr = Transition(label="Testimonial Request")

# Build the feedback loop: first Concept Draft, then choose to exit or go through Feedback Loop and back
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[cd, fb])

# Collect all nodes
nodes = [
    ci, ib, feedback_loop,
    ms, ws, pr, ac, dp, qc, pp, ss, ipa, fi, cf, tr
]

# Create the root partial order
root = StrictPartialOrder(nodes=nodes)

# Sequencing edges
root.order.add_edge(ci, ib)
root.order.add_edge(ib, feedback_loop)

# After the feedback loop, Material Sourcing and Work Scheduling can proceed in parallel
root.order.add_edge(feedback_loop, ms)
root.order.add_edge(feedback_loop, ws)

# Both must complete before Prototype Review
root.order.add_edge(ms, pr)
root.order.add_edge(ws, pr)

# Then linear sequence through creation, detailing, quality, packaging, shipping
root.order.add_edge(pr, ac)
root.order.add_edge(ac, dp)
root.order.add_edge(dp, qc)
root.order.add_edge(qc, pp)
root.order.add_edge(pp, ss)

# After shipping: manage IP and finalize invoicing
root.order.add_edge(ss, ipa)
root.order.add_edge(ss, fi)
root.order.add_edge(ipa, fi)

# Post-sale follow-up and testimonial request
root.order.add_edge(fi, cf)
root.order.add_edge(cf, tr)