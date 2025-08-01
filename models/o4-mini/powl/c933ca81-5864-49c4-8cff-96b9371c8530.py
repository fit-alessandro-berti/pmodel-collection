# Generated from: c933ca81-5864-49c4-8cff-96b9371c8530.json
# Description: This process outlines the specialized steps involved in the custom manufacturing of drones tailored to unique client specifications. It begins with client consultation to define precise requirements, followed by design iteration incorporating advanced aerodynamics and AI integration. Components procurement involves sourcing rare materials and bespoke electronics. Subsequent phases include precision assembly, multi-layer firmware installation, and rigorous environmental testing under varying conditions. Quality assurance ensures compliance with international aviation standards before packaging with custom branding. Finally, logistics coordination manages secure delivery and post-sale technical support to ensure optimal drone performance and customer satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
cc = Transition(label='Client Consult')
sf = Transition(label='Spec Finalize')
dd = Transition(label='Design Draft')
at = Transition(label='Aerodynamics Test')
ai = Transition(label='AI Integration')
ms = Transition(label='Material Sourcing')
co = Transition(label='Component Order')
al = Transition(label='Assembly Line')
fi = Transition(label='Firmware Install')
et = Transition(label='Environmental Test')
qc = Transition(label='Quality Check')
bp = Transition(label='Brand Packaging')
sp = Transition(label='Shipping Prep')
ds = Transition(label='Delivery Schedule')
ps = Transition(label='Post-Sale Support')

# Define the concurrent testing partial order (aerodynamics & AI can be done in any order)
tests = StrictPartialOrder(nodes=[at, ai])
# No edges => at and ai are concurrent

# Define the design iteration loop: draft design, then perform tests, then optionally repeat
design_loop = OperatorPOWL(operator=Operator.LOOP, children=[dd, tests])

# Build the top‐level workflow partial order
root = StrictPartialOrder(nodes=[
    cc, sf,               # consultation & spec
    design_loop,          # iterative design & testing
    ms, co,               # procurement
    al,                   # assembly
    fi,                   # firmware
    et,                   # environmental testing
    qc,                   # quality assurance
    bp,                   # packaging
    sp, ds,               # logistics
    ps                    # post‐sale support
])

# Specify the control‐flow dependencies
root.order.add_edge(cc, sf)
root.order.add_edge(sf, design_loop)
root.order.add_edge(design_loop, ms)
root.order.add_edge(design_loop, co)
root.order.add_edge(ms, al)
root.order.add_edge(co, al)
root.order.add_edge(al, fi)
root.order.add_edge(fi, et)
root.order.add_edge(et, qc)
root.order.add_edge(qc, bp)
root.order.add_edge(bp, sp)
root.order.add_edge(sp, ds)
root.order.add_edge(ds, ps)