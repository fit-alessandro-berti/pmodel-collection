# Generated from: 3c65a68b-8bbf-41c3-994c-ea5fad0481dc.json
# Description: This process involves dynamically optimizing supply chain parameters by integrating real-time market analytics, supplier reliability scores, and environmental impact data. It requires continuous feedback loops between procurement, logistics, and production teams to recalibrate inventory thresholds and delivery schedules. Advanced predictive models guide adjustments to mitigate risks from geopolitical disruptions or sudden demand shifts. Regular cross-functional reviews ensure alignment with sustainability goals and financial constraints, resulting in an agile, resilient supply chain ecosystem that balances cost efficiency with responsiveness and environmental responsibility.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
mscan   = Transition(label="Market Scan")
saudit  = Transition(label="Supplier Audit")
dsync   = Transition(label="Data Sync")
rassess = Transition(label="Risk Assess")
dforecast = Transition(label="Demand Forecast")
icheck  = Transition(label="Inventory Check")
tset    = Transition(label="Threshold Set")
mupdate = Transition(label="Model Update")
sadjust = Transition(label="Schedule Adjust")
ireview = Transition(label="Impact Review")
cverify = Transition(label="Compliance Verify")
ctsync  = Transition(label="Cross-Team Sync")
fcollect = Transition(label="Feedback Collect")
canalyze = Transition(label="Cost Analyze")
salign   = Transition(label="Strategy Align")
rgenerate = Transition(label="Report Generate")

# Pre-loop partial order: initial market scan and supplier audit feeding into data sync
pre = StrictPartialOrder(nodes=[mscan, saudit, dsync])
pre.order.add_edge(mscan, dsync)
pre.order.add_edge(saudit, dsync)

# Loop body A: the recalibration cycle from Risk Assess through Schedule Adjust
A = StrictPartialOrder(
    nodes=[rassess, dforecast, icheck, tset, mupdate, sadjust]
)
A.order.add_edge(rassess, dforecast)
A.order.add_edge(dforecast, icheck)
A.order.add_edge(icheck, tset)
A.order.add_edge(icheck, mupdate)
A.order.add_edge(tset, sadjust)
A.order.add_edge(mupdate, sadjust)

# Loop body B: feedback and cross-functional alignment
B = StrictPartialOrder(
    nodes=[fcollect, canalyze, salign, ctsync]
)
B.order.add_edge(fcollect, canalyze)
B.order.add_edge(canalyze, salign)
B.order.add_edge(salign, ctsync)

# Define the feedback loop: do A, then either exit or do B then A again
loop_op = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Post-loop partial order: impact review, compliance verification, and final report
# We can inline these three as separate nodes in the root
# and order them sequentially.
root = StrictPartialOrder(
    nodes=[pre, loop_op, ireview, cverify, rgenerate]
)
# Connect pre -> loop
root.order.add_edge(pre, loop_op)
# Exit loop -> Impact Review -> Compliance Verify -> Report Generate
root.order.add_edge(loop_op, ireview)
root.order.add_edge(ireview, cverify)
root.order.add_edge(cverify, rgenerate)