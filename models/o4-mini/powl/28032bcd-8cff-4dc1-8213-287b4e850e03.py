# Generated from: 28032bcd-8cff-4dc1-8213-287b4e850e03.json
# Description: This process details the end-to-end workflow of exporting artisanal cheese from small-scale farms to international gourmet markets. It involves curating unique cheese varieties, obtaining health certifications, managing cold chain logistics, coordinating with customs brokers, and ensuring compliance with varying import regulations across countries. The process also includes marketing strategies tailored to niche markets, packaging design to maintain freshness and brand identity, and post-delivery feedback collection to continuously improve product quality and customer satisfaction. Special attention is given to traceability and sustainability certifications to meet modern consumer expectations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
fs = Transition(label="Farm Selection")
mt = Transition(label="Milk Testing")
aging = Transition(label="Cheese Aging")
qc = Transition(label="Quality Check")
health = Transition(label="Health Certify")
pd = Transition(label="Packaging Design")
la = Transition(label="Label Approval")
cs = Transition(label="Cold Storage")
tb = Transition(label="Transport Booking")
cf = Transition(label="Customs Filing")
en = Transition(label="Export Negotiation")
mr = Transition(label="Market Research")
op = Transition(label="Order Processing")
co = Transition(label="Customer Outreach")
fr = Transition(label="Feedback Review")
sa = Transition(label="Sustainability Audit")

# Loop for quality check → optionally re-age cheese until pass
quality_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[qc, aging]
)

# Loop for packaging design → optionally re-do label approval until accepted
packaging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[pd, la]
)

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        fs, mt, aging, quality_loop, health,
        packaging_loop, mr, co,
        cs, tb, cf, en, op,
        sa, fr
    ]
)

# Define sequencing and concurrency via order edges
# 1. Farm selection to milk testing to cheese aging to quality loop
root.order.add_edge(fs, mt)
root.order.add_edge(mt, aging)
root.order.add_edge(aging, quality_loop)

# 2. After quality approved, get health certification
root.order.add_edge(quality_loop, health)

# 3. After health certification launch parallel branches:
#    a) Packaging design & label approval loop
#    b) Market research → customer outreach
#    c) Cold chain & customs & export & order processing
#    d) Sustainability audit
root.order.add_edge(health, packaging_loop)
root.order.add_edge(health, mr)
root.order.add_edge(health, cs)
root.order.add_edge(health, sa)

#   b) marketing branch
root.order.add_edge(mr, co)

#   c) logistics & export branch
root.order.add_edge(cs, tb)
root.order.add_edge(tb, cf)
root.order.add_edge(cf, en)
root.order.add_edge(en, op)

# 4. After all branches complete, do feedback review
root.order.add_edge(packaging_loop, fr)
root.order.add_edge(co, fr)
root.order.add_edge(op, fr)
root.order.add_edge(sa, fr)