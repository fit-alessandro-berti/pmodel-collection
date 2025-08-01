# Generated from: db32f673-4372-486b-8b3f-8b10b78505e0.json
# Description: This process involves the intricate verification and certification of historical artifacts for museums and private collectors. It starts with initial artifact receipt and condition logging, followed by multi-modal scientific analysis including radiocarbon dating and spectroscopy. Expert consultations are scheduled to assess provenance, involving cross-referencing archival records and past ownership documentation. A risk assessment is performed to evaluate potential forgery or damage, then a digital 3D scan is created for virtual archiving. Legal compliance checks ensure cultural heritage laws are respected. The artifact is then insured, and an official certificate of authenticity is drafted and approved. Finally, the artifact is packaged under climate-controlled conditions for either display or secure storage, with ongoing monitoring scheduled for conservation purposes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
receive = Transition(label='Receive Artifact')
condition = Transition(label='Condition Log')
radiocarbon = Transition(label='Radiocarbon Test')
spectroscopy = Transition(label='Spectroscopy Scan')
consult = Transition(label='Expert Consult')
archive = Transition(label='Archive Search')
provenance = Transition(label='Provenance Check')
risk = Transition(label='Risk Assess')
scan3d = Transition(label='3D Scan')
legal = Transition(label='Legal Review')
insurance = Transition(label='Insurance Setup')
draft = Transition(label='Certificate Draft')
approve = Transition(label='Certificate Approve')
pack = Transition(label='Climate Pack')
plan = Transition(label='Conservation Plan')
monitor = Transition(label='Monitoring Schedule')

# Build the partial order
root = StrictPartialOrder(nodes=[
    receive, condition,
    radiocarbon, spectroscopy,
    consult, archive, provenance,
    risk, scan3d, legal, insurance,
    draft, approve, pack, plan, monitor
])

# Initial receipt and logging
root.order.add_edge(receive, condition)

# Scientific analysis in parallel
root.order.add_edge(condition, radiocarbon)
root.order.add_edge(condition, spectroscopy)

# Provenance assessment after both analyses
root.order.add_edge(radiocarbon, consult)
root.order.add_edge(radiocarbon, archive)
root.order.add_edge(spectroscopy, consult)
root.order.add_edge(spectroscopy, archive)
root.order.add_edge(consult, provenance)
root.order.add_edge(archive, provenance)

# Subsequent sequential steps
root.order.add_edge(provenance, risk)
root.order.add_edge(risk, scan3d)
root.order.add_edge(scan3d, legal)
root.order.add_edge(legal, insurance)
root.order.add_edge(insurance, draft)
root.order.add_edge(draft, approve)
root.order.add_edge(approve, pack)
root.order.add_edge(pack, plan)
root.order.add_edge(plan, monitor)