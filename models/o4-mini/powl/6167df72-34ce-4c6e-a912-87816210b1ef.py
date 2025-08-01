# Generated from: 6167df72-34ce-4c6e-a912-87816210b1ef.json
# Description: This process involves leasing high-value contemporary artworks to corporate clients on a rotating basis. It begins with client profiling to understand aesthetic preferences and office ambiance needs. Next, inventory curation pairs available art pieces with client tastes. Contracts are drafted with flexible terms allowing periodic swaps. Logistics coordinate secure transportation and installation at client sites. Regular condition inspections ensure artwork preservation. Client feedback is gathered to adjust future selections. Marketing campaigns target emerging art trends to refresh inventory. Financial reconciliation tracks leasing fees, insurance, and depreciation. Finally, renewal negotiations or returns conclude the cycle, ensuring continuous client engagement and asset management in a niche leasing market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
cp = Transition(label='Client Profiling')
ic = Transition(label='Inventory Check')
ac = Transition(label='Art Curation')
cd = Transition(label='Contract Draft')
tr = Transition(label='Terms Review')
lp = Transition(label='Logistics Plan')
ts = Transition(label='Transport Secure')
ia = Transition(label='Install Art')
ca = Transition(label='Condition Audit')
fc = Transition(label='Feedback Collect')
tm = Transition(label='Trend Monitor')
mp = Transition(label='Marketing Push')
ft = Transition(label='Finance Track')
rd = Transition(label='Renewal Discuss')
ar = Transition(label='Asset Return')

# Silent activity for the loop body
skip = SilentTransition()

# At the end of finance tracking we either renew or return
renewal_choice = OperatorPOWL(operator=Operator.XOR, children=[rd, ar])

# Build the main sequential workflow as a strict partial order
main_seq = StrictPartialOrder(nodes=[
    cp, ic, ac, cd, tr, lp, ts, ia, ca, fc, tm, mp, ft, renewal_choice
])
# Add the control‐flow edges in the given order
main_seq.order.add_edge(cp, ic)
main_seq.order.add_edge(ic, ac)
main_seq.order.add_edge(ac, cd)
main_seq.order.add_edge(cd, tr)
main_seq.order.add_edge(tr, lp)
main_seq.order.add_edge(lp, ts)
main_seq.order.add_edge(ts, ia)
main_seq.order.add_edge(ia, ca)
main_seq.order.add_edge(ca, fc)
main_seq.order.add_edge(fc, tm)
main_seq.order.add_edge(tm, mp)
main_seq.order.add_edge(mp, ft)
main_seq.order.add_edge(ft, renewal_choice)

# Wrap the entire cycle in a loop to allow repeated leasing rounds
root = OperatorPOWL(operator=Operator.LOOP, children=[main_seq, skip])