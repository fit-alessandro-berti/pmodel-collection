# Generated from: 94526029-9d68-4e0b-b1ca-718620e2fbe4.json
# Description: This process involves locating, authenticating, and reclaiming lost or stolen antique assets from private collections or public sales. It requires extensive provenance research, legal clearance, negotiation with current holders, coordination with law enforcement, and meticulous documentation. The process also includes restoration assessment, insurance appraisal, and final asset repatriation to rightful owners or museums. Each step demands expert collaboration, risk management, and compliance with international cultural property laws to ensure ethical and legal recovery.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Asset_Locate = Transition(label='Asset Locate')
Provenance_Check = Transition(label='Provenance Check')
Legal_Review = Transition(label='Legal Review')
Ownership_Verify = Transition(label='Ownership Verify')
Law_Consult = Transition(label='Law Consult')
Holder_Contact = Transition(label='Holder Contact')
Negotiation_Lead = Transition(label='Negotiation Lead')
Forensic_Audit = Transition(label='Forensic Audit')
Restoration_Plan = Transition(label='Restoration Plan')
Insurance_Assess = Transition(label='Insurance Assess')
Customs_Clear = Transition(label='Customs Clear')
Transport_Arrange = Transition(label='Transport Arrange')
Documentation = Transition(label='Documentation')
Repatriate_Asset = Transition(label='Repatriate Asset')
Final_Report = Transition(label='Final Report')

# Build the partial order respecting the described logical flow with concurrency where logical
# The sequence is roughly:
# Asset Locate -> Provenance Check -> Legal Review -> Ownership Verify
# Then Law Consult and Holder Contact (can be concurrent but both depending on Ownership Verify)
# Then Negotiation Lead (depends on Holder Contact)
# Forensic Audit (depends on Negotiation Lead)
# Restoration Plan and Insurance Assess (can be concurrent after Forensic Audit)
# Customs Clear and Transport Arrange (can be concurrent but after Restoration Plan and Insurance Assess)
# Documentation (after Customs Clear and Transport Arrange)
# Repatriate Asset (after Documentation)
# Final Report (after Repatriate Asset)

# Note: Law Consult might be done concurrently with Holder Contact, both after Ownership Verify.

# Create the partial order node set
nodes = [
    Asset_Locate,
    Provenance_Check,
    Legal_Review,
    Ownership_Verify,
    Law_Consult,
    Holder_Contact,
    Negotiation_Lead,
    Forensic_Audit,
    Restoration_Plan,
    Insurance_Assess,
    Customs_Clear,
    Transport_Arrange,
    Documentation,
    Repatriate_Asset,
    Final_Report
]

root = StrictPartialOrder(nodes=nodes)

# Add edges to represent the ordering described above

# Linear start chain
root.order.add_edge(Asset_Locate, Provenance_Check)
root.order.add_edge(Provenance_Check, Legal_Review)
root.order.add_edge(Legal_Review, Ownership_Verify)

# After Ownership Verify, two concurrent branches: Law Consult and Holder Contact
root.order.add_edge(Ownership_Verify, Law_Consult)
root.order.add_edge(Ownership_Verify, Holder_Contact)

# Negotiation Lead depends on Holder Contact
root.order.add_edge(Holder_Contact, Negotiation_Lead)

# Forensic Audit depends on Negotiation Lead
root.order.add_edge(Negotiation_Lead, Forensic_Audit)

# Restoration Plan and Insurance Assess both depend on Forensic Audit, concurrent with each other
root.order.add_edge(Forensic_Audit, Restoration_Plan)
root.order.add_edge(Forensic_Audit, Insurance_Assess)

# Customs Clear and Transport Arrange depend on both Restoration Plan and Insurance Assess
root.order.add_edge(Restoration_Plan, Customs_Clear)
root.order.add_edge(Insurance_Assess, Customs_Clear)
root.order.add_edge(Restoration_Plan, Transport_Arrange)
root.order.add_edge(Insurance_Assess, Transport_Arrange)

# Documentation depends on Customs Clear and Transport Arrange
root.order.add_edge(Customs_Clear, Documentation)
root.order.add_edge(Transport_Arrange, Documentation)

# Repatriate Asset depends on Documentation
root.order.add_edge(Documentation, Repatriate_Asset)

# Final Report depends on Repatriate Asset
root.order.add_edge(Repatriate_Asset, Final_Report)