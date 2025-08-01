# Generated from: b8cdaeba-0004-4dcd-b3db-03f6c89616a1.json
# Description: This process governs the acquisition, authentication, preservation, and exchange of rare cultural artifacts between international museums and private collectors. It involves multi-layered verification steps including provenance research, scientific testing, and diplomatic clearance. The process ensures legal compliance with cultural heritage laws, ethical considerations, and optimal preservation methodologies. Stakeholders coordinate through multiple channels to negotiate terms, arrange secure transportation, and manage insurance policies. Additionally, public exhibition planning and educational outreach are integrated to maximize cultural impact and accessibility while respecting ownership rights and international treaties.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
Artifact_Sourcing = Transition(label='Artifact Sourcing')
Provenance_Check = Transition(label='Provenance Check')
Scientific_Test = Transition(label='Scientific Test')
Legal_Review = Transition(label='Legal Review')
Ethics_Approval = Transition(label='Ethics Approval')
Owner_Negotiation = Transition(label='Owner Negotiation')
Diplomatic_Clear = Transition(label='Diplomatic Clear')
Contract_Draft = Transition(label='Contract Draft')
Insurance_Setup = Transition(label='Insurance Setup')
Secure_Transit = Transition(label='Secure Transit')
Condition_Report = Transition(label='Condition Report')
Preservation_Plan = Transition(label='Preservation Plan')
Exhibit_Design = Transition(label='Exhibit Design')
Public_Outreach = Transition(label='Public Outreach')
Ownership_Transfer = Transition(label='Ownership Transfer')
Compliance_Audit = Transition(label='Compliance Audit')
Feedback_Collect = Transition(label='Feedback Collect')
skip = SilentTransition()

# Verification sub-process: Provenance_Check and Scientific_Test concur after Artifact_Sourcing
verification = StrictPartialOrder(
    nodes=[Provenance_Check, Scientific_Test]
)  # concurrent verification steps
# No order edges: concurrent

# After verification, legal and ethical checks in parallel
legal_ethics = StrictPartialOrder(
    nodes=[Legal_Review, Ethics_Approval]
)  # concurrent

# Negotiation step after legal and ethics
negotiation = OperatorPOWL(
    operator=Operator.XOR,
    children=[
        Owner_Negotiation,
        # Possibly skip negotiation - using skip to model choice here
        skip
    ]
)

# Diplomatic clearance after negotiation (possibly after skip the same)
diplomatic_and_contract = StrictPartialOrder(
    nodes=[Diplomatic_Clear, Contract_Draft]
)
diplomatic_and_contract.order.add_edge(Diplomatic_Clear, Contract_Draft)

# Insurance and secure transit parallel after contract draft
insurance_transit = StrictPartialOrder(
    nodes=[Insurance_Setup, Secure_Transit]
)
# concurrent, no order edges

# Condition report and preservation plan after transit
condition_preservation = StrictPartialOrder(
    nodes=[Condition_Report, Preservation_Plan]
)
# concurrent

# Exhibition planning and public outreach concurrent after preservation
exhibit_public = StrictPartialOrder(
    nodes=[Exhibit_Design, Public_Outreach]
)
# concurrent

# Ownership transfer after negotiation and contracts
ownership_transfer = Ownership_Transfer

# Compliance audit and feedback collection are looped after ownership transfer to ensure continuous improvement
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        Compliance_Audit,
        Feedback_Collect
    ]
)

# Model the process flow

# Base PO from Artifact_Sourcing, verification, legal_ethics, negotiation
po1 = StrictPartialOrder(
    nodes=[Artifact_Sourcing, verification, legal_ethics, negotiation]
)
po1.order.add_edge(Artifact_Sourcing, verification)
po1.order.add_edge(verification, legal_ethics)
po1.order.add_edge(legal_ethics, negotiation)

# Diplomatic and contract after negotiation
po2 = StrictPartialOrder(
    nodes=[po1, diplomatic_and_contract]
)
po2.order.add_edge(po1, diplomatic_and_contract)

# Insurance and transit after contract
po3 = StrictPartialOrder(
    nodes=[po2, insurance_transit]
)
po3.order.add_edge(po2, insurance_transit)

# Condition report and preservation plan after transit
po4 = StrictPartialOrder(
    nodes=[po3, condition_preservation]
)
po4.order.add_edge(po3, condition_preservation)

# Exhibition and outreach after preservation
po5 = StrictPartialOrder(
    nodes=[po4, exhibit_public]
)
po5.order.add_edge(po4, exhibit_public)

# Ownership transfer after exhibition and outreach (both must finish)
po6 = StrictPartialOrder(
    nodes=[po5, ownership_transfer]
)
po6.order.add_edge(po5, ownership_transfer)

# Loop on compliance audit and feedback after ownership transfer
po7 = StrictPartialOrder(
    nodes=[po6, loop]
)
po7.order.add_edge(po6, loop)

root = po7