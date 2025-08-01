# Generated from: e83c6cbe-82da-478d-aa10-b35eb91ed2f6.json
# Description: This process involves the multi-layered verification and authentication of ancient artifacts before acquisition or exhibition. It begins with initial provenance research, followed by scientific material analysis, stylistic comparison, and expert consultations. Legal clearance and ethical sourcing checks are conducted alongside insurance valuation and risk assessment. The process also includes digital archiving, replica creation for display, and preparation for transport under controlled conditions. Finally, the artifact undergoes a final review meeting before formal cataloging and public announcement, ensuring authenticity, legality, and preservation standards are met comprehensively.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define activities
pc = Transition(label="Provenance Check")
mt = Transition(label="Material Testing")
sr = Transition(label="Stylistic Review")
ep = Transition(label="Expert Panel")
lc = Transition(label="Legal Clearance")
ea = Transition(label="Ethics Audit")
iq = Transition(label="Insurance Quote")
ra = Transition(label="Risk Assess")
da = Transition(label="Digital Archive")
rb = Transition(label="Replica Build")
tp = Transition(label="Transport Prep")
cr = Transition(label="Condition Report")
fr = Transition(label="Final Review")
ce = Transition(label="Catalog Entry")
pn = Transition(label="Public Notice")

# Build the partial order
root = StrictPartialOrder(nodes=[pc, mt, sr, ep, lc, ea, iq, ra, da, rb, tp, cr, fr, ce, pn])

# Step 1: Provenance Check before Material Testing, Stylistic Review, Expert Panel
for nxt in [mt, sr, ep]:
    root.order.add_edge(pc, nxt)

# Step 2: After MT, SR, EP perform Legal Clearance, Ethics Audit, Insurance Quote, Risk Assess
for prev in [mt, sr, ep]:
    for nxt in [lc, ea, iq, ra]:
        root.order.add_edge(prev, nxt)

# Step 3: After LC, EA, IQ, RA perform Digital Archive, Replica Build, Transport Prep
for prev in [lc, ea, iq, ra]:
    for nxt in [da, rb, tp]:
        root.order.add_edge(prev, nxt)

# Step 4: After archiving/build/prep, do Condition Report and Final Review (in parallel)
for prev in [da, rb, tp]:
    root.order.add_edge(prev, cr)
    root.order.add_edge(prev, fr)

# Step 5: Both Condition Report and Final Review complete before Catalog Entry, then Public Notice
root.order.add_edge(cr, ce)
root.order.add_edge(fr, ce)
root.order.add_edge(ce, pn)