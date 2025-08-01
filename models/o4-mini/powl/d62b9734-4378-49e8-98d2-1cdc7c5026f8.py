# Generated from: d62b9734-4378-49e8-98d2-1cdc7c5026f8.json
# Description: This process involves the detailed verification and authentication of rare cultural artifacts acquired from diverse global sources. It begins with initial provenance research, followed by multi-spectral imaging and material composition analysis. Expert consultations and historical cross-referencing are conducted to confirm authenticity. Legal ownership is verified through international registries and customs documentation. The artifact then undergoes conservation status assessment before final certification is issued. Throughout the process, secure data logging and chain-of-custody protocols ensure integrity and traceability, essential for auction or museum acquisition purposes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
t_pc   = Transition(label='Provenance Check')
t_ic   = Transition(label='Image Capture')
t_ms   = Transition(label='Material Scan')
t_er   = Transition(label='Expert Review')
t_hc   = Transition(label='Historical Cross')
t_lv   = Transition(label='Legal Verify')
t_rs   = Transition(label='Registry Search')
t_cc   = Transition(label='Customs Clear')
t_ca   = Transition(label='Condition Assess')
t_dl   = Transition(label='Data Log')
t_cco  = Transition(label='Chain Custody')
t_rd   = Transition(label='Report Draft')
t_cert = Transition(label='Certification')
t_sa   = Transition(label='Secure Archive')
t_ap   = Transition(label='Auction Prep')

# Build the partial order
root = StrictPartialOrder(nodes=[
    t_pc, t_ic, t_ms, t_er, t_hc, t_lv,
    t_rs, t_cc, t_ca, t_dl, t_cco,
    t_rd, t_cert, t_sa, t_ap
])

# Sequence: provenance → imaging & scan
root.order.add_edge(t_pc, t_ic)
root.order.add_edge(t_pc, t_ms)
# After imaging & scan → expert & historical
root.order.add_edge(t_ic, t_er)
root.order.add_edge(t_ic, t_hc)
root.order.add_edge(t_ms, t_er)
root.order.add_edge(t_ms, t_hc)
# After reviews → legal verify
root.order.add_edge(t_er, t_lv)
root.order.add_edge(t_hc, t_lv)
# Legal verify → registry & customs
root.order.add_edge(t_lv, t_rs)
root.order.add_edge(t_lv, t_cc)
# Registry & customs → condition assess
root.order.add_edge(t_rs, t_ca)
root.order.add_edge(t_cc, t_ca)
# Condition assess → report → certification
root.order.add_edge(t_ca, t_rd)
root.order.add_edge(t_rd, t_cert)
# Certification → archive & auction prep
root.order.add_edge(t_cert, t_sa)
root.order.add_edge(t_cert, t_ap)

# 'Data Log' and 'Chain Custody' remain unconstrained (concurrent with all)