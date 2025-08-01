# Generated from: beea25ca-2e3e-4567-9349-f7275431b90c.json
# Description: This complex business process governs the authentication and provenance verification of rare historical artifacts before acquisition or exhibition. It involves multidisciplinary evaluations including chemical composition analysis, historical documentation cross-referencing, expert consultations, and advanced imaging techniques. The process ensures that artifacts meet stringent authenticity criteria by integrating scientific data with archival research. Each artifact undergoes risk assessment for forgery, condition appraisal, and legal clearance. The workflow culminates in a detailed provenance report and a decision on acquisition or loan, safeguarding institutional collections and maintaining public trust in exhibited items.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
sc = Transition(label='Sample Collection')
cs = Transition(label='Chemical Scan')
ic = Transition(label='Image Capture')
da = Transition(label='Data Analysis')
er = Transition(label='Expert Review')
asr = Transition(label='Archival Search')
fc = Transition(label='Forgery Check')
cnd = Transition(label='Condition Survey')
lr = Transition(label='Legal Review')
ra = Transition(label='Risk Assess')
rd = Transition(label='Report Draft')
pv = Transition(label='Provenance Verify')
av = Transition(label='Acquisition Vote')
ls = Transition(label='Loan Setup')
fa = Transition(label='Final Approval')
doc = Transition(label='Documentation')

# Acquisition and Loan branches
acq_po = StrictPartialOrder(nodes=[av, fa])
acq_po.order.add_edge(av, fa)

loan_po = StrictPartialOrder(nodes=[ls, fa])
loan_po.order.add_edge(ls, fa)

# Exclusive choice between acquisition or loan
decision = OperatorPOWL(operator=Operator.XOR, children=[acq_po, loan_po])

# Root partial order
root = StrictPartialOrder(nodes=[sc, cs, ic, da, er, asr, fc, cnd, lr, ra, rd, pv, decision, doc])

root.order.add_edge(sc, cs)
root.order.add_edge(sc, ic)
root.order.add_edge(cs, da)
root.order.add_edge(ic, da)
root.order.add_edge(da, er)
root.order.add_edge(da, asr)
root.order.add_edge(er, fc)
root.order.add_edge(asr, fc)
root.order.add_edge(er, cnd)
root.order.add_edge(asr, cnd)
root.order.add_edge(er, lr)
root.order.add_edge(asr, lr)
root.order.add_edge(fc, ra)
root.order.add_edge(cnd, ra)
root.order.add_edge(lr, ra)
root.order.add_edge(ra, rd)
root.order.add_edge(rd, pv)
root.order.add_edge(pv, decision)
root.order.add_edge(decision, doc)