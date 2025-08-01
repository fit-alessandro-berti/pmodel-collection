# Generated from: 2107561f-77cf-4c8f-bfa5-4a05bc072194.json
# Description: This process outlines the detailed steps involved in authenticating historical artifacts for museums and private collectors. It begins with preliminary provenance research and physical inspection, followed by advanced scientific analysis such as isotope dating and material composition tests. Experts then cross-reference findings with historical records and consult with specialized historians. The artifact undergoes condition assessment, restoration feasibility study, and ethical clearance review. Documentation is compiled into a comprehensive report, which is then verified by a peer review panel. Finally, authentication certification is issued, and the artifact is logged into a centralized registry for future reference and insurance purposes. Throughout the process, secure chain-of-custody protocols and confidentiality agreements are strictly maintained to ensure integrity and trustworthiness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
pc = Transition(label='Provenance Check')
vi = Transition(label='Visual Inspect')
mt = Transition(label='Material Test')
idate = Transition(label='Isotope Dating')
hcross = Transition(label='Historical Cross')
econsult = Transition(label='Expert Consult')
cond = Transition(label='Condition Assess')
plan = Transition(label='Restoration Plan')
ethics = Transition(label='Ethics Review')
report = Transition(label='Report Compile')
peer = Transition(label='Peer Review')
certify = Transition(label='Certify Authentic')
registry = Transition(label='Registry Log')
custody = Transition(label='Custody Secure')
confidentiality = Transition(label='Confidentiality')

# Build the partial order
root = StrictPartialOrder(nodes=[
    pc, vi, mt, idate, hcross, econsult, cond, plan, ethics,
    report, peer, certify, registry, custody, confidentiality
])

# Set ordering constraints
root.order.add_edge(pc, vi)
root.order.add_edge(vi, mt)
root.order.add_edge(vi, idate)
root.order.add_edge(mt, hcross)
root.order.add_edge(mt, econsult)
root.order.add_edge(idate, hcross)
root.order.add_edge(idate, econsult)
root.order.add_edge(hcross, cond)
root.order.add_edge(hcross, plan)
root.order.add_edge(hcross, ethics)
root.order.add_edge(econsult, cond)
root.order.add_edge(econsult, plan)
root.order.add_edge(econsult, ethics)
root.order.add_edge(cond, report)
root.order.add_edge(plan, report)
root.order.add_edge(ethics, report)
root.order.add_edge(report, peer)
root.order.add_edge(peer, certify)
root.order.add_edge(certify, registry)