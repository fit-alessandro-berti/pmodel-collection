# Generated from: 5d48f8fe-345f-4790-b182-418d2c7ee4bd.json
# Description: This process involves the complex evaluation and authentication of antique artifacts, combining historical research, scientific analysis, and expert consultations. It begins with initial artifact intake and condition assessment, followed by provenance verification through archival research. Scientific tests such as radiocarbon dating and material composition analysis are then conducted to validate the artifact's age and origin. Concurrently, expert appraisers evaluate stylistic and craftsmanship details. Results are synthesized into a comprehensive authentication report, which undergoes peer review before final certification is issued. The process also includes risk assessment for forgery and fraud prevention, culminating in secure documentation and artifact registration in a centralized database for future reference.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
ti = Transition(label="Artifact Intake")
cc = Transition(label="Condition Check")
ps = Transition(label="Provenance Search")
ar = Transition(label="Archive Review")
rt = Transition(label="Radiocarbon Test")
ms = Transition(label="Material Scan")
sa = Transition(label="Style Assessment")
ce = Transition(label="Craftsmanship Eval")
ec = Transition(label="Expert Consultation")
fr = Transition(label="Forgery Risk")
rd = Transition(label="Report Draft")
pr = Transition(label="Peer Review")
fc = Transition(label="Final Certification")
sr = Transition(label="Secure Registration")
db = Transition(label="Database Entry")

# Create the root partial order with all nodes
root = StrictPartialOrder(nodes=[
    ti, cc, ps, ar,
    rt, ms, sa, ce, ec,
    rd, pr, fr, fc,
    sr, db
])

# Define the control‐flow dependencies
root.order.add_edge(ti, cc)
root.order.add_edge(cc, ps)
root.order.add_edge(ps, ar)

# After archive review, run scientific tests & expert appraisals in parallel
root.order.add_edge(ar, rt)
root.order.add_edge(ar, ms)
root.order.add_edge(ar, sa)
root.order.add_edge(ar, ce)
root.order.add_edge(ar, ec)

# Once all analyses and appraisals finish, draft the report
for predecessor in (rt, ms, sa, ce, ec):
    root.order.add_edge(predecessor, rd)

# Peer review then risk assessment then final certification
root.order.add_edge(rd, pr)
root.order.add_edge(pr, fr)
root.order.add_edge(fr, fc)

# Final steps: secure registration and database entry
root.order.add_edge(fc, sr)
root.order.add_edge(sr, db)