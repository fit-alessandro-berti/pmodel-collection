# Generated from: c5f0a079-007a-4dae-a48d-afa9f04a238e.json
# Description: This process involves the intricate steps required to authenticate rare historical artifacts. It begins with initial provenance research followed by material composition analysis using advanced spectrometry. Specialists then conduct microscopic wear pattern examination to identify inconsistencies. Concurrently, digital imaging captures high-resolution details for pattern matching against known databases. Legal verification ensures ownership legitimacy, while ethical committees assess cultural sensitivity. The artifact undergoes carbon dating to confirm age, and restoration experts evaluate preservation needs. Finally, a comprehensive report is compiled, reviewed by multiple stakeholders, and archived securely for future reference and public exhibition approval.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Provenance_Check = Transition(label='Provenance Check')
Material_Scan = Transition(label='Material Scan')
Wear_Analysis = Transition(label='Wear Analysis')
Image_Capture = Transition(label='Image Capture')
Pattern_Match = Transition(label='Pattern Match')
Ownership_Verify = Transition(label='Ownership Verify')
Ethics_Review = Transition(label='Ethics Review')
Carbon_Dating = Transition(label='Carbon Dating')
Restoration_Eval = Transition(label='Restoration Eval')
Report_Draft = Transition(label='Report Draft')
Stakeholder_Review = Transition(label='Stakeholder Review')
Archive_Data = Transition(label='Archive Data')
Exhibit_Approve = Transition(label='Exhibit Approve')
Condition_Monitor = Transition(label='Condition Monitor')
Final_Certification = Transition(label='Final Certification')

# Material Scan -> Wear Analysis and concurrent digital imaging & pattern matching
# Concurrent Image Capture and Pattern Match (Image Capture --> Pattern Match)
image_pattern_PO = StrictPartialOrder(nodes=[Image_Capture, Pattern_Match])
image_pattern_PO.order.add_edge(Image_Capture, Pattern_Match)

# Concurrent Legal and Ethics checks (Ownership Verify and Ethics Review concurrent)
legal_ethics_PO = StrictPartialOrder(nodes=[Ownership_Verify, Ethics_Review])

# Concurrent Carbon Dating and Restoration Evaluation
carbon_restoration_PO = StrictPartialOrder(nodes=[Carbon_Dating, Restoration_Eval])

# Report process sequence: Report Draft --> Stakeholder Review --> Archive Data --> Exhibit Approve
report_PO = StrictPartialOrder(nodes=[Report_Draft, Stakeholder_Review, Archive_Data, Exhibit_Approve])
report_PO.order.add_edge(Report_Draft, Stakeholder_Review)
report_PO.order.add_edge(Stakeholder_Review, Archive_Data)
report_PO.order.add_edge(Archive_Data, Exhibit_Approve)

# Main partial order combining all steps with respective dependencies.

# Start: Provenance Check --> Material Scan
# Material Scan --> Wear Analysis and concurrently image_pattern_PO
# Wear Analysis and image_pattern_PO must both complete before continuing to Ownership Verify and Ethics Review
# Then concurrent carbon_restoration_PO
# Then the report_PO
# After report_PO, Condition Monitor and Final Certification are concurrent with order: Condition Monitor --> Final Certification

# Combine Ownership_Verify and Ethics_Review concurrent
ownership_ethics_PO = legal_ethics_PO

# Combine Carbon Dating and Restoration Eval concurrent
carbon_restoration_PO = carbon_restoration_PO

# Condition Monitor --> Final Certification
condition_final_PO = StrictPartialOrder(nodes=[Condition_Monitor, Final_Certification])
condition_final_PO.order.add_edge(Condition_Monitor, Final_Certification)

# Combine all nodes
nodes_all = [
    Provenance_Check,
    Material_Scan,
    Wear_Analysis,
    image_pattern_PO,
    ownership_ethics_PO,
    carbon_restoration_PO,
    report_PO,
    condition_final_PO
]

root = StrictPartialOrder(nodes=nodes_all)

# Define ordering edges:

# Provenance Check --> Material Scan
root.order.add_edge(Provenance_Check, Material_Scan)
# Material Scan --> Wear Analysis
root.order.add_edge(Material_Scan, Wear_Analysis)
# Material Scan --> image_pattern_PO
root.order.add_edge(Material_Scan, image_pattern_PO)

# Wear_Analysis --> ownership_ethics_PO
root.order.add_edge(Wear_Analysis, ownership_ethics_PO)
# image_pattern_PO --> ownership_ethics_PO
root.order.add_edge(image_pattern_PO, ownership_ethics_PO)

# ownership_ethics_PO --> carbon_restoration_PO
root.order.add_edge(ownership_ethics_PO, carbon_restoration_PO)

# carbon_restoration_PO --> report_PO
root.order.add_edge(carbon_restoration_PO, report_PO)

# report_PO --> condition_final_PO
root.order.add_edge(report_PO, condition_final_PO)