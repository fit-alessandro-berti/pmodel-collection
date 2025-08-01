# Generated from: 378c2769-7024-488f-a5e4-aeebd5cc3ae4.json
# Description: This process involves the authentication and validation of unique cultural artifacts destined for international auction. It begins with initial provenance research followed by multi-expert verification, material composition analysis, and advanced imaging inspections. Concurrently, legal compliance checks for cross-border transfers are conducted. If discrepancies arise, iterative consultations with historians occur. Once authenticated, the artifact undergoes secure packaging, insurance valuation, and digitized certification. Finally, the artifact is logged into a blockchain registry to ensure immutable provenance records before shipment to the auction house, ensuring transparency, security, and authenticity verification throughout the entire lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
p_check     = Transition(label='Provenance Check')
expert      = Transition(label='Expert Review')
material    = Transition(label='Material Scan')
imaging     = Transition(label='Imaging Analysis')
legal       = Transition(label='Legal Audit')
disc_flag   = Transition(label='Discrepancy Flag')
hist_consult= Transition(label='Historians Consult')
re_verif    = Transition(label='Re-Verification')
packing     = Transition(label='Secure Packing')
ins_quote   = Transition(label='Insurance Quote')
val_assess  = Transition(label='Value Assessment')
cert_issue  = Transition(label='Certification Issue')
bc_entry    = Transition(label='Blockchain Entry')
ship_prep   = Transition(label='Shipment Prep')
final_log   = Transition(label='Final Logging')

# Loop for iterative historian consultation if discrepancies arise
b_loop = StrictPartialOrder(nodes=[hist_consult, re_verif])
b_loop.order.add_edge(hist_consult, re_verif)
loop   = OperatorPOWL(operator=Operator.LOOP, children=[disc_flag, b_loop])

# Assemble the full partial order
root = StrictPartialOrder(nodes=[
    p_check, expert, material, imaging, legal,
    loop,
    packing, ins_quote, val_assess, cert_issue,
    bc_entry, ship_prep, final_log
])

# Initial sequence and concurrency with legal audit
root.order.add_edge(p_check,   expert)
root.order.add_edge(expert,    material)
root.order.add_edge(material,  imaging)
# legal audit runs concurrently, so no edge to the initial chain

# Join point before discrepancy loop
root.order.add_edge(imaging, loop)
root.order.add_edge(legal,   loop)

# After loop, the remaining linear workflow
root.order.add_edge(loop,     packing)
root.order.add_edge(packing,  ins_quote)
root.order.add_edge(ins_quote,val_assess)
root.order.add_edge(val_assess,cert_issue)
root.order.add_edge(cert_issue,bc_entry)
root.order.add_edge(bc_entry, ship_prep)
root.order.add_edge(ship_prep,final_log)