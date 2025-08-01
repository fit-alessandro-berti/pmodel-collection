# Generated from: af23eed9-0a5b-46bd-9ff0-a6366aa95c30.json
# Description: This process is designed to authenticate and verify the provenance of rare historical artifacts prior to acquisition by a museum. It involves multidisciplinary evaluations including forensic material analysis, provenance research, expert consultations, and legal clearance. Initial steps include artifact intake and preliminary condition assessment, followed by spectroscopy and carbon dating tests to validate age. Concurrently, provenance documentation is gathered and cross-referenced with archival databases to detect forgeries or ownership disputes. Expert historians and conservators provide interpretive reports, while legal teams ensure compliance with cultural heritage laws. The process concludes with a comprehensive authentication report and decision on acquisition, ensuring the artifact’s legitimacy and ethical procurement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
ti = Transition(label='Artifact Intake')
cc = Transition(label='Condition Check')
ms = Transition(label='Material Scan')
ad = Transition(label='Age Dating')
ps = Transition(label='Provenance Search')
ar = Transition(label='Archive Review')
fc = Transition(label='Forgery Check')
ec = Transition(label='Expert Consult')
hr = Transition(label='Historical Report')
ci = Transition(label='Conservator Input')
ra = Transition(label='Risk Assessment')
lr = Transition(label='Legal Review')
ca = Transition(label='Compliance Audit')
fa = Transition(label='Final Analysis')
rg = Transition(label='Report Generation')
av = Transition(label='Acquisition Vote')

# Build the partial order
root = StrictPartialOrder(
    nodes=[ti, cc, ms, ad, ps, ar, fc, ec, hr, ci, ra, lr, ca, fa, rg, av]
)

# Define the control-flow dependencies
root.order.add_edge(ti, cc)

# After condition check, tests and provenance gathering run in parallel
root.order.add_edge(cc, ms)
root.order.add_edge(cc, ps)

# Material analysis branch
root.order.add_edge(ms, ad)

# Provenance branch
root.order.add_edge(ps, ar)
root.order.add_edge(ar, fc)

# After tests and forgery check, interpretive activities run in parallel
for pred in [ad, fc]:
    for succ in [ec, hr, ci, ra]:
        root.order.add_edge(pred, succ)

# After interpretive activities, legal and compliance reviews
for pred in [ec, hr, ci, ra]:
    root.order.add_edge(pred, lr)
    root.order.add_edge(pred, ca)

# Final consolidation and decision
root.order.add_edge(lr, fa)
root.order.add_edge(ca, fa)
root.order.add_edge(fa, rg)
root.order.add_edge(rg, av)