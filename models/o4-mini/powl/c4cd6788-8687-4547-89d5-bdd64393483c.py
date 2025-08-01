# Generated from: c4cd6788-8687-4547-89d5-bdd64393483c.json
# Description: This process involves the identification, negotiation, verification, transportation, and legal transfer of cultural artifacts from foreign institutions back to their countries of origin. It requires interdisciplinary coordination between historians, legal experts, logistics teams, government agencies, and indigenous communities to ensure ethical handling, proper documentation, and compliance with international laws. Activities include provenance research, diplomatic outreach, condition assessment, customs clearance, and final integration into local museums or cultural centers. The process demands sensitivity to cultural heritage and often involves conflict resolution and public communication.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
artifact_research   = Transition(label="Artifact Research")
ownership_verify    = Transition(label="Ownership Verify")
stakeholder_meet    = Transition(label="Stakeholder Meet")
diplomatic_contact  = Transition(label="Diplomatic Contact")
legal_review        = Transition(label="Legal Review")
condition_report    = Transition(label="Condition Report")
transport_plan      = Transition(label="Transport Plan")
insurance_setup     = Transition(label="Insurance Setup")
secure_packaging    = Transition(label="Secure Packaging")
customs_clear       = Transition(label="Customs Clear")
shipping_monitor    = Transition(label="Shipping Monitor")
arrival_inspect     = Transition(label="Arrival Inspect")
exhibit_prepare     = Transition(label="Exhibit Prepare")
community_brief     = Transition(label="Community Brief")
public_release      = Transition(label="Public Release")

# Build the negotiation/verification loop:
#   * ( Aneg , stakeholder_meet )
# where Aneg = Diplomatic Contact -> Legal Review
Aneg = StrictPartialOrder(nodes=[diplomatic_contact, legal_review])
Aneg.order.add_edge(diplomatic_contact, legal_review)
negotiation_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Aneg, stakeholder_meet]
)

# Assemble the top‐level partial order
root = StrictPartialOrder(nodes=[
    artifact_research,
    ownership_verify,
    stakeholder_meet,
    negotiation_loop,
    condition_report,
    transport_plan,
    insurance_setup,
    secure_packaging,
    customs_clear,
    shipping_monitor,
    arrival_inspect,
    exhibit_prepare,
    community_brief,
    public_release
])

# Sequencing edges before the loop
root.order.add_edge(artifact_research, ownership_verify)
root.order.add_edge(ownership_verify, stakeholder_meet)
root.order.add_edge(stakeholder_meet, negotiation_loop)

# After the negotiation loop: condition assessment, transport planning,
# insurance setup can proceed in parallel
for t in [condition_report, transport_plan, insurance_setup]:
    root.order.add_edge(negotiation_loop, t)

# These three must all complete before secure packaging
for t in [condition_report, transport_plan, insurance_setup]:
    root.order.add_edge(t, secure_packaging)

# Shipping sequence
root.order.add_edge(secure_packaging, customs_clear)
root.order.add_edge(customs_clear, shipping_monitor)

# Arrival, unpacking, exhibit preparation, community briefing, and release
root.order.add_edge(shipping_monitor, arrival_inspect)
root.order.add_edge(arrival_inspect, exhibit_prepare)
root.order.add_edge(exhibit_prepare, community_brief)
root.order.add_edge(community_brief, public_release)