# Generated from: f6d7b41c-13e9-4589-a8cc-c20658c7f869.json
# Description: This process involves leasing high-value artwork to corporations for office display, combining legal, logistical, and curatorial expertise. It begins with client consultation to assess aesthetic and spatial needs, followed by artwork selection from a curated inventory or bespoke acquisitions. Legal agreements cover insurance, liability, and lease terms. Logistics coordinate secure transportation and installation by specialized art handlers. Periodic condition reports and appraisals ensure preservation and compliance. The process includes renewal negotiations or artwork rotation to keep displays fresh. Financial reconciliation manages lease payments, tax implications, and depreciation schedules. Finally, deinstallation and return or purchase options complete the cycle, emphasizing sustainability and client relationship management throughout.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
cc = Transition(label='Client Consult')
na = Transition(label='Needs Assess')
asel = Transition(label='Art Selection')
inv = Transition(label='Inventory Check')
ld = Transition(label='Legal Draft')
cs = Transition(label='Contract Sign')
ins = Transition(label='Insurance Setup')
tp = Transition(label='Transport Plan')
st = Transition(label='Secure Transit')
ai = Transition(label='Art Install')
cck = Transition(label='Condition Check')
al = Transition(label='Appraisal Log')
pp = Transition(label='Payment Process')
lr = Transition(label='Lease Renew')
da = Transition(label='Deinstall Art')
ri = Transition(label='Return Inspect')
po = Transition(label='Purchase Option')

# Initial linear sequence up to installation
initial_po = StrictPartialOrder(nodes=[cc, na, asel, inv, ld, cs, ins, tp, st, ai])
initial_po.order.add_edge(cc, na)
initial_po.order.add_edge(na, asel)
initial_po.order.add_edge(asel, inv)
initial_po.order.add_edge(inv, ld)
initial_po.order.add_edge(ld, cs)
initial_po.order.add_edge(cs, ins)
initial_po.order.add_edge(ins, tp)
initial_po.order.add_edge(tp, st)
initial_po.order.add_edge(st, ai)

# Periodic cycle: condition check, appraisal, payment
periodic_cycle = StrictPartialOrder(nodes=[cck, al, pp])
periodic_cycle.order.add_edge(cck, al)
periodic_cycle.order.add_edge(al, pp)

# Loop: do periodic_cycle, then optionally Lease Renew and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[periodic_cycle, lr])

# Final choice after deinstallation: inspect return or purchase option
final_choice = OperatorPOWL(operator=Operator.XOR, children=[ri, po])

# Root model: initial sequence >> loop >> deinstallation >> final choice
root = StrictPartialOrder(nodes=[initial_po, loop, da, final_choice])
root.order.add_edge(initial_po, loop)
root.order.add_edge(loop, da)
root.order.add_edge(da, final_choice)