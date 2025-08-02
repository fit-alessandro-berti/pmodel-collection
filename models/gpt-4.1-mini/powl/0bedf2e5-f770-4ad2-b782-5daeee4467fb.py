# Generated from: 0bedf2e5-f770-4ad2-b782-5daeee4467fb.json
# Description: This process involves locating, authenticating, restoring, and legally reclaiming lost or stolen antique assets from private collections, auctions, and international markets. It requires coordination between legal experts, historians, restoration specialists, and logistics teams to ensure the artifacts are properly verified, restored to their original condition, and returned to rightful owners or museums. The process also includes discreet negotiation, provenance research, customs clearance, and final documentation to safeguard the asset's value and legality throughout the reclamation journey.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Asset_Locate = Transition(label='Asset Locate')
Provenance_Check = Transition(label='Provenance Check')
Legal_Review = Transition(label='Legal Review')
Owner_Contact = Transition(label='Owner Contact')
Condition_Assess = Transition(label='Condition Assess')
Restoration_Plan = Transition(label='Restoration Plan')
Specialist_Hire = Transition(label='Specialist Hire')
Restoration_Work = Transition(label='Restoration Work')
Authentication_Test = Transition(label='Authentication Test')
Negotiation_Meet = Transition(label='Negotiation Meet')
Contract_Draft = Transition(label='Contract Draft')
Customs_Clear = Transition(label='Customs Clear')
Transport_Arrange = Transition(label='Transport Arrange')
Final_Inspection = Transition(label='Final Inspection')
Documentation_File = Transition(label='Documentation File')
Payment_Process = Transition(label='Payment Process')
Ownership_Transfer = Transition(label='Ownership Transfer')

# Build subprocesses:

# 1. Asset location and verification
locate_and_provenance = StrictPartialOrder(nodes=[Asset_Locate, Provenance_Check])
locate_and_provenance.order.add_edge(Asset_Locate, Provenance_Check)

# 2. Legal review and owner contact (legal experts involved before notification)
legal_and_owner = StrictPartialOrder(nodes=[Legal_Review, Owner_Contact])
legal_and_owner.order.add_edge(Legal_Review, Owner_Contact)

# 3. Condition assessment and restoration planning (historians/restoration specialists)
assessment_and_plan = StrictPartialOrder(nodes=[Condition_Assess, Restoration_Plan])
assessment_and_plan.order.add_edge(Condition_Assess, Restoration_Plan)

# 4. Specialist hire and restoration work (restoration specialists)
hire_and_restore = StrictPartialOrder(nodes=[Specialist_Hire, Restoration_Work])
hire_and_restore.order.add_edge(Specialist_Hire, Restoration_Work)

# 5. Authentication test after restoration
authentication = Authentication_Test

# 6. Negotiation meet and contract draft (discreet negotiation)
negotiation_contract = StrictPartialOrder(nodes=[Negotiation_Meet, Contract_Draft])
negotiation_contract.order.add_edge(Negotiation_Meet, Contract_Draft)

# 7. Customs clearance and transport arrange (logistics)
customs_transport = StrictPartialOrder(nodes=[Customs_Clear, Transport_Arrange])
customs_transport.order.add_edge(Customs_Clear, Transport_Arrange)

# 8. Final inspection and documentation file
inspection_and_doc = StrictPartialOrder(nodes=[Final_Inspection, Documentation_File])
inspection_and_doc.order.add_edge(Final_Inspection, Documentation_File)

# 9. Payment process and ownership transfer (finalize reclamation)
payment_and_transfer = StrictPartialOrder(nodes=[Payment_Process, Ownership_Transfer])
payment_and_transfer.order.add_edge(Payment_Process, Ownership_Transfer)

# Combine condition assessment subprocesses with restoration
# After assessment_and_plan -> hire_and_restore -> authentication
restoration_subprocess = StrictPartialOrder(
    nodes=[assessment_and_plan, hire_and_restore, authentication]
)
restoration_subprocess.order.add_edge(assessment_and_plan, hire_and_restore)
restoration_subprocess.order.add_edge(hire_and_restore, authentication)

# Combine all subprocesses in order based on likely control flow:
# locate_and_provenance -> legal_and_owner -> restoration_subprocess -> negotiation_contract -> customs_transport -> inspection_and_doc -> payment_and_transfer

root = StrictPartialOrder(
    nodes=[
        locate_and_provenance,
        legal_and_owner,
        restoration_subprocess,
        negotiation_contract,
        customs_transport,
        inspection_and_doc,
        payment_and_transfer,
    ]
)

# Add edges to represent ordering between subprocesses
root.order.add_edge(locate_and_provenance, legal_and_owner)
root.order.add_edge(legal_and_owner, restoration_subprocess)
root.order.add_edge(restoration_subprocess, negotiation_contract)
root.order.add_edge(negotiation_contract, customs_transport)
root.order.add_edge(customs_transport, inspection_and_doc)
root.order.add_edge(inspection_and_doc, payment_and_transfer)