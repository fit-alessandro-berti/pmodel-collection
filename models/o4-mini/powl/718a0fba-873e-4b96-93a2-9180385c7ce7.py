# Generated from: 718a0fba-873e-4b96-93a2-9180385c7ce7.json
# Description: This process outlines the atypical yet realistic supply chain management for urban beekeeping. It involves sourcing sustainable hive materials from local artisans, coordinating micro-scale nectar collection schedules with city flora bloom cycles, ensuring compliance with municipal regulations on apiary placement, monitoring hive health remotely using IoT sensors, orchestrating community workshops for beekeeper training, managing seasonal honey extraction and packaging, facilitating direct-to-consumer urban farmers markets sales, and implementing a feedback loop for continuous product and process improvement. The complexity arises from intertwining ecological factors, regulatory constraints, and hyper-localized logistics within a dense urban environment, demanding agile coordination across diverse stakeholders.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
ms = Transition(label='Material Sourcing')
al = Transition(label='Artisan Liaison')
da = Transition(label='Design Approval')
rc = Transition(label='Regulation Check')
bm = Transition(label='Bloom Mapping')
nt = Transition(label='Nectar Timing')
hs = Transition(label='Hive Setup')
si = Transition(label='Sensor Install')
hm = Transition(label='Health Monitor')
wp = Transition(label='Workshop Plan')
td = Transition(label='Training Deliver')
he = Transition(label='Honey Extract')
pp = Transition(label='Packaging Prep')
msu = Transition(label='Market Setup')

# Body of the process (one iteration)
body = StrictPartialOrder(nodes=[ms, al, da, rc, bm, nt, hs, si, hm, wp, td, he, pp, msu])
edges_body = [
    (ms, al),
    (al, da),
    (da, rc),
    (rc, bm),
    (bm, nt),
    (nt, hs),
    (hs, si),
    (si, hm),
    (hm, wp),
    (wp, td),
    (td, he),
    (he, pp),
    (pp, msu)
]
for src, tgt in edges_body:
    body.order.add_edge(src, tgt)

# Feedback segment for loop
cf = Transition(label='Customer Feedback')
pr = Transition(label='Process Review')
feedback = StrictPartialOrder(nodes=[cf, pr])
feedback.order.add_edge(cf, pr)

# Loop: execute body, then either exit or perform feedback and repeat
root = OperatorPOWL(operator=Operator.LOOP, children=[body, feedback])