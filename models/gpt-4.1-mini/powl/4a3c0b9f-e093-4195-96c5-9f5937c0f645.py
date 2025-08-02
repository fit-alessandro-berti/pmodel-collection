# Generated from: 4a3c0b9f-e093-4195-96c5-9f5937c0f645.json
# Description: This process involves the complex verification and authentication of ancient artifacts crossing international borders. It includes multi-disciplinary collaboration between historians, customs officials, forensic analysts, and legal experts to ensure provenance accuracy, compliance with cultural heritage laws, and secure transportation. The procedure requires detailed historical research, chemical composition analysis, photographic documentation, legal clearance, and diplomatic coordination to prevent illicit trafficking and preserve cultural integrity. Each step is critical to validate authenticity, legality, and safe delivery to museums or private collectors while respecting international treaties and ethical standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transition objects
Artifact_Logging = Transition(label='Artifact Logging')
Historical_Review = Transition(label='Historical Review')
Customs_Check = Transition(label='Customs Check')
Chemical_Scan = Transition(label='Chemical Scan')
Provenance_Match = Transition(label='Provenance Match')
Photo_Capture = Transition(label='Photo Capture')
Legal_Review = Transition(label='Legal Review')
Diplomatic_Notify = Transition(label='Diplomatic Notify')
Security_Clear = Transition(label='Security Clear')
Transport_Arrange = Transition(label='Transport Arrange')
Condition_Report = Transition(label='Condition Report')
Data_Archiving = Transition(label='Data Archiving')
Stakeholder_Update = Transition(label='Stakeholder Update')
Final_Approval = Transition(label='Final Approval')
Delivery_Confirm = Transition(label='Delivery Confirm')

# Model explanation and assumptions for partial order and control flow:
# 1) Artifact Logging is first.
# 2) Historical Review and Customs Check run concurrently after Artifact Logging.
# 3) Chemical Scan happens after Customs Check.
# 4) Provenance Match after Historical Review and Chemical Scan.
# 5) Photo Capture parallel with Legal Review after Provenance Match.
# 6) Diplomatic Notify after Legal Review.
# 7) Security Clear after Customs Check.
# 8) Transport Arrange after Security Clear and Diplomatic Notify.
# 9) Condition Report and Data Archiving can run concurrently after Transport Arrange.
# 10) Stakeholder Update after Data Archiving.
# 11) Final Approval after Stakeholder Update and Condition Report.
# 12) Delivery Confirm last.

# Construct partial order nodes
nodes = [
    Artifact_Logging,
    Historical_Review,
    Customs_Check,
    Chemical_Scan,
    Provenance_Match,
    Photo_Capture,
    Legal_Review,
    Diplomatic_Notify,
    Security_Clear,
    Transport_Arrange,
    Condition_Report,
    Data_Archiving,
    Stakeholder_Update,
    Final_Approval,
    Delivery_Confirm
]

# Create StrictPartialOrder
root = StrictPartialOrder(nodes=nodes)

# Define order edges according to assumptions:

# 1
root.order.add_edge(Artifact_Logging, Historical_Review)
root.order.add_edge(Artifact_Logging, Customs_Check)

# 2
root.order.add_edge(Customs_Check, Chemical_Scan)

# 3 Provenance Match requires Historical Review and Chemical Scan
root.order.add_edge(Historical_Review, Provenance_Match)
root.order.add_edge(Chemical_Scan, Provenance_Match)

# 4 Photo Capture and Legal Review after Provenance Match
root.order.add_edge(Provenance_Match, Photo_Capture)
root.order.add_edge(Provenance_Match, Legal_Review)

# 5 Diplomatic Notify after Legal Review
root.order.add_edge(Legal_Review, Diplomatic_Notify)

# 6 Security Clear after Customs Check
root.order.add_edge(Customs_Check, Security_Clear)

# 7 Transport Arrange after Security Clear and Diplomatic Notify
root.order.add_edge(Security_Clear, Transport_Arrange)
root.order.add_edge(Diplomatic_Notify, Transport_Arrange)

# 8 Condition Report and Data Archiving after Transport Arrange
root.order.add_edge(Transport_Arrange, Condition_Report)
root.order.add_edge(Transport_Arrange, Data_Archiving)

# 9 Stakeholder Update after Data Archiving
root.order.add_edge(Data_Archiving, Stakeholder_Update)

# 10 Final Approval after Stakeholder Update and Condition Report
root.order.add_edge(Stakeholder_Update, Final_Approval)
root.order.add_edge(Condition_Report, Final_Approval)

# 11 Delivery Confirm after Final Approval
root.order.add_edge(Final_Approval, Delivery_Confirm)