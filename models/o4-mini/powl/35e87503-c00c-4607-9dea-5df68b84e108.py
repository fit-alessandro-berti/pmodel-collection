# Generated from: 35e87503-c00c-4607-9dea-5df68b84e108.json
# Description: This process outlines the end-to-end workflow for commissioning bespoke artwork tailored to individual client preferences. It begins with initial client inquiry and concept briefing, proceeds through iterative design proposals and client feedback sessions, incorporates material sourcing and artist scheduling, and culminates in final production, quality assurance, packaging, and delivery. Throughout, the process involves coordination between multiple stakeholders including clients, artists, suppliers, and logistics, ensuring custom specifications are met while managing timelines and budgets efficiently. Post-delivery follow-ups and archival documentation close the cycle, enabling repeat business and portfolio enhancement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as POWL transitions
ci = Transition(label='Client Inquiry')
cb = Transition(label='Concept Brief')
dd = Transition(label='Design Draft')
fr = Transition(label='Feedback Review')
ms = Transition(label='Material Sourcing')
asched = Transition(label='Artist Scheduling')
pc = Transition(label='Prototype Creation')
qc = Transition(label='Quality Check')
ca = Transition(label='Client Approval')
fp = Transition(label='Final Production')
pp = Transition(label='Packaging Prep')
sa = Transition(label='Shipping Arrange')
dc = Transition(label='Delivery Confirm')
pf = Transition(label='Post Followup')
ar = Transition(label='Archive Records')

# Loop for iterative design and feedback
design_loop = OperatorPOWL(operator=Operator.LOOP, children=[dd, fr])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    ci, cb,               # start
    design_loop,          # iterative design-feedback
    ms, asched,           # material & scheduling (concurrent)
    pc, qc, ca,           # prototype -> quality -> approval
    fp, pp, sa, dc,       # production -> packaging -> shipping -> confirm
    pf, ar                # post follow-up & archive (concurrent)
])

# Define the control-flow edges
root.order.add_edge(ci, cb)
root.order.add_edge(cb, design_loop)

# After the design loop, do material sourcing and artist scheduling in parallel
root.order.add_edge(design_loop, ms)
root.order.add_edge(design_loop, asched)

# Both must finish before prototype creation
root.order.add_edge(ms, pc)
root.order.add_edge(asched, pc)

# Sequential steps thereafter
root.order.add_edge(pc, qc)
root.order.add_edge(qc, ca)
root.order.add_edge(ca, fp)
root.order.add_edge(fp, pp)
root.order.add_edge(pp, sa)
root.order.add_edge(sa, dc)

# Post-delivery activities in parallel
root.order.add_edge(dc, pf)
root.order.add_edge(dc, ar)