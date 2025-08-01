# Generated from: 8a7ec494-47d6-4209-a0b7-b341c12d124d.json
# Description: This process involves the detailed verification and authentication of rare cultural artifacts acquired from private collectors before integration into a museum's permanent collection. It includes provenance research, chemical composition analysis, expert consultation, legal clearance, and digital archiving. Each step ensures the artifact's authenticity, legal ownership, and preservation readiness. The process also entails coordinating with international agencies for cross-border compliance, preparing detailed reports, and managing secure transportation logistics. Finally, the artifact is digitally cataloged with 3D imaging and metadata tagging for future research and public accessibility.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities
Provenance_Check = Transition(label='Provenance Check')
Material_Testing = Transition(label='Material Testing')
Expert_Review = Transition(label='Expert Review')
Legal_Clearance = Transition(label='Legal Clearance')
Customs_Filing = Transition(label='Customs Filing')
Transport_Booking = Transition(label='Transport Booking')
Condition_Report = Transition(label='Condition Report')
Digital_Scan = Transition(label='Digital Scan')
Metadata_Tagging = Transition(label='Metadata Tagging')
Security_Audit = Transition(label='Security Audit')
Crosscheck_Database = Transition(label='Crosscheck Database')
Restoration_Plan = Transition(label='Restoration Plan')
Insurance_Setup = Transition(label='Insurance Setup')
Stakeholder_Brief = Transition(label='Stakeholder Brief')
Archive_Upload = Transition(label='Archive Upload')

# Partial order for verification & authentication steps
verification_PO = StrictPartialOrder(nodes=[Provenance_Check, Material_Testing, Expert_Review, Legal_Clearance])
verification_PO.order.add_edge(Provenance_Check, Material_Testing)
verification_PO.order.add_edge(Material_Testing, Expert_Review)
verification_PO.order.add_edge(Expert_Review, Legal_Clearance)

# Partial order for logistics & compliance steps (Customs, Transport, Security)
logistics_PO = StrictPartialOrder(nodes=[Customs_Filing, Transport_Booking, Security_Audit])
# All concurrent, no order edges

# Partial order for reporting and planning (Condition report, restoration, insurance, briefing)
planning_PO = StrictPartialOrder(nodes=[Condition_Report, Restoration_Plan, Insurance_Setup, Stakeholder_Brief])
# No explicit order — concurrent

# Partial order for digital archiving (Crosscheck DB, Digital Scan, Metadata Tagging, Archive Upload)
digital_PO = StrictPartialOrder(nodes=[Crosscheck_Database, Digital_Scan, Metadata_Tagging, Archive_Upload])
digital_PO.order.add_edge(Crosscheck_Database, Digital_Scan)
digital_PO.order.add_edge(Digital_Scan, Metadata_Tagging)
digital_PO.order.add_edge(Metadata_Tagging, Archive_Upload)

# High-level partial order combining all major phases

# Phase 1: verification_PO --> Phase2: logistics_PO --> Phase3: planning_PO --> Phase4: digital_PO
# plus Security_Audit can run concurrently with Transport_Booking in logistics_PO so no edge needed

root = StrictPartialOrder(
    nodes=[verification_PO, logistics_PO, planning_PO, digital_PO]
)

root.order.add_edge(verification_PO, logistics_PO)
root.order.add_edge(logistics_PO, planning_PO)
root.order.add_edge(planning_PO, digital_PO)