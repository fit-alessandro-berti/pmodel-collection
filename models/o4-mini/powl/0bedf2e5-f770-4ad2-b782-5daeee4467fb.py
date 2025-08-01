# Generated from: 0bedf2e5-f770-4ad2-b782-5daeee4467fb.json
# Description: This process involves locating, authenticating, restoring, and legally reclaiming lost or stolen antique assets from private collections, auctions, and international markets. It requires coordination between legal experts, historians, restoration specialists, and logistics teams to ensure the artifacts are properly verified, restored to their original condition, and returned to rightful owners or museums. The process also includes discreet negotiation, provenance research, customs clearance, and final documentation to safeguard the asset's value and legality throughout the reclamation journey.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define activities
asset_locate         = Transition(label='Asset Locate')
provenance_check     = Transition(label='Provenance Check')
legal_review         = Transition(label='Legal Review')
owner_contact        = Transition(label='Owner Contact')
condition_assess     = Transition(label='Condition Assess')
restoration_plan     = Transition(label='Restoration Plan')
specialist_hire      = Transition(label='Specialist Hire')
restoration_work     = Transition(label='Restoration Work')
authentication_test  = Transition(label='Authentication Test')
negotiation_meet     = Transition(label='Negotiation Meet')
contract_draft       = Transition(label='Contract Draft')
customs_clear        = Transition(label='Customs Clear')
transport_arrange    = Transition(label='Transport Arrange')
final_inspection     = Transition(label='Final Inspection')
documentation_file   = Transition(label='Documentation File')
payment_process      = Transition(label='Payment Process')
ownership_transfer   = Transition(label='Ownership Transfer')

# Build the strict partial order
root = StrictPartialOrder(nodes=[
    asset_locate,
    provenance_check,
    legal_review,
    owner_contact,
    condition_assess,
    restoration_plan,
    specialist_hire,
    restoration_work,
    authentication_test,
    negotiation_meet,
    contract_draft,
    customs_clear,
    transport_arrange,
    final_inspection,
    documentation_file,
    payment_process,
    ownership_transfer
])

# Define the control‐flow dependencies
root.order.add_edge(asset_locate,        provenance_check)
root.order.add_edge(provenance_check,    legal_review)
root.order.add_edge(legal_review,        owner_contact)
root.order.add_edge(owner_contact,       condition_assess)
root.order.add_edge(condition_assess,    restoration_plan)
root.order.add_edge(restoration_plan,    specialist_hire)
root.order.add_edge(specialist_hire,     restoration_work)
root.order.add_edge(restoration_work,    authentication_test)
root.order.add_edge(authentication_test, negotiation_meet)
root.order.add_edge(negotiation_meet,    contract_draft)
root.order.add_edge(contract_draft,      customs_clear)
root.order.add_edge(customs_clear,       transport_arrange)
root.order.add_edge(transport_arrange,   final_inspection)
root.order.add_edge(final_inspection,    documentation_file)
root.order.add_edge(documentation_file,  payment_process)
root.order.add_edge(payment_process,     ownership_transfer)