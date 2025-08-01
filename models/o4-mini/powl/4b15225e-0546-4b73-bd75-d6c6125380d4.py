# Generated from: 4b15225e-0546-4b73-bd75-d6c6125380d4.json
# Description: This process describes a dynamic approach to supply chain management that integrates real-time data analytics, machine learning predictions, and decentralized decision-making across multiple stakeholders. It begins with continuous demand sensing to capture evolving customer preferences, followed by adaptive inventory adjustments that respond to market volatility. Supplier collaboration involves synchronized updates and risk assessments to mitigate disruptions. The process incorporates automated transport routing with contingency planning for delays, alongside quality compliance checks using IoT-enabled sensors. Financial reconciliation is performed through blockchain verification to ensure transparency and reduce fraud. Finally, performance feedback loops utilize AI-driven insights to refine forecasting models and operational strategies, enabling a resilient and responsive supply chain ecosystem that adapts proactively to unexpected changes and optimizes resource allocation efficiently.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ds = Transition(label='Demand Sensing')
dc = Transition(label='Data Collection')
ia = Transition(label='Inventory Adjust')
ov = Transition(label='Order Validation')
ss = Transition(label='Supplier Sync')
ra = Transition(label='Risk Assess')
da = Transition(label='Disruption Alert')
rp = Transition(label='Route Planning')
tm = Transition(label='Transport Monitor')
qc = Transition(label='Quality Check')
ca = Transition(label='Compliance Audit')
bv = Transition(label='Blockchain Verify')
pa = Transition(label='Payment Authorize')
fa = Transition(label='Feedback Analyze')
fu = Transition(label='Forecast Update')
sr = Transition(label='Strategy Revise')
ral = Transition(label='Resource Allocate')
skip = SilentTransition()

# Supplier collaboration subprocess: Supplier Sync and Risk Assess in parallel, then Disruption Alert
supplierPO = StrictPartialOrder(nodes=[ss, ra, da])
supplierPO.order.add_edge(ra, da)

# Transport subprocess: Route Planning then Transport Monitor
transportPO = StrictPartialOrder(nodes=[rp, tm])
transportPO.order.add_edge(rp, tm)

# Quality subprocess: Quality Check then Compliance Audit
qualityPO = StrictPartialOrder(nodes=[qc, ca])
qualityPO.order.add_edge(qc, ca)

# Combine transport and quality in parallel
transQualPO = StrictPartialOrder(nodes=[transportPO, qualityPO])

# Feedback cycle subprocess
feedbackCycle = StrictPartialOrder(nodes=[fa, fu, sr, ral])
feedbackCycle.order.add_edge(fa, fu)
feedbackCycle.order.add_edge(fu, sr)
feedbackCycle.order.add_edge(sr, ral)

# Loop for performance feedback until exit
feedbackLoop = OperatorPOWL(operator=Operator.LOOP, children=[feedbackCycle, skip])

# Root partial order connecting all subprocesses
root = StrictPartialOrder(nodes=[
    ds, dc, ia, ov,
    supplierPO,
    transQualPO,
    bv, pa,
    feedbackLoop
])
root.order.add_edge(ds, dc)
root.order.add_edge(dc, ia)
root.order.add_edge(ia, ov)
root.order.add_edge(ov, supplierPO)
root.order.add_edge(supplierPO, transQualPO)
root.order.add_edge(transQualPO, bv)
root.order.add_edge(bv, pa)
root.order.add_edge(pa, feedbackLoop)