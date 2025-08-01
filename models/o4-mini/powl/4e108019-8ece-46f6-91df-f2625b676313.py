# Generated from: 4e108019-8ece-46f6-91df-f2625b676313.json
# Description: This process involves dynamically adjusting supply chain operations based on real-time data inputs from multiple sources including weather forecasts, geopolitical events, and market demand fluctuations. It coordinates procurement, production scheduling, logistics, and inventory management by continuously evaluating risk factors and optimizing resource allocation. The process employs predictive analytics to anticipate disruptions and initiate contingency protocols, ensuring minimal downtime and cost efficiency. Cross-functional teams collaborate to validate adjustments, confirm supplier capabilities, and realign distribution strategies to maintain service levels while adapting to evolving external conditions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
di  = Transition(label='Data Ingestion')
ra  = Transition(label='Risk Assessment')
dfc = Transition(label='Demand Forecast')
sa  = Transition(label='Supplier Audit')
ic  = Transition(label='Inventory Check')
cp  = Transition(label='Capacity Plan')
su  = Transition(label='Schedule Update')
lr  = Transition(label='Logistics Review')
cs  = Transition(label='Contingency Setup')
ral = Transition(label='Resource Align')
cts = Transition(label='Cross-team Sync')
op  = Transition(label='Order Prioritize')
ca  = Transition(label='Cost Analysis')
pt  = Transition(label='Performance Track')
cv  = Transition(label='Compliance Verify')
fl  = Transition(label='Feedback Loop')

# Build the core partial‐order of one iteration
main_flow = StrictPartialOrder(nodes=[di, ra, dfc,
                                      sa, ic,
                                      cp,
                                      su, lr,
                                      cs,
                                      ral,
                                      cts,
                                      op, ca,
                                      pt, cv])

# Data ingestion precedes risk assessment and demand forecasting (which run in parallel)
main_flow.order.add_edge(di, ra)
main_flow.order.add_edge(di, dfc)

# Both risk assessment and demand forecast precede supplier audit and inventory check
main_flow.order.add_edge(ra, sa)
main_flow.order.add_edge(ra, ic)
main_flow.order.add_edge(dfc, sa)
main_flow.order.add_edge(dfc, ic)

# Audit and inventory check precede capacity planning
main_flow.order.add_edge(sa, cp)
main_flow.order.add_edge(ic, cp)

# Capacity planning precedes schedule update and logistics review (parallel)
main_flow.order.add_edge(cp, su)
main_flow.order.add_edge(cp, lr)

# Schedule update and logistics review precede contingency setup
main_flow.order.add_edge(su, cs)
main_flow.order.add_edge(lr, cs)

# Contingency setup precedes resource alignment
main_flow.order.add_edge(cs, ral)

# Resource alignment precedes cross‐team synchronization
main_flow.order.add_edge(ral, cts)

# Cross‐team sync precedes order prioritization and cost analysis (parallel)
main_flow.order.add_edge(cts, op)
main_flow.order.add_edge(cts, ca)

# Order prioritization leads to performance tracking; cost analysis leads to compliance check
main_flow.order.add_edge(op, pt)
main_flow.order.add_edge(ca, cv)

# Wrap the core flow in a loop with a feedback step
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[main_flow, fl]
)