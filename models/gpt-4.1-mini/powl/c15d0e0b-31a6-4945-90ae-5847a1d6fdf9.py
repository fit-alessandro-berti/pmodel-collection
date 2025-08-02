# Generated from: c15d0e0b-31a6-4945-90ae-5847a1d6fdf9.json
# Description: This process involves the verification and authentication of rare cultural artifacts before acquisition by a museum. It includes provenance research, material analysis, expert consultations, and digital replication for archival purposes. The process ensures authenticity, legal compliance, and preservation standards while coordinating with international regulatory bodies and insurance providers. Multiple interdisciplinary teams collaborate to mitigate risks and document findings in a secure database, enabling informed decision-making and public transparency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Initial_Review = Transition(label='Initial Review')
Provenance_Check = Transition(label='Provenance Check')
Material_Testing = Transition(label='Material Testing')
Expert_Panel = Transition(label='Expert Panel')
Legal_Audit = Transition(label='Legal Audit')
Insurance_Setup = Transition(label='Insurance Setup')
Digital_Scan = Transition(label='Digital Scan')
Replication_Draft = Transition(label='Replication Draft')
Risk_Assessment = Transition(label='Risk Assessment')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Compliance_Review = Transition(label='Compliance Review')
Archival_Entry = Transition(label='Archival Entry')
Acquisition_Approval = Transition(label='Acquisition Approval')
Transport_Arrange = Transition(label='Transport Arrange')
Condition_Report = Transition(label='Condition Report')
Final_Documentation = Transition(label='Final Documentation')

# Silent transition for optional or internal steps
skip = SilentTransition()

# Partial Order 1: Verification of authenticity and provenance
# Initial Review --> Provenance Check || Material Testing --> Expert Panel
po_verification = StrictPartialOrder(nodes=[
    Initial_Review, Provenance_Check, Material_Testing, Expert_Panel
])
po_verification.order.add_edge(Initial_Review, Provenance_Check)
po_verification.order.add_edge(Initial_Review, Material_Testing)
po_verification.order.add_edge(Provenance_Check, Expert_Panel)
po_verification.order.add_edge(Material_Testing, Expert_Panel)

# Partial Order 2: Legal compliance and insurance setup, concurrent with expertise
po_legal_insurance = StrictPartialOrder(nodes=[Legal_Audit, Insurance_Setup, Risk_Assessment])
po_legal_insurance.order.add_edge(Legal_Audit, Risk_Assessment)
po_legal_insurance.order.add_edge(Insurance_Setup, Risk_Assessment)

# Stakeholder meet and Compliance review in parallel after Risk Assessment
po_stakeholder_compliance = StrictPartialOrder(nodes=[Stakeholder_Meet, Compliance_Review])
# These two are concurrent, no edges needed

# Combine po_legal_insurance and po_stakeholder_compliance
po_compliance = StrictPartialOrder(nodes=[po_legal_insurance, po_stakeholder_compliance])
po_compliance.order.add_edge(po_legal_insurance, po_stakeholder_compliance)

# Partial Order 3: Digital replication and archival
# Digital Scan --> Replication Draft --> Archival Entry
po_replication = StrictPartialOrder(nodes=[Digital_Scan, Replication_Draft, Archival_Entry])
po_replication.order.add_edge(Digital_Scan, Replication_Draft)
po_replication.order.add_edge(Replication_Draft, Archival_Entry)

# Partial Order 4: Final acquisition and transport
po_final = StrictPartialOrder(nodes=[Condition_Report, Acquisition_Approval, Transport_Arrange, Final_Documentation])
po_final.order.add_edge(Condition_Report, Acquisition_Approval)
po_final.order.add_edge(Acquisition_Approval, Transport_Arrange)
po_final.order.add_edge(Transport_Arrange, Final_Documentation)

# Overall partial order
# Root nodes: verification, compliance, replication, final
root = StrictPartialOrder(nodes=[po_verification, po_compliance, po_replication, po_final])
# The final acquisition depends on Archival Entry, Stakeholder Meet and Expert Panel, so:
root.order.add_edge(po_verification, po_final)       # Expert Panel before final steps
root.order.add_edge(po_compliance, po_final)          # Compliance before final steps
root.order.add_edge(po_replication, po_final)          # Archival before final steps

# Additionally, Stakeholder Meet depends on Risk Assessment inside po_compliance
# We already embedded that by adding po_legal_insurance --> po_stakeholder_compliance

# And Risk Assessment depends on Legal Audit and Insurance Setup in po_legal_insurance

# This captures concurrency, dependencies, choices (none explicitly), and loops (none needed here).
