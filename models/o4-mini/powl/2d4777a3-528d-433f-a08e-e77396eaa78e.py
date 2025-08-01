# Generated from: 2d4777a3-528d-433f-a08e-e77396eaa78e.json
# Description: This process involves sourcing rare and exotic ingredients from multiple remote regions worldwide, requiring intricate coordination between local suppliers, customs authorities, and quality assurance teams. The process includes verifying authenticity, negotiating exclusive contracts, managing complex logistics involving temperature control and legal compliance, and ensuring sustainable and ethical harvesting methods. Additionally, real-time tracking and risk mitigation strategies are implemented to handle geopolitical or environmental disruptions, while maintaining continuous communication with research and development to align ingredient specifications with emerging market trends and regulatory changes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
sv = Transition(label='Supplier Vetting')
cd = Transition(label='Contract Drafting')
ccus = Transition(label='Customs Clearance')
qt = Transition(label='Quality Testing')
lp = Transition(label='Logistics Planning')
tc = Transition(label='Temperature Control')
sa = Transition(label='Sustainability Audit')
er = Transition(label='Ethical Review')
ra = Transition(label='Risk Assessment')
rt = Transition(label='Real-time Tracking')
ma = Transition(label='Market Analysis')
rd = Transition(label='R&D Coordination')
cck = Transition(label='Compliance Check')
iu = Transition(label='Inventory Update')
pp = Transition(label='Payment Processing')

# Build the partial order
root = StrictPartialOrder(nodes=[
    sv, cd, ccus, qt, lp, tc, sa, er, ra, rt, ma, rd, cck, iu, pp
])

# Supplier vetting before contract drafting
root.order.add_edge(sv, cd)

# After contract drafting, start parallel preparations
root.order.add_edge(cd, ccus)
root.order.add_edge(cd, qt)
root.order.add_edge(cd, lp)
root.order.add_edge(cd, sa)
root.order.add_edge(cd, ma)
root.order.add_edge(cd, rd)

# Logistics and customs both precede temperature control
root.order.add_edge(lp, tc)
root.order.add_edge(ccus, tc)

# Temperature control enables real-time tracking
root.order.add_edge(tc, rt)

# Quality testing chain
root.order.add_edge(qt, er)
root.order.add_edge(er, cck)

# Sustainability audit leads to risk assessment
root.order.add_edge(sa, ra)

# Real-time tracking precedes inventory update
root.order.add_edge(rt, iu)

# Final payment processing awaits inventory arrival, compliance, risk clearance, and R&D sign-off
root.order.add_edge(iu, pp)
root.order.add_edge(cck, pp)
root.order.add_edge(ra, pp)
root.order.add_edge(rd, pp)