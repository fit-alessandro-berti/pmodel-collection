# Generated from: b6f50622-e1bf-496e-bdbe-9490d85cc24c.json
# Description: This process involves the intricate verification and authentication of rare cultural artifacts sourced from multiple continents. It begins with initial provenance research, followed by scientific material analysis and expert consultation. The process requires coordinating with international regulatory bodies, performing forensic age dating, and executing advanced imaging techniques. After validation, artifact digitization and certification are carried out before final cataloging into a secure database. Throughout, legal compliance checks and ownership transfer protocols ensure legitimacy while mitigating risks of illicit trade. The process concludes with archival storage recommendations and stakeholder reporting to maintain transparency and integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
t_pc = Transition(label='Provenance Check')
t_ma = Transition(label='Material Analysis')
t_er = Transition(label='Expert Review')
t_rl = Transition(label='Regulatory Liaison')
t_ad = Transition(label='Age Dating')
t_is = Transition(label='Imaging Scan')
t_dc = Transition(label='Digital Capture')
t_cf = Transition(label='Certification')
t_db = Transition(label='Database Entry')
t_ca = Transition(label='Compliance Audit')
t_ot = Transition(label='Ownership Transfer')
t_ra = Transition(label='Risk Assessment')
t_ap = Transition(label='Archival Prep')
t_sr = Transition(label='Stakeholder Report')
t_fa = Transition(label='Final Approval')

# Build a strict partial order over all activities
root = StrictPartialOrder(nodes=[
    t_pc, t_ma, t_er, t_rl, t_ad, t_is,
    t_dc, t_cf, t_db, t_ca, t_ot, t_ra,
    t_ap, t_sr, t_fa
])

# 1) After Provenance Check, do Material Analysis and Expert Review in parallel
root.order.add_edge(t_pc, t_ma)
root.order.add_edge(t_pc, t_er)

# 2) After both MA and ER, run Regulatory Liaison, Age Dating, Imaging Scan in parallel
for nxt in (t_rl, t_ad, t_is):
    root.order.add_edge(t_ma, nxt)
    root.order.add_edge(t_er, nxt)

# 3) After those three, proceed to Digital Capture → Certification → Database Entry
for prev in (t_rl, t_ad, t_is):
    root.order.add_edge(prev, t_dc)
root.order.add_edge(t_dc, t_cf)
root.order.add_edge(t_cf, t_db)

# 4) 'Throughout' the main flow, Compliance Audit, Ownership Transfer, Risk Assessment
#    can start after Provenance Check (i.e., run concurrently thereafter)
for audit in (t_ca, t_ot, t_ra):
    root.order.add_edge(t_pc, audit)

# 5) After Database Entry, do Archival Prep → Stakeholder Report
root.order.add_edge(t_db, t_ap)
root.order.add_edge(t_ap, t_sr)

# 6) Final Approval requires the report and also that audit/transfer/risk steps have been initiated
root.order.add_edge(t_sr, t_fa)
for audit in (t_ca, t_ot, t_ra):
    root.order.add_edge(audit, t_fa)