# Generated from: a4299542-9b53-499a-b845-638e130cc69e.json
# Description: This process involves the detailed restoration of antique items, combining historical research, material analysis, delicate cleaning, and precise reconstruction to preserve authenticity while enhancing durability. It begins with provenance verification and condition assessment, followed by specialized treatment planning. Each step demands careful documentation and iterative quality checks to ensure that the restored artifact retains its original character. Collaborative input from historians, chemists, and artisans is integrated throughout. The process culminates in final preservation and detailed reporting for archival purposes, enabling museums or collectors to maintain cultural heritage effectively.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
pcheck   = Transition(label='Provenance Check')
cscan    = Transition(label='Condition Scan')
matest   = Transition(label='Material Test')
dmap     = Transition(label='Damage Map')
cprep    = Transition(label='Cleaning Prep')
sclean   = Transition(label='Surface Clean')
sfix     = Transition(label='Structural Fix')
pmatch   = Transition(label='Paint Match')
ctouch   = Transition(label='Color Touch')
fseal    = Transition(label='Finish Seal')
hcontrol = Transition(label='Humidity Control')
docu     = Transition(label='Documentation')
expert   = Transition(label='Expert Review')
quality  = Transition(label='Quality Audit')
final    = Transition(label='Final Report')

# Build the loop body: Documentation -> Expert Review
body = StrictPartialOrder(nodes=[docu, expert])
body.order.add_edge(docu, expert)

# LOOP: after each review you can exit or do a Quality Audit and then repeat
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[body, quality])

# Build the top‐level partial order (the overall sequence + the loop + final report)
root = StrictPartialOrder(nodes=[
    pcheck, cscan, matest, dmap, cprep, sclean, sfix,
    pmatch, ctouch, fseal, hcontrol, loop_node, final
])
root.order.add_edge(pcheck,   cscan)
root.order.add_edge(cscan,    matest)
root.order.add_edge(matest,   dmap)
root.order.add_edge(dmap,     cprep)
root.order.add_edge(cprep,    sclean)
root.order.add_edge(sclean,   sfix)
root.order.add_edge(sfix,     pmatch)
root.order.add_edge(pmatch,   ctouch)
root.order.add_edge(ctouch,   fseal)
root.order.add_edge(fseal,    hcontrol)
root.order.add_edge(hcontrol, loop_node)
root.order.add_edge(loop_node, final)