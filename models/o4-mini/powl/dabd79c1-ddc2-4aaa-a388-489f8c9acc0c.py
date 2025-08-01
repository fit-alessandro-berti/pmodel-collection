# Generated from: dabd79c1-ddc2-4aaa-a388-489f8c9acc0c.json
# Description: This process involves the detailed authentication of historical artifacts to verify provenance and ensure authenticity before acquisition or exhibition. It begins with initial documentation review, followed by scientific testing such as radiocarbon dating and material composition analysis. Experts in art history then conduct stylistic evaluations, comparing findings against known databases. Concurrently, legal checks assess ownership history and export permissions. If discrepancies arise, a secondary expert panel convenes for arbitration. Upon successful validation, conservation specialists recommend preservation methods. Final approval is granted by the acquisitions committee, after which logistics coordinate secure transport and insurance. This workflow ensures that artifacts entering collections are genuine and legally obtained, minimizing risks associated with forgery or illicit trade.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Atomic activities
doc_review    = Transition(label='Document Review')
mat_test      = Transition(label='Material Testing')
radio_date    = Transition(label='Radiocarbon Date')
sty_eval      = Transition(label='Stylistic Eval')
db_check      = Transition(label='Database Check')
own_audit     = Transition(label='Ownership Audit')
export_verify = Transition(label='Export Verify')
expert_arb    = Transition(label='Expert Arbitration')
cons_plan     = Transition(label='Conservation Plan')
risk_assess   = Transition(label='Risk Assessment')
approval_rev  = Transition(label='Approval Review')
acq_meet      = Transition(label='Acquisitions Meet')
ins_setup     = Transition(label='Insurance Setup')
sec_trans     = Transition(label='Secure Transport')
final_doc     = Transition(label='Final Documentation')

# Silent transition for skipping arbitration
skip = SilentTransition()

# XOR choice: either skip or go to expert arbitration
arbitration = OperatorPOWL(operator=Operator.XOR, children=[skip, expert_arb])

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    doc_review,
    mat_test, radio_date,
    sty_eval, db_check,
    own_audit, export_verify,
    arbitration,
    cons_plan, risk_assess,
    approval_rev, acq_meet,
    ins_setup, sec_trans,
    final_doc
])

# 1) Initial documentation review → scientific tests
root.order.add_edge(doc_review, mat_test)
root.order.add_edge(doc_review, radio_date)

# 2) Tests → stylistic evaluation
root.order.add_edge(mat_test, sty_eval)
root.order.add_edge(radio_date, sty_eval)

# 3) Stylistic evaluation → database check
root.order.add_edge(sty_eval, db_check)

# 4) Tests → legal checks (concurrent with expert eval)
root.order.add_edge(mat_test, own_audit)
root.order.add_edge(radio_date, own_audit)
root.order.add_edge(mat_test, export_verify)
root.order.add_edge(radio_date, export_verify)

# 5) After both evaluations and legal checks → arbitration choice
root.order.add_edge(db_check, arbitration)
root.order.add_edge(own_audit, arbitration)
root.order.add_edge(export_verify, arbitration)

# 6) After arbitration → conservation plan → risk assessment
root.order.add_edge(arbitration, cons_plan)
root.order.add_edge(cons_plan, risk_assess)

# 7) Risk assessment → approval review → acquisitions meeting
root.order.add_edge(risk_assess, approval_rev)
root.order.add_edge(approval_rev, acq_meet)

# 8) After acquisitions meet → logistics (insurance & transport in parallel)
root.order.add_edge(acq_meet, ins_setup)
root.order.add_edge(acq_meet, sec_trans)

# 9) Both logistics tasks → final documentation
root.order.add_edge(ins_setup, final_doc)
root.order.add_edge(sec_trans, final_doc)