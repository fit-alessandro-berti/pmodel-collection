# Generated from: 3fcab79a-85eb-49ae-8fec-06ab017ac03d.json
# Description: This process governs the complex flow of licensing dynamic, generative art pieces to multiple digital platforms under varying usage rights and time-bound exclusivity. It involves continuous monitoring of artwork versioning, real-time negotiation of terms based on AI-generated demand forecasts, adaptive royalty recalculations, cross-platform synchronization of rights management, and automated dispute resolution triggered by unauthorized derivative works or usage breaches. The process requires coordination between legal, technical, and creative teams to ensure compliance, optimize revenue streams, and maintain artistic integrity while navigating multi-jurisdictional intellectual property laws and evolving digital distribution standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
asub     = Transition(label='Art Submission')
vctrl    = Transition(label='Version Control')
dbkp     = Transition(label='Data Backup')
demand   = Transition(label='Demand Forecast')
rsetup   = Transition(label='Royalty Setup')
tneg     = Transition(label='Term Negotiation')
cdraft   = Transition(label='Contract Draft')
psync    = Transition(label='Platform Sync')
umon     = Transition(label='Usage Monitor')
dtrig    = Transition(label='Dispute Trigger')
lconsult = Transition(label='Legal Consult')
pproc    = Transition(label='Payment Process')
ccheck   = Transition(label='Compliance Check')
rgen     = Transition(label='Report Generate')
ralert   = Transition(label='Renewal Alert')
skip     = SilentTransition()

# 1) Adaptive‐royalty loop: negotiate terms, then (loop) do demand forecast → royalty setup → renegotiate …
sub_adaptive = StrictPartialOrder(nodes=[demand, rsetup])
sub_adaptive.order.add_edge(demand, rsetup)
loop_adaptive = OperatorPOWL(operator=Operator.LOOP, children=[tneg, sub_adaptive])

# 2) Dispute‐resolution loop: monitor usage, then (if a dispute) dispute trigger → legal consult → back to monitor
sub_resolve = StrictPartialOrder(nodes=[dtrig, lconsult])
sub_resolve.order.add_edge(dtrig, lconsult)
loop_resolve = OperatorPOWL(operator=Operator.LOOP, children=[umon, sub_resolve])

# 3) Rights‐review check: if issues ⇒ legal consult, else skip
xor_issue = OperatorPOWL(operator=Operator.XOR, children=[skip, lconsult])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    asub, vctrl, dbkp,
    ccheck, rreview := Transition(label='Rights Review'), xor_issue,
    loop_adaptive, cdraft,
    psync, loop_resolve,
    pproc, rgen, ralert
])

# 1) After art submission: version control & backup in parallel
root.order.add_edge(asub, vctrl)
root.order.add_edge(asub, dbkp)

# 2) After version control: rights review & compliance check
root.order.add_edge(vctrl, rreview)
root.order.add_edge(vctrl, ccheck)

# 3) Rights‐review feeds into the issue check (XOR)
root.order.add_edge(rreview, xor_issue)

# 4) Both compliance‐check and issue‐check must complete before adaptive loop
root.order.add_edge(ccheck, loop_adaptive)
root.order.add_edge(xor_issue, loop_adaptive)

# 5) After exiting the adaptive loop, draft the contract
root.order.add_edge(loop_adaptive, cdraft)

# 6) From contract draft: sync to platforms, process payments, generate reports (latter two in parallel)
root.order.add_edge(cdraft, psync)
root.order.add_edge(cdraft, pproc)
root.order.add_edge(cdraft, rgen)

# 7) Platform sync then triggers the dispute‐resolution loop & can also kick off payments
root.order.add_edge(psync, loop_resolve)
root.order.add_edge(psync, pproc)

# 8) Once the dispute‐loop exits or payments/reports complete, send a renewal alert
root.order.add_edge(loop_resolve, ralert)
root.order.add_edge(pproc, ralert)
root.order.add_edge(rgen, ralert)