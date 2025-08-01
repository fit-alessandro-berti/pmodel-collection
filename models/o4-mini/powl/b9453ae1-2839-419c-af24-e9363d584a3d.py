# Generated from: b9453ae1-2839-419c-af24-e9363d584a3d.json
# Description: This process governs the intricate supply chain for handcrafted artisan goods, integrating raw material sourcing from remote villages, quality certification by cultural experts, bespoke packaging design, and direct-to-consumer logistics. It involves multiple stakeholders including local artisans, certification bodies, eco-friendly transport providers, and niche market distributors, ensuring authenticity, sustainability, and cultural preservation while adapting dynamically to fluctuating demand and seasonal availability of materials.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic transitions
ms = Transition(label='Material Sourcing')
av = Transition(label='Artisan Vetting')
qa = Transition(label='Quality Audit')
cc = Transition(label='Cultural Certify')
dp = Transition(label='Design Packaging')
cl = Transition(label='Custom Labeling')
op = Transition(label='Order Processing')
ps = Transition(label='Payment Settlement')
et = Transition(label='Eco Transport')
df = Transition(label='Demand Forecast')
ma = Transition(label='Market Analysis')
rp = Transition(label='Restock Planning')
isyn = Transition(label='Inventory Sync')
sb = Transition(label='Stakeholder Meet')
comp = Transition(label='Compliance Check')
cf = Transition(label='Consumer Feedback')
rt = Transition(label='Return Handling')
skip = SilentTransition()

# 1) Compliance review is optional (stakeholder meet + compliance check) or skip
comp_po = StrictPartialOrder(nodes=[sb, comp])
comp_po.order.add_edge(sb, comp)
complianceChoice = OperatorPOWL(operator=Operator.XOR, children=[comp_po, skip])

# 2) Return handling is optional after feedback
returnChoice = OperatorPOWL(operator=Operator.XOR, children=[rt, skip])

# 3) Continuous restock loop: forecast -> analysis -> plan -> sync
A_body = StrictPartialOrder(nodes=[df, ma, rp, isyn])
A_body.order.add_edge(df, ma)
A_body.order.add_edge(ma, rp)
A_body.order.add_edge(rp, isyn)
# B_body is the same body for each loop iteration
B_body = StrictPartialOrder(nodes=[df, ma, rp, isyn])
B_body.order.add_edge(df, ma)
B_body.order.add_edge(ma, rp)
B_body.order.add_edge(rp, isyn)
loopRestock = OperatorPOWL(operator=Operator.LOOP, children=[A_body, B_body])

# 4) Build the main partial order
root = StrictPartialOrder(nodes=[
    ms, av, qa, cc, dp, cl,
    complianceChoice,
    op, ps,
    et, cf, returnChoice,
    loopRestock
])

# Define the main flow
root.order.add_edge(ms, av)
root.order.add_edge(av, qa)
root.order.add_edge(qa, cc)
root.order.add_edge(cc, dp)
root.order.add_edge(dp, cl)
root.order.add_edge(cl, complianceChoice)
root.order.add_edge(complianceChoice, op)
root.order.add_edge(op, ps)

# After payment, delivery and feedback proceed (in parallel)
root.order.add_edge(ps, et)
root.order.add_edge(ps, cf)
root.order.add_edge(cf, returnChoice)

# Restocking loop kicks off once sourcing starts
root.order.add_edge(ms, loopRestock)