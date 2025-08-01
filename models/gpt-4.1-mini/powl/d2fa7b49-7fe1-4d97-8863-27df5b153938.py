# Generated from: d2fa7b49-7fe1-4d97-8863-27df5b153938.json
# Description: This process involves the intricate verification and certification of rare cultural artifacts before international auction. It begins with artifact intake and preliminary assessment, followed by multi-disciplinary expert validation including historical, chemical, and provenance analyses. After validation, a blockchain-based authenticity token is minted to ensure traceability. Next, legal compliance checks across jurisdictions are conducted, alongside insurance valuation and risk assessment. Finally, the artifact undergoes packaging with climate control measures before secure transport arrangements are finalized for auction delivery.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all basic activities
artifact_intake = Transition(label='Artifact Intake')
preliminary_check = Transition(label='Preliminary Check')
historical_review = Transition(label='Historical Review')
chemical_test = Transition(label='Chemical Test')
provenance_audit = Transition(label='Provenance Audit')
expert_panel = Transition(label='Expert Panel')
token_minting = Transition(label='Token Minting')
legal_review = Transition(label='Legal Review')
compliance_check = Transition(label='Compliance Check')
insurance_valuation = Transition(label='Insurance Valuation')
risk_assessment = Transition(label='Risk Assessment')
packaging_prep = Transition(label='Packaging Prep')
climate_control = Transition(label='Climate Control')
transport_setup = Transition(label='Transport Setup')
final_approval = Transition(label='Final Approval')

# Multi-disciplinary expert validation: 'Historical Review', 'Chemical Test', 'Provenance Audit' concurrent
# followed by synchronization in 'Expert Panel'
experts_po = StrictPartialOrder(nodes=[historical_review, chemical_test, provenance_audit, expert_panel])
# All three expert tasks must precede the expert panel meeting
experts_po.order.add_edge(historical_review, expert_panel)
experts_po.order.add_edge(chemical_test, expert_panel)
experts_po.order.add_edge(provenance_audit, expert_panel)

# Legal and compliance checks done concurrently: 'Legal Review', 'Compliance Check', 'Insurance Valuation', 'Risk Assessment'
legal_compliance_po = StrictPartialOrder(nodes=[
    legal_review, compliance_check, insurance_valuation, risk_assessment
])
# No edges - all concurrent

# Packaging with climate control concurrent (both must finish before next)
packaging_po = StrictPartialOrder(nodes=[packaging_prep, climate_control])
# no order between packaging_prep and climate_control => concurrent

# Partial order for artifact intake --> preliminary check --> experts --> token minting
first_part = StrictPartialOrder(nodes=[
    artifact_intake, preliminary_check, experts_po, token_minting
])
first_part.order.add_edge(artifact_intake, preliminary_check)
first_part.order.add_edge(preliminary_check, experts_po)
first_part.order.add_edge(experts_po, token_minting)

# After token minting, legal_compliance and packaging are concurrent
# So define partial order with legal_compliance and packaging concurrent
post_token_po = StrictPartialOrder(nodes=[legal_compliance_po, packaging_po])
# no edges between legal_compliance_po and packaging_po => concurrent

# Then transport setup and final approval in sequence after both above
final_sequence = StrictPartialOrder(nodes=[transport_setup, final_approval])
final_sequence.order.add_edge(transport_setup, final_approval)

# Now connect overall:
# first_part --> post_token_po --> final_sequence
root = StrictPartialOrder(nodes=[first_part, post_token_po, transport_setup, final_approval])
root.order.add_edge(first_part, post_token_po)
root.order.add_edge(post_token_po, transport_setup)
root.order.add_edge(transport_setup, final_approval)