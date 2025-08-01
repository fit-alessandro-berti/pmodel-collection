# Generated from: 70624408-facb-430b-a4eb-811971596dbd.json
# Description: This process involves locating, authenticating, and reclaiming lost or stolen corporate artifacts that hold significant historical or strategic value. It combines legal research, field investigation, negotiation with private collectors, and coordination with law enforcement agencies. The process demands careful documentation, risk assessment, and strategic communication to ensure successful recovery while preserving corporate reputation and avoiding legal pitfalls. Multiple stakeholders including legal, security, PR, and executive teams collaborate to track provenance, validate ownership, and secure transfer agreements in compliance with international laws. The final phase includes artifact restoration and integration into corporate heritage or museum collections, followed by public relations campaigns to highlight the recovery success.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define Activities
Initiate_Request = Transition(label='Initiate Request')

Legal_Review = Transition(label='Legal Review')
Historical_Audit = Transition(label='Historical Audit')

Provenance_Check = Transition(label='Provenance Check')

Field_Investigation = Transition(label='Field Investigation')
Stakeholder_Map = Transition(label='Stakeholder Map')
Risk_Assessment = Transition(label='Risk Assessment')

Collector_Contact = Transition(label='Collector Contact')
Negotiation_Phase = Transition(label='Negotiation Phase')

Law_Enforcement = Transition(label='Law Enforcement')

Ownership_Validation = Transition(label='Ownership Validation')
Transfer_Agreement = Transition(label='Transfer Agreement')

Artifact_Transport = Transition(label='Artifact Transport')

Restoration_Work = Transition(label='Restoration Work')

PR_Campaign = Transition(label='PR Campaign')
Final_Reporting = Transition(label='Final Reporting')

# Partial order representing parallel activities Legal Review and Historical Audit after Initiate Request
legal_historical = StrictPartialOrder(nodes=[Legal_Review, Historical_Audit])

# Provenance Check after both Legal Review and Historical Audit (join)
provenance_check_po = StrictPartialOrder(
    nodes=[legal_historical, Provenance_Check],
    # legal_historical's nodes are inside, so edges from both Legal and Historical go to Provenance_Check
)
# We will create explicit edges after assembling all nodes.

# Parallel execution: Field Investigation, Stakeholder Map, Risk Assessment after Provenance Check
field_stake_risk = StrictPartialOrder(nodes=[Field_Investigation, Stakeholder_Map, Risk_Assessment])

# Parallel execution: Collector Contact and Negotiation Phase
collector_negotiation = StrictPartialOrder(nodes=[Collector_Contact, Negotiation_Phase])

# Negotiation and Law Enforcement precede Ownership Validation and Transfer Agreement
negotiation_law = StrictPartialOrder(nodes=[collector_negotiation, Law_Enforcement])

ownership_transfer = StrictPartialOrder(nodes=[Ownership_Validation, Transfer_Agreement])

# Transport and Restoration after Ownership and Transfer
artifact_restoration = StrictPartialOrder(nodes=[Artifact_Transport, Restoration_Work])

# PR Campaign and Final Reporting after Restoration
pr_final = StrictPartialOrder(nodes=[PR_Campaign, Final_Reporting])

# Assemble the whole process as a large partial order including all nodes and edges

# Collect all individual transitions (flatten nodes)
# Because we embed POWL models inside POs, flatten nodes for root PO

# Define all atomic nodes
all_activities = [
    Initiate_Request,
    Legal_Review, Historical_Audit,
    Provenance_Check,
    Field_Investigation, Stakeholder_Map, Risk_Assessment,
    Collector_Contact, Negotiation_Phase,
    Law_Enforcement,
    Ownership_Validation, Transfer_Agreement,
    Artifact_Transport, Restoration_Work,
    PR_Campaign, Final_Reporting
]

root = StrictPartialOrder(nodes=all_activities)

# Add edges following process description

# Initiate Request --> Legal Review and Historical Audit (parallel after Initiate)
root.order.add_edge(Initiate_Request, Legal_Review)
root.order.add_edge(Initiate_Request, Historical_Audit)

# Legal Review and Historical Audit --> Provenance Check (join)
root.order.add_edge(Legal_Review, Provenance_Check)
root.order.add_edge(Historical_Audit, Provenance_Check)

# Provenance Check --> Field Investigation, Stakeholder Map, Risk Assessment (all concurrent)
root.order.add_edge(Provenance_Check, Field_Investigation)
root.order.add_edge(Provenance_Check, Stakeholder_Map)
root.order.add_edge(Provenance_Check, Risk_Assessment)

# Field Investigation, Stakeholder Map, Risk Assessment --> Collector Contact and Negotiation Phase
root.order.add_edge(Field_Investigation, Collector_Contact)
root.order.add_edge(Stakeholder_Map, Collector_Contact)
root.order.add_edge(Risk_Assessment, Collector_Contact)

root.order.add_edge(Field_Investigation, Negotiation_Phase)
root.order.add_edge(Stakeholder_Map, Negotiation_Phase)
root.order.add_edge(Risk_Assessment, Negotiation_Phase)

# Collector Contact and Negotiation Phase --> Law Enforcement (parallel)
root.order.add_edge(Collector_Contact, Law_Enforcement)
root.order.add_edge(Negotiation_Phase, Law_Enforcement)

# Law Enforcement --> Ownership Validation and Transfer Agreement (both parallel)
root.order.add_edge(Law_Enforcement, Ownership_Validation)
root.order.add_edge(Law_Enforcement, Transfer_Agreement)

# Ownership Validation and Transfer Agreement --> Artifact Transport (both must complete before transport)
root.order.add_edge(Ownership_Validation, Artifact_Transport)
root.order.add_edge(Transfer_Agreement, Artifact_Transport)

# Artifact Transport --> Restoration Work
root.order.add_edge(Artifact_Transport, Restoration_Work)

# Restoration Work --> PR Campaign
root.order.add_edge(Restoration_Work, PR_Campaign)

# PR Campaign --> Final Reporting
root.order.add_edge(PR_Campaign, Final_Reporting)