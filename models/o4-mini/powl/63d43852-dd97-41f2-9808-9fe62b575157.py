# Generated from: 63d43852-dd97-41f2-9808-9fe62b575157.json
# Description: This process outlines the cross-industry innovation cycle where ideas are sourced externally from unrelated sectors, filtered through multi-disciplinary teams, and then prototyped using adaptive methodologies. The process integrates continuous feedback loops from diverse stakeholders, including suppliers, customers, and regulatory bodies. It incorporates risk evaluation based on emerging trends and leverages collaborative digital platforms for knowledge sharing. The cycle culminates in scalable pilot projects before final market integration, ensuring adaptability and compliance across multiple domains while fostering sustainable competitive advantages through unconventional partnerships and resource utilization.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic transitions
idea        = Transition(label='Idea Sourcing')
cross       = Transition(label='Cross-Check')
feas        = Transition(label='Feasibility Study')
trend       = Transition(label='Trend Scanning')
risk        = Transition(label='Risk Assess')
know        = Transition(label='Knowledge Share')
stake       = Transition(label='Stakeholder Map')
partner     = Transition(label='Partner Align')
resource    = Transition(label='Resource Allocate')
concept     = Transition(label='Concept Design')
prototype   = Transition(label='Prototype Build')
feedback    = Transition(label='Feedback Loop')
pilot       = Transition(label='Pilot Launch')
perf        = Transition(label='Performance Review')
comp        = Transition(label='Compliance Check')
scale       = Transition(label='Scale Strategy')
market      = Transition(label='Market Integrate')

# Build the sub-model for design-build with feedback loop
cd_pb = StrictPartialOrder(nodes=[concept, prototype])
cd_pb.order.add_edge(concept, prototype)

# LOOP: do (Concept Design -> Prototype Build), then optionally Feedback Loop and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[cd_pb, feedback])

# Assemble the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    idea, cross, feas, trend, risk, know, stake, partner, resource,
    loop, pilot, perf, comp, scale, market
])

# Define the main control-flow edges
root.order.add_edge(idea,      cross)
root.order.add_edge(cross,     feas)
root.order.add_edge(feas,      trend)
root.order.add_edge(trend,     risk)
root.order.add_edge(risk,      know)
root.order.add_edge(know,      stake)
root.order.add_edge(stake,     partner)
root.order.add_edge(partner,   resource)
root.order.add_edge(resource,  loop)
root.order.add_edge(loop,      pilot)
root.order.add_edge(pilot,     perf)
root.order.add_edge(perf,      comp)
root.order.add_edge(comp,      scale)
root.order.add_edge(scale,     market)