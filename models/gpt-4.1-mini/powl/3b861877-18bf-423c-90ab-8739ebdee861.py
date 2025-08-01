# Generated from: 3b861877-18bf-423c-90ab-8739ebdee861.json
# Description: This process involves locating, authenticating, and repatriating corporate artifacts lost or stolen during historical mergers and acquisitions. It begins with artifact identification using archival research, followed by stakeholder interviews to verify provenance. Legal consultations ensure compliance with international ownership laws. Next, covert negotiations with current holders are conducted to facilitate return agreements. Logistics planning addresses secure transport and customs clearance. Finally, artifacts are restored, cataloged, and integrated into corporate heritage exhibits to preserve brand legacy and employee engagement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Artifact_ID = Transition(label='Artifact ID')
Archival_Scan = Transition(label='Archival Scan')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Provenance_Check = Transition(label='Provenance Check')
Legal_Review = Transition(label='Legal Review')
Ownership_Audit = Transition(label='Ownership Audit')
Negotiation_Prep = Transition(label='Negotiation Prep')
Stakeholder_Contact = Transition(label='Stakeholder Contact')
Agreement_Draft = Transition(label='Agreement Draft')
Transport_Plan = Transition(label='Transport Plan')
Customs_Clear = Transition(label='Customs Clear')
Artifact_Restore = Transition(label='Artifact Restore')
Catalog_Entry = Transition(label='Catalog Entry')
Exhibit_Setup = Transition(label='Exhibit Setup')
Legacy_Report = Transition(label='Legacy Report')

# Step 1: Artifact ID + Archival Scan (concurrent or sequential?)
# Description says "begins with artifact identification using archival research"
# I interpret this as Artifact ID then Archival Scan
# Then Stakeholder interviews to verify provenance
# Which includes Stakeholder Meet and Provenance Check (sequential)
# Legal Consultations: Legal Review, Ownership Audit (concurrent)
# Covert negotiations: Negotiation Prep, Stakeholder Contact, Agreement Draft (sequential)
# Logistics planning: Transport Plan, Customs Clear (sequential)
# Final: restore, catalog, exhibit, legacy report (concurrent or sequential?)
# Description says restored, cataloged, and integrated - sounds sequential

# Compose initial sequence:
initial_seq = StrictPartialOrder(nodes=[Artifact_ID, Archival_Scan, Stakeholder_Meet, Provenance_Check])
initial_seq.order.add_edge(Artifact_ID, Archival_Scan)
initial_seq.order.add_edge(Archival_Scan, Stakeholder_Meet)
initial_seq.order.add_edge(Stakeholder_Meet, Provenance_Check)

# Legal consultations: Legal Review and Ownership Audit concurrent
legal_consult = StrictPartialOrder(nodes=[Legal_Review, Ownership_Audit])
# no order → concurrent

# Negotiations sequential:
negotiations = StrictPartialOrder(nodes=[Negotiation_Prep, Stakeholder_Contact, Agreement_Draft])
negotiations.order.add_edge(Negotiation_Prep, Stakeholder_Contact)
negotiations.order.add_edge(Stakeholder_Contact, Agreement_Draft)

# Logistics sequential:
logistics = StrictPartialOrder(nodes=[Transport_Plan, Customs_Clear])
logistics.order.add_edge(Transport_Plan, Customs_Clear)

# Final restoration sequence:
restoration_seq = StrictPartialOrder(nodes=[Artifact_Restore, Catalog_Entry, Exhibit_Setup, Legacy_Report])
restoration_seq.order.add_edge(Artifact_Restore, Catalog_Entry)
restoration_seq.order.add_edge(Catalog_Entry, Exhibit_Setup)
restoration_seq.order.add_edge(Exhibit_Setup, Legacy_Report)

# Combine legal consultations and negotiations (legal before negotiations?)
# Description: "Legal consultations ensure compliance" before "covert negotiations"
legal_to_negotiations = StrictPartialOrder(
    nodes=[legal_consult, negotiations]
)
legal_to_negotiations.order.add_edge(legal_consult, negotiations)

# Combine logistics and final restoration (logistics before restoration)
logistics_to_restoration = StrictPartialOrder(
    nodes=[logistics, restoration_seq]
)
logistics_to_restoration.order.add_edge(logistics, restoration_seq)

# Combine all major parts in sequence:
# initial_seq -> legal_to_negotiations -> logistics_to_restoration
root = StrictPartialOrder(
    nodes=[initial_seq, legal_to_negotiations, logistics_to_restoration]
)
root.order.add_edge(initial_seq, legal_to_negotiations)
root.order.add_edge(legal_to_negotiations, logistics_to_restoration)