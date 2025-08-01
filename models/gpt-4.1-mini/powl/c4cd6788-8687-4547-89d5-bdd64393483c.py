# Generated from: c4cd6788-8687-4547-89d5-bdd64393483c.json
# Description: This process involves the identification, negotiation, verification, transportation, and legal transfer of cultural artifacts from foreign institutions back to their countries of origin. It requires interdisciplinary coordination between historians, legal experts, logistics teams, government agencies, and indigenous communities to ensure ethical handling, proper documentation, and compliance with international laws. Activities include provenance research, diplomatic outreach, condition assessment, customs clearance, and final integration into local museums or cultural centers. The process demands sensitivity to cultural heritage and often involves conflict resolution and public communication.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the main activities as transitions
Artifact_Research = Transition(label='Artifact Research')
Ownership_Verify = Transition(label='Ownership Verify')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Legal_Review = Transition(label='Legal Review')
Diplomatic_Contact = Transition(label='Diplomatic Contact')
Condition_Report = Transition(label='Condition Report')
Transport_Plan = Transition(label='Transport Plan')
Insurance_Setup = Transition(label='Insurance Setup')
Customs_Clear = Transition(label='Customs Clear')
Secure_Packaging = Transition(label='Secure Packaging')
Shipping_Monitor = Transition(label='Shipping Monitor')
Community_Brief = Transition(label='Community Brief')
Arrival_Inspect = Transition(label='Arrival Inspect')
Exhibit_Prepare = Transition(label='Exhibit Prepare')
Public_Release = Transition(label='Public Release')

# Model conflict resolution and public communication as a choice:
# Either Community_Brief or Public_Release first? 
# Better assumption: Community_Brief and Public_Release are sequential after Exhibit_Prepare but can incorporate minor choices inside Community_Brief?
# Since description mentions 'often involves conflict resolution and public communication' that 'often involves' => we can model it as an XOR (exclusive choice) before public release.
# Let's assume 'Community_Brief' and 'Public_Release' happen in order and the conflict resolution (silent tau) is handled internally and is implicit.

# Build partial order:

# Create the main chain start:
# Identification: Artifact Research
# Negotiation and verification: Ownership Verify, Stakeholder Meet, Legal Review, Diplomatic Contact
# Condition assessment and logistic planning: Condition Report, Transport Plan, Insurance Setup
# Transport and customs: Secure Packaging, Customs Clear, Shipping Monitor
# Arrival and final integration: Arrival Inspect, Exhibit Prepare
# Communication: Community Brief, Public Release

# For interdisciplinary coordination, some activities are concurrent where possible:
# Stakeholder Meet and Legal Review can be concurrent
# Transport Plan and Insurance Setup can be concurrent and after Condition Report
# Secure Packaging depends on Transport Plan and Insurance Setup
# Customs Clear depends on Secure Packaging
# Shipping Monitor depends on Customs Clear
# Community Brief can be concurrent or after Arrival Inspect
# Exhibit Prepare depends on Arrival Inspect
# Public Release after Exhibit Prepare and Community Brief

# Construct concurrency and ordering accordingly:

# To implement concurrency, use StrictPartialOrder with multiple nodes and edges

nodes = [
    Artifact_Research,
    Ownership_Verify,
    Stakeholder_Meet,
    Legal_Review,
    Diplomatic_Contact,
    Condition_Report,
    Transport_Plan,
    Insurance_Setup,
    Secure_Packaging,
    Customs_Clear,
    Shipping_Monitor,
    Community_Brief,
    Arrival_Inspect,
    Exhibit_Prepare,
    Public_Release
]

root = StrictPartialOrder(nodes=nodes)

# Artifact Research -> Ownership Verify
root.order.add_edge(Artifact_Research, Ownership_Verify)

# Ownership Verify -> Stakeholder Meet and Legal Review and Diplomatic Contact in parallel
root.order.add_edge(Ownership_Verify, Stakeholder_Meet)
root.order.add_edge(Ownership_Verify, Legal_Review)
root.order.add_edge(Ownership_Verify, Diplomatic_Contact)

# After Stakeholder Meet, Legal Review and Diplomatic Contact complete, Condition Report can start
# So Condition Report depends on all three:
root.order.add_edge(Stakeholder_Meet, Condition_Report)
root.order.add_edge(Legal_Review, Condition_Report)
root.order.add_edge(Diplomatic_Contact, Condition_Report)

# After Condition Report, Transport Plan and Insurance Setup can be done concurrently
root.order.add_edge(Condition_Report, Transport_Plan)
root.order.add_edge(Condition_Report, Insurance_Setup)

# After Transport Plan and Insurance Setup, Secure Packaging can occur
root.order.add_edge(Transport_Plan, Secure_Packaging)
root.order.add_edge(Insurance_Setup, Secure_Packaging)

# Secure Packaging -> Customs Clear -> Shipping Monitor
root.order.add_edge(Secure_Packaging, Customs_Clear)
root.order.add_edge(Customs_Clear, Shipping_Monitor)

# Arrival Inspect depends on Shipping Monitor
root.order.add_edge(Shipping_Monitor, Arrival_Inspect)

# Exhibit Prepare depends on Arrival Inspect
root.order.add_edge(Arrival_Inspect, Exhibit_Prepare)

# Community Brief depends on Arrival Inspect (can run concurrently with Exhibit Prepare)
root.order.add_edge(Arrival_Inspect, Community_Brief)

# Public Release depends on both Exhibit Prepare and Community Brief
root.order.add_edge(Exhibit_Prepare, Public_Release)
root.order.add_edge(Community_Brief, Public_Release)