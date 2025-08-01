# Generated from: 6d0c85fc-a7c3-435b-8ced-457293504f73.json
# Description: This process involves the meticulous restoration of antique items, blending historical research, material analysis, and precision craftsmanship. It begins with initial assessment and provenance verification, followed by detailed condition reporting and risk evaluation. Restoration planning includes sourcing period-appropriate materials and consulting specialists. The workflow proceeds with careful disassembly, cleaning, repair, and replacement of damaged elements using traditional techniques. Quality control is continuous, ensuring authenticity and structural integrity. Finally, documentation and preservation recommendations complete the process, supporting future maintenance and historical value retention.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define all activities as transitions
ia = Transition(label="Initial Assess")
pc = Transition(label="Provenance Check")
cr = Transition(label="Condition Report")
re = Transition(label="Risk Evaluate")
ms = Transition(label="Material Source")
ec = Transition(label="Expert Consult")
rp = Transition(label="Restoration Plan")
dis = Transition(label="Item Disassemble")
clean = Transition(label="Surface Clean")
repair = Transition(label="Structural Repair")
replace = Transition(label="Element Replace")
finish = Transition(label="Traditional Finish")
qc = Transition(label="Quality Control")
doc = Transition(label="Documentation")
pa = Transition(label="Preservation Advise")
fr = Transition(label="Final Review")

# Build the partial‐order workflow
root = StrictPartialOrder(
    nodes=[ia, pc, cr, re, ms, ec, rp, dis, clean, repair, replace, finish, qc, doc, pa, fr]
)

# Initial assessment and provenance check must finish before condition report and risk evaluation
root.order.add_edge(ia, cr)
root.order.add_edge(pc, cr)
root.order.add_edge(ia, re)
root.order.add_edge(pc, re)

# Condition report and risk evaluation feed into material sourcing and expert consultation
root.order.add_edge(cr, ms)
root.order.add_edge(re, ms)
root.order.add_edge(cr, ec)
root.order.add_edge(re, ec)

# Material source and expert consult feed into the restoration plan
root.order.add_edge(ms, rp)
root.order.add_edge(ec, rp)

# Restoration plan opens the disassembly‐to‐finish sequence
root.order.add_edge(rp, dis)
root.order.add_edge(dis, clean)
root.order.add_edge(clean, repair)
root.order.add_edge(repair, replace)
root.order.add_edge(replace, finish)

# After finishing, perform a final quality control
root.order.add_edge(finish, qc)

# Documentation and preservation advise follow quality control
root.order.add_edge(qc, doc)
root.order.add_edge(doc, pa)

# Final review closes the process
root.order.add_edge(pa, fr)