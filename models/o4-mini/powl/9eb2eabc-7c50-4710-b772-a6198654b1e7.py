# Generated from: 9eb2eabc-7c50-4710-b772-a6198654b1e7.json
# Description: This process outlines the end-to-end assembly of custom drones tailored to specific client requirements. It involves initial design consultation, component sourcing from multiple suppliers, firmware customization, iterative prototype testing, regulatory compliance checks, final quality assurance, and packaging. The process also includes dynamic risk assessment, supply chain adjustments based on inventory fluctuations, and post-production client training to ensure proper drone operation. Each stage requires coordination among engineering, procurement, and logistics teams to deliver a fully functional, reliable drone solution meeting both performance and safety standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
db = Transition(label='Design Brief')
cs = Transition(label='Component Sourcing')
fw = Transition(label='Firmware Setup')
pb = Transition(label='Prototype Build')
ft = Transition(label='Flight Testing')
rv = Transition(label='Regulatory Review')
ra = Transition(label='Risk Assessment')
sa = Transition(label='Supplier Audit')
ic = Transition(label='Inventory Check')
qc = Transition(label='Quality Control')
pp = Transition(label='Packaging Prep')
ct = Transition(label='Client Training')
fr = Transition(label='Feedback Review')
pr = Transition(label='Production Ramp')
ss = Transition(label='Shipping Schedule')

# Silent transition for loop exits
skip = SilentTransition()

# Supply chain adjustment loop: audit then optionally check inventory and repeat audit
supply_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[sa, ic]
)

# Prototype testing partial order
testing_PO = StrictPartialOrder(nodes=[pb, ft, fr])
testing_PO.order.add_edge(pb, ft)
testing_PO.order.add_edge(ft, fr)

# Iterative prototype testing loop
testing_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[testing_PO, skip]
)

# Regulatory compliance loop: review then risk assessment, repeat if needed
reg_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[rv, ra]
)

# Root partial order combining all stages
root = StrictPartialOrder(
    nodes=[
        db,
        cs,
        supply_loop,
        fw,
        testing_loop,
        reg_loop,
        pr,
        qc,
        pp,
        ct,
        ss
    ]
)

# Define the sequencing dependencies
root.order.add_edge(db, cs)
root.order.add_edge(cs, supply_loop)
root.order.add_edge(supply_loop, fw)
root.order.add_edge(fw, testing_loop)
root.order.add_edge(testing_loop, reg_loop)
root.order.add_edge(reg_loop, pr)
root.order.add_edge(pr, qc)
root.order.add_edge(qc, pp)
root.order.add_edge(pp, ct)
root.order.add_edge(ct, ss)