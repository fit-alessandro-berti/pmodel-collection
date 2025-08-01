# Generated from: e08a7d64-544a-4c48-b9e7-18379f108723.json
# Description: This process outlines the intricate steps involved in authenticating rare historical artifacts for museums or private collectors. Beginning with initial provenance research, the workflow includes multidisciplinary scientific testing, expert consultations, and legal verifications to ensure authenticity and compliance with international cultural property laws. The process further addresses risk assessments, insurance appraisals, digital cataloging, and final certification issuance. Throughout the workflow, collaboration between historians, chemists, legal advisors, and logistics coordinators is critical to maintain integrity and transparency, culminating in secure artifact transfer or exhibition planning.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
pc = Transition(label='Provenance Check')
mt = Transition(label='Material Testing')
cr = Transition(label='Condition Report')
er = Transition(label='Expert Review')
lv = Transition(label='Legal Verify')
ra = Transition(label='Risk Assess')
iq = Transition(label='Insurance Quote')
ce = Transition(label='Catalog Entry')
ds = Transition(label='Digital Scan')
ct = Transition(label='Certification')
tp = Transition(label='Transport Plan')
cc = Transition(label='Customs Clear')
es = Transition(label='Exhibit Setup')
on = Transition(label='Owner Notify')
fa = Transition(label='Final Audit')

# Build the partial order
root = StrictPartialOrder(nodes=[
    pc, mt, cr, er, lv, ra, iq, ce, ds, ct, tp, cc, es, on, fa
])

# Initial provenance -> parallel branches
root.order.add_edge(pc, mt)
root.order.add_edge(pc, lv)

# Scientific testing branch: Material Testing -> Condition Report -> Expert Review
root.order.add_edge(mt, cr)
root.order.add_edge(cr, er)

# Legal branch: Legal Verify -> Risk Assess -> Insurance Quote
root.order.add_edge(lv, ra)
root.order.add_edge(ra, iq)

# After both Expert Review and Insurance Quote: digital cataloging (Catalog Entry, Digital Scan)
root.order.add_edge(er, ce)
root.order.add_edge(iq, ce)
root.order.add_edge(er, ds)
root.order.add_edge(iq, ds)

# Certification after cataloging
root.order.add_edge(ce, ct)
root.order.add_edge(ds, ct)

# Post-certification: transport planning and owner notification
root.order.add_edge(ct, tp)
root.order.add_edge(ct, on)

# Transport execution: Transport Plan -> Customs Clear -> Exhibit Setup
root.order.add_edge(tp, cc)
root.order.add_edge(cc, es)

# Final audit after exhibit setup and owner notification
root.order.add_edge(es, fa)
root.order.add_edge(on, fa)