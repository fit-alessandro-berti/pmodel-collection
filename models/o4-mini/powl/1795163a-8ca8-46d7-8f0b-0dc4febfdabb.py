# Generated from: 1795163a-8ca8-46d7-8f0b-0dc4febfdabb.json
# Description: This process manages the complex coordination involved in swapping transport assets between multiple logistics providers across different regions. It includes verification of asset conditions, regulatory compliance checks, scheduling synchronized handoffs, and reconciling financial and legal obligations. The process ensures that assets such as containers, vehicles, or equipment are efficiently exchanged while minimizing downtime and maintaining traceability through digital ledgers and real-time communication channels, adapting dynamically to delays or discrepancies detected during transit or inspection phases.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
av = Transition(label='Asset Verify')
cc = Transition(label='Condition Check')
caud = Transition(label='Compliance Audit')
ss = Transition(label='Schedule Sync')
hc = Transition(label='Handoff Confirm')
dr = Transition(label='Documentation Review')
fr = Transition(label='Financial Reconcile')
lv = Transition(label='Legal Validate')
lu = Transition(label='Ledger Update')
tt = Transition(label='Transit Track')
dm = Transition(label='Delay Monitor')
df = Transition(label='Discrepancy Flag')
cale = Transition(label='Communication Alert')
ir = Transition(label='Inspection Report')
fa = Transition(label='Final Approval')
se = Transition(label='Swap Execute')

# Loop body: track -> monitor -> flag
seq_loop_a = StrictPartialOrder(nodes=[tt, dm, df])
seq_loop_a.order.add_edge(tt, dm)
seq_loop_a.order.add_edge(dm, df)

# Loop: perform tracking/monitoring/flagging, then optionally alert and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[seq_loop_a, cale])

# Root partial order
root = StrictPartialOrder(nodes=[av, cc, caud, ss, hc, dr, fr, lv, lu, loop, ir, fa, se])

# Define the main sequence
root.order.add_edge(av, cc)
root.order.add_edge(cc, caud)
root.order.add_edge(caud, ss)
root.order.add_edge(ss, hc)
root.order.add_edge(hc, dr)
root.order.add_edge(dr, fr)
root.order.add_edge(fr, lv)
root.order.add_edge(lv, lu)
root.order.add_edge(lu, loop)
root.order.add_edge(loop, ir)
root.order.add_edge(ir, fa)
root.order.add_edge(fa, se)