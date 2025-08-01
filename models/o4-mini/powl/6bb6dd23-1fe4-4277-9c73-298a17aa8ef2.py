# Generated from: 6bb6dd23-1fe4-4277-9c73-298a17aa8ef2.json
# Description: This process describes the end-to-end flow of sourcing rare, handcrafted materials from remote artisans, verifying authenticity through blockchain certification, coordinating bespoke production schedules with multiple small workshops, and managing bespoke logistics for fragile goods. The process involves collaborative design reviews, custom packaging development, and adaptive marketing strategies tailored to niche collectors, ensuring exclusivity and traceability throughout the supply chain while maintaining sustainability and fair trade practices.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
supplier     = Transition(label='Supplier Onboard')
material     = Transition(label='Material Verify')
auth         = Transition(label='Auth Certify')
order        = Transition(label='Order Schedule')
workshop     = Transition(label='Workshop Align')
design       = Transition(label='Design Review')
sample       = Transition(label='Sample Produce')
inspect      = Transition(label='Quality Inspect')
pack         = Transition(label='Packaging Develop')
logistics    = Transition(label='Logistics Plan')
label_custom = Transition(label='Custom Label')
track        = Transition(label='Shipment Track')
notify       = Transition(label='Customer Notify')
feedback     = Transition(label='Feedback Collect')
sustain      = Transition(label='Sustain Audit')
compliance   = Transition(label='Trade Compliance')

# Loop: iterate sample production and design review until design is approved
loop_review = OperatorPOWL(operator=Operator.LOOP, children=[design, sample])

# Build the partial order: 
# 1) onboarding & verification
# 2) schedule & align workshops
# 3) review/produce loop
# 4) quality inspection
# 5) parallel packaging, logistics, sustainability audit, trade compliance
# 6) synchronization into shipment
# 7) notify customer & collect feedback
root = StrictPartialOrder(nodes=[
    supplier, material, auth, order, workshop,
    loop_review,
    inspect,
    pack, logistics, sustain, compliance,
    label_custom, track, notify, feedback
])

# 1. Onboard → Verify → Certify
root.order.add_edge(supplier, material)
root.order.add_edge(material, auth)

# 2. Schedule → Align
root.order.add_edge(auth, order)
root.order.add_edge(order, workshop)

# 3. Workshops aligned → enter design/produce review loop → then quality inspect
root.order.add_edge(workshop, loop_review)
root.order.add_edge(loop_review, inspect)

# 4. After inspection, branch into four parallel flows
root.order.add_edge(inspect, pack)
root.order.add_edge(inspect, logistics)
root.order.add_edge(inspect, sustain)
root.order.add_edge(inspect, compliance)

# 5. Packaging → labeling → must synchronize with logistics, audit, compliance before shipment
root.order.add_edge(pack, label_custom)
root.order.add_edge(label_custom, track)
root.order.add_edge(logistics, track)
root.order.add_edge(sustain, track)
root.order.add_edge(compliance, track)

# 6. Shipment → notify → feedback
root.order.add_edge(track, notify)
root.order.add_edge(notify, feedback)