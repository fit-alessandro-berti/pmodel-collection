# Generated from: 56b8dd67-451f-4a64-bbe2-d681a2eed576.json
# Description: This process governs the intricate coordination required to facilitate international loans of valuable artworks between museums, galleries, and private collectors. It involves provenance verification, customs compliance, conditional insurance underwriting, climate-controlled transportation planning, and installation scheduling. The process also addresses risk mitigation, legal documentation, multi-party approvals, and real-time status reporting to ensure the artwork's integrity and security throughout transit and display. Stakeholders include conservators, legal teams, logistics providers, and curators, all collaborating to meet strict deadlines and maintain cultural heritage standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
provenance_check = Transition(label='Provenance Check')
loan_request    = Transition(label='Loan Request')
legal_review    = Transition(label='Legal Review')
risk_assess     = Transition(label='Risk Assessment')
insurance_setup = Transition(label='Insurance Setup')
customs_filing  = Transition(label='Customs Filing')
condition_rpt   = Transition(label='Condition Report')
pack_design     = Transition(label='Packaging Design')
climate_plan    = Transition(label='Climate Plan')
security_clear  = Transition(label='Security Clearance')
transport_book  = Transition(label='Transport Booking')
install_prep    = Transition(label='Installation Prep')
stakeholder_sync= Transition(label='Stakeholder Sync')
status_update   = Transition(label='Status Update')
final_approval  = Transition(label='Final Approval')
deinstallation  = Transition(label='Deinstallation')
return_logistics= Transition(label='Return Logistics')

# Silent skip for optional insurance
skip = SilentTransition()

# Exclusive choice: either do insurance setup or skip
xor_insurance = OperatorPOWL(operator=Operator.XOR,
                             children=[insurance_setup, skip])

# Loop: do stakeholder sync and status updates repeatedly until exit
loop_updates = OperatorPOWL(operator=Operator.LOOP,
                           children=[stakeholder_sync, status_update])

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    loan_request,
    provenance_check,
    legal_review,
    risk_assess,
    xor_insurance,
    customs_filing,
    condition_rpt,
    pack_design,
    climate_plan,
    security_clear,
    transport_book,
    install_prep,
    loop_updates,
    final_approval,
    deinstallation,
    return_logistics
])

# Define the ordering/dependencies
root.order.add_edge(loan_request, provenance_check)
root.order.add_edge(provenance_check, legal_review)
root.order.add_edge(legal_review, risk_assess)

# After risk assessment, optionally do insurance
root.order.add_edge(risk_assess, xor_insurance)

# Then customs filing
root.order.add_edge(xor_insurance, customs_filing)

# After customs, the following prep tasks can run in parallel
for task in [condition_rpt, pack_design, climate_plan, security_clear]:
    root.order.add_edge(customs_filing, task)

# All prep tasks must finish before booking transport
for task in [condition_rpt, pack_design, climate_plan, security_clear]:
    root.order.add_edge(task, transport_book)

# Transport booking → installation prep → reporting loop → final approval
root.order.add_edge(transport_book, install_prep)
root.order.add_edge(install_prep, loop_updates)
root.order.add_edge(loop_updates, final_approval)

# Final approval → deinstallation → return logistics
root.order.add_edge(final_approval, deinstallation)
root.order.add_edge(deinstallation, return_logistics)