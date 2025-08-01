# Generated from: 9f1d86cb-3f0e-4481-b0ee-e169d2be0a37.json
# Description: This process involves the comprehensive verification and authentication of historical artifacts using a multi-disciplinary approach. It includes initial provenance research, scientific material analysis, contextual historical comparison, expert peer review, digital imaging, and blockchain certification. Each artifact undergoes condition assessment, restoration feasibility evaluation, and risk management before final authentication. The process integrates advanced AI pattern recognition with manual expert validation, ensuring both technological precision and human judgment. The cycle concludes with secure cataloging and controlled public disclosure, balancing conservation needs with scholarly access while maintaining a transparent audit trail for future reference and potential repatriation claims.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
provenance = Transition(label='Provenance Check')
material = Transition(label='Material Scan')
context = Transition(label='Context Review')
peer = Transition(label='Peer Review')
imaging = Transition(label='Imaging Capture')
blockchain = Transition(label='Blockchain Cert')
condition = Transition(label='Condition Assess')
restore = Transition(label='Restoration Plan')
risk = Transition(label='Risk Evaluate')
ai = Transition(label='AI Analysis')
expert = Transition(label='Expert Consult')
catalog = Transition(label='Catalog Entry')
public_release = Transition(label='Public Release')
audit = Transition(label='Audit Log')
repat = Transition(label='Repatriation Eval')

# Silent transitions for loop exit and optional repatriation
skip_loop = SilentTransition()
skip_repat = SilentTransition()

# Loop: integrate AI Analysis with manual Expert Consult until exit
body_loop = StrictPartialOrder(nodes=[ai, expert])
body_loop.order.add_edge(ai, expert)
ai_expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[body_loop, skip_loop])

# Optional repatriation evaluation
repatriation_xor = OperatorPOWL(operator=Operator.XOR, children=[repat, skip_repat])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    provenance, material, context, peer,
    imaging, blockchain, condition, restore, risk,
    ai_expert_loop, catalog, public_release, audit, repatriation_xor
])

# Add ordering edges
root.order.add_edge(provenance, material)
root.order.add_edge(provenance, context)
root.order.add_edge(material, peer)
root.order.add_edge(context, peer)
root.order.add_edge(peer, imaging)
root.order.add_edge(imaging, blockchain)
root.order.add_edge(blockchain, condition)
root.order.add_edge(condition, restore)
root.order.add_edge(restore, risk)
root.order.add_edge(risk, ai_expert_loop)
root.order.add_edge(ai_expert_loop, catalog)
root.order.add_edge(catalog, public_release)
root.order.add_edge(catalog, audit)
root.order.add_edge(audit, repatriation_xor)