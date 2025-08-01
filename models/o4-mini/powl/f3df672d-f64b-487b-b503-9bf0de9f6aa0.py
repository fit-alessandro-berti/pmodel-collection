# Generated from: f3df672d-f64b-487b-b503-9bf0de9f6aa0.json
# Description: This process involves verifying the authenticity of rare and custom-made artifacts through multi-layered analysis combining historical research, material science tests, provenance validation, and expert consensus. It integrates unconventional data sources such as oral histories and blockchain records, followed by secure certification and archival. The process ensures artifacts are properly cataloged, insured, and prepared for exhibition or sale, while maintaining strict confidentiality and compliance with international cultural property laws. Final steps include continuous monitoring through IoT sensors and periodic re-validation to prevent fraud and degradation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
dc = Transition(label='Data Collection')
pc = Transition(label='Provenance Check')
ms = Transition(label='Material Scan')
hr = Transition(label='Historical Review')
pv = Transition(label='Blockchain Verify')
oh = Transition(label='Oral History')
ep = Transition(label='Expert Panel')
cr = Transition(label='Condition Report')
lr = Transition(label='Legal Review')
cert = Transition(label='Certification')
au = Transition(label='Archival Update')
ins = Transition(label='Insurance Setup')
prep = Transition(label='Exhibition Prep')
iot = Transition(label='IoT Monitoring')
rv = Transition(label='Re-validation')

# Loop for continuous monitoring and periodic re-validation
loop = OperatorPOWL(operator=Operator.LOOP, children=[iot, rv])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    dc, pc, ms, hr, pv, oh,
    ep, cr, lr, cert, au,
    ins, prep, loop
])

# 1) After data collection, run all analyses in parallel
root.order.add_edge(dc, pc)
root.order.add_edge(dc, ms)
root.order.add_edge(dc, hr)
root.order.add_edge(dc, pv)
root.order.add_edge(dc, oh)

# 2) All analyses must complete before the expert panel
root.order.add_edge(pc, ep)
root.order.add_edge(ms, ep)
root.order.add_edge(hr, ep)
root.order.add_edge(pv, ep)
root.order.add_edge(oh, ep)

# 3) Sequential processing after expert panel
root.order.add_edge(ep, cr)
root.order.add_edge(cr, lr)
root.order.add_edge(lr, cert)
root.order.add_edge(cert, au)

# 4) After archival update, insurance setup and exhibition prep can run concurrently
root.order.add_edge(au, ins)
root.order.add_edge(au, prep)

# 5) Both insurance setup and exhibition prep feed into the continuous monitoring loop
root.order.add_edge(ins, loop)
root.order.add_edge(prep, loop)