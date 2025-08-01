# Generated from: 5446dd11-a6f8-4479-87d3-d82632dba1db.json
# Description: This process outlines the complex supply chain of artisanal cheese production, starting from sourcing rare local milk varieties, ensuring microbial cultures are cultivated in controlled environments, and managing precise aging conditions. It involves batch testing for quality, coordinating with seasonal farmers, integrating traditional handcraft techniques with modern hygiene standards, managing niche market orders, and handling export regulatory compliance. The process also covers waste management, packaging optimization for delicate transport, and consumer feedback integration to continuously refine cheese profiles while preserving artisanal authenticity and sustainability goals.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities as POWL transitions
ms = Transition(label='Milk Sourcing')
cp = Transition(label='Culture Prep')
bt = Transition(label='Batch Testing')
coag = Transition(label='Coagulation')
cc = Transition(label='Curd Cutting')
mi = Transition(label='Mold Inoculation')
pr = Transition(label='Pressing')
sa = Transition(label='Salting')
asup = Transition(label='Aging Setup')
hc = Transition(label='Humidity Control')
qc = Transition(label='Quality Check')
pkg = Transition(label='Packaging')
op = Transition(label='Order Processing')
ec = Transition(label='Export Compliance')
wd = Transition(label='Waste Disposal')
ma = Transition(label='Market Analysis')
fr = Transition(label='Feedback Review')

# Main production sequence A
A = StrictPartialOrder(nodes=[
    ms, cp, bt, coag, cc, mi, pr, sa,
    asup, hc, qc, pkg, op, ec, wd
])
# concurrent start: Milk Sourcing and Culture Prep
A.order.add_edge(ms, bt)
A.order.add_edge(cp, bt)
# linear handcraft chain
A.order.add_edge(bt, coag)
A.order.add_edge(coag, cc)
A.order.add_edge(cc, mi)
A.order.add_edge(mi, pr)
A.order.add_edge(pr, sa)
# aging and environment control
A.order.add_edge(sa, asup)
A.order.add_edge(asup, hc)
A.order.add_edge(hc, qc)
# downstream logistics
A.order.add_edge(qc, pkg)
A.order.add_edge(pkg, op)
A.order.add_edge(op, ec)
# waste management at end
A.order.add_edge(ec, wd)

# Feedback loop body B
B = StrictPartialOrder(nodes=[ma, fr])
B.order.add_edge(ma, fr)

# Wrap in a LOOP: do A, then either exit or do (B then A) again
root = OperatorPOWL(operator=Operator.LOOP, children=[A, B])