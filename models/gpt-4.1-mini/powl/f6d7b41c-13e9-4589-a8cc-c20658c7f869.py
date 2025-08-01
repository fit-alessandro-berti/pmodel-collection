# Generated from: f6d7b41c-13e9-4589-a8cc-c20658c7f869.json
# Description: This process involves leasing high-value artwork to corporations for office display, combining legal, logistical, and curatorial expertise. It begins with client consultation to assess aesthetic and spatial needs, followed by artwork selection from a curated inventory or bespoke acquisitions. Legal agreements cover insurance, liability, and lease terms. Logistics coordinate secure transportation and installation by specialized art handlers. Periodic condition reports and appraisals ensure preservation and compliance. The process includes renewal negotiations or artwork rotation to keep displays fresh. Financial reconciliation manages lease payments, tax implications, and depreciation schedules. Finally, deinstallation and return or purchase options complete the cycle, emphasizing sustainability and client relationship management throughout.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
client_consult = Transition(label='Client Consult')
needs_assess = Transition(label='Needs Assess')
art_selection = Transition(label='Art Selection')
inventory_check = Transition(label='Inventory Check')
legal_draft = Transition(label='Legal Draft')
contract_sign = Transition(label='Contract Sign')
insurance_setup = Transition(label='Insurance Setup')
transport_plan = Transition(label='Transport Plan')
secure_transit = Transition(label='Secure Transit')
art_install = Transition(label='Art Install')
condition_check = Transition(label='Condition Check')
appraisal_log = Transition(label='Appraisal Log')
lease_renew = Transition(label='Lease Renew')
payment_process = Transition(label='Payment Process')
deinstall_art = Transition(label='Deinstall Art')
return_inspect = Transition(label='Return Inspect')
purchase_option = Transition(label='Purchase Option')

# Choice between Inventory Check and bespoke Art Selection path
inventory_vs_bespoke = OperatorPOWL(operator=Operator.XOR, children=[inventory_check, art_selection])

# Legal agreements - assume signing requires setup and drafting in partial order
legal_part = StrictPartialOrder(nodes=[legal_draft, contract_sign, insurance_setup])
legal_part.order.add_edge(legal_draft, contract_sign)
legal_part.order.add_edge(contract_sign, insurance_setup)

# Logistics partial order
logistics_part = StrictPartialOrder(nodes=[transport_plan, secure_transit, art_install])
logistics_part.order.add_edge(transport_plan, secure_transit)
logistics_part.order.add_edge(secure_transit, art_install)

# Condition Check and Appraisal Log are concurrent
condition_appraisal = StrictPartialOrder(nodes=[condition_check, appraisal_log])
# no order edges -> concurrent

# Renewal negotiation or artwork rotation represented as choice in a loop:
# Loop children: A = renewal negotiations, B = artwork rotation (modeled as Condition Check + Appraisal + loop body)
# For clarity, the loop structure: after condition/appraisal,
# either exit loop by lease renew, or do renewal and continue

# Loop body (B): Condition Check + Appraisal Log executed concurrently in a PO; 
# after that, payment processing and deinstallation + return or purchase options

payment_and_end = StrictPartialOrder(nodes=[payment_process, deinstall_art])
payment_and_end.order.add_edge(payment_process, deinstall_art)

return_vs_purchase = OperatorPOWL(operator=Operator.XOR, children=[return_inspect, purchase_option])

end_part = StrictPartialOrder(nodes=[payment_and_end, return_vs_purchase])
end_part.order.add_edge(payment_and_end, return_vs_purchase)

# Compose the loop body with Condition and Appraisal then end part
body_loop = StrictPartialOrder(nodes=[condition_appraisal, end_part])
body_loop.order.add_edge(condition_appraisal, end_part)  # condition/appraisal before payment...etc

# Loop: after lease renew, the process can loop again or exit (modeled by silent transition)
# But lease renew appears after appraisal/condition + payment etc. 
# To fit description: periodic condition reports/appraisals -> renewal negotiations or artwork rotation to keep fresh
# We'll represent loop as:
# Loop(A=lease renew, B= body_loop)
# But the description suggests we do condition check/appraisal then loop with renewal or exit,
# So we should move lease renew into loop head (A), body is artwork rotation phases.

# We'll merge condition_appraisal and lease_renew in loop body with loop head as 'lease renew', since it is periodic.

# But looking closer:
# Loop executes A then chooses exit or executes B then A again repeatedly

# We can set:
# - A = lease renew
# - B = condition_check + appraisal_log + payment and deinstallation + return/purchase

# Because condition check/appraisal precede renewal negotiations repeatedly, alternative is:

# Actually, prior appraisal etc. then lease renew loops or exit.

# To best map this, do:
# Loop head = (X(lease_renew, skip)) to represent option to renew or exit, or just lease_renew with optional skip.
# Body = condition_appraisal + payment & end_part (to simulate rotation cycle)

# However, description says 'renewal negotiations or artwork rotation', so choice before loop iteration.

# Let's make loop children: 
# A = lease_renew (the renewal negotiation)
# B = condition_appraisal then payment_and_end and return_vs_purchase

# loop = *(lease_renew, body_loop)
# We need to execute condition_appraisal + end parts before renewal, but note the description:
# "Periodic condition reports and appraisals ensure preservation and compliance. The process includes renewal negotiations or artwork rotation to keep displays fresh."

# Possibly better:
# First, do condition/appraisal then loop for renewal or not

# So:
# body_loop = StrictPartialOrder(nodes=[condition_check, appraisal_log])
# loop = *(lease_renew, body_loop)

# But the payment etc. done after renewal or rotation ?

# Considering process flow:
# - After condition/appraisal: payment process and deinstallation/return or purchase options

# So payment and end should be after loop; loop is for renewal negotiation + artwork rotation (condition/appraisal)

# Hence:
# loop = *(lease_renew, condition_appraisal)

# Then after loop, payment_process, deinstallation, and return/purchase choice.

loop = OperatorPOWL(operator=Operator.LOOP, children=[lease_renew, condition_appraisal])

# Finally, build the full process partial order:

# Nodes:
nodes = [
    client_consult,
    needs_assess,
    inventory_vs_bespoke,
    legal_part,
    insurance_setup,  # inside legal_part, but included in case for clarity 
    logistics_part,
    loop,
    payment_process,
    deinstall_art,
    return_vs_purchase
]

# Actually payment_process, deinstall_art, return_vs_purchase are inside payment_and_end, which is already considered.

# Final composition:

# Stepwise order edges:
root = StrictPartialOrder(nodes=[
    client_consult,
    needs_assess,
    inventory_vs_bespoke,
    legal_part,
    logistics_part,
    loop,
    payment_process,
    deinstall_art,
    return_vs_purchase
])

# Control flow order:

root.order.add_edge(client_consult, needs_assess)
root.order.add_edge(needs_assess, inventory_vs_bespoke)
root.order.add_edge(inventory_vs_bespoke, legal_part)
root.order.add_edge(legal_part, logistics_part)
root.order.add_edge(logistics_part, loop)
root.order.add_edge(loop, payment_process)
root.order.add_edge(payment_process, deinstall_art)
root.order.add_edge(deinstall_art, return_vs_purchase)