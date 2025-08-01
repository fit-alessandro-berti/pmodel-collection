# Generated from: 67ef1b6a-8f8b-44ff-9c9c-fccb32f54247.json
# Description: This process outlines the comprehensive steps required to authenticate ancient artifacts for museum acquisition. It begins with preliminary provenance verification, followed by multi-disciplinary scientific analysis including radiocarbon dating and material composition assessment. Next, expert consultations and stylistic comparisons are conducted to validate cultural origin. The process also involves condition reporting, risk assessment for transportation, and legal compliance checks related to export/import regulations. Finally, a formal authentication report is compiled and submitted for board approval before acquisition decision and artifact cataloging occur, ensuring a thorough and legally compliant authentication workflow for rare historical items.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
p = Transition(label='Provenance Check')
rct = Transition(label='Radiocarbon Test')
ma = Transition(label='Material Analysis')
sr = Transition(label='Stylistic Review')
ec = Transition(label='Expert Consultation')
cr = Transition(label='Condition Report')
ra = Transition(label='Risk Assessment')
lc = Transition(label='Legal Compliance')
ev = Transition(label='Export Verification')
ic = Transition(label='Import Clearance')
ad = Transition(label='Authentication Draft')
ba = Transition(label='Board Approval')
acq = Transition(label='Acquisition Decision')
ce = Transition(label='Catalog Entry')
tp = Transition(label='Transport Planning')

# Build the partial order
root = StrictPartialOrder(nodes=[
    p, rct, ma, ec, sr, cr, ra, lc, ev, ic, tp, ad, ba, acq, ce
])

# Provenance leads to parallel scientific analyses
root.order.add_edge(p, rct)
root.order.add_edge(p, ma)

# Both analyses must complete before expert review and stylistic review
root.order.add_edge(rct, ec)
root.order.add_edge(rct, sr)
root.order.add_edge(ma, ec)
root.order.add_edge(ma, sr)

# Reviews synchronize into a condition report
root.order.add_edge(ec, cr)
root.order.add_edge(sr, cr)

# Condition report enables risk assessment and legal compliance
root.order.add_edge(cr, ra)
root.order.add_edge(cr, lc)

# Risk assessment leads to transport planning
root.order.add_edge(ra, tp)

# Legal compliance branches into export and import checks
root.order.add_edge(lc, ev)
root.order.add_edge(lc, ic)

# All preparatory tasks precede the authentication draft
root.order.add_edge(tp, ad)
root.order.add_edge(ev, ad)
root.order.add_edge(ic, ad)

# Final sequencing: draft -> board approval -> acquisition -> catalog entry
root.order.add_edge(ad, ba)
root.order.add_edge(ba, acq)
root.order.add_edge(acq, ce)