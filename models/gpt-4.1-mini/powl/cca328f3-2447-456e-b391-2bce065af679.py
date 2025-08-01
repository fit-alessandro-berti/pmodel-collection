# Generated from: cca328f3-2447-456e-b391-2bce065af679.json
# Description: This process involves the thorough evaluation and verification of historical artifacts in a museum setting. It starts with initial artifact intake, followed by detailed provenance research, material composition analysis using advanced spectroscopy, and stylistic comparison against known samples. Concurrently, digital imaging captures high-resolution visuals for documentation. Expert consultations are arranged to assess cultural significance and authenticity. The process includes cross-referencing with global artifact databases and legal compliance checks regarding ownership and export laws. After synthesis of all data, a final authenticity report is prepared, archived, and the artifact is either approved for display, returned to the lender, or flagged for further investigation. This atypical process requires coordination across departments including curators, scientists, legal advisors, and archivists, ensuring comprehensive and credible authentication outcomes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
Artifact_Intake = Transition(label='Artifact Intake')

Provenance_Check = Transition(label='Provenance Check')
Material_Scan = Transition(label='Material Scan')
Style_Compare = Transition(label='Style Compare')

Digital_Capture = Transition(label='Digital Capture')

Expert_Review = Transition(label='Expert Review')

Database_Search = Transition(label='Database Search')
Legal_Audit = Transition(label='Legal Audit')
Cultural_Assess = Transition(label='Cultural Assess')

Data_Synthesis = Transition(label='Data Synthesis')

Report_Draft = Transition(label='Report Draft')
Archival_Store = Transition(label='Archival Store')

Display_Approve = Transition(label='Display Approve')
Lender_Notify = Transition(label='Lender Notify')
Investigation_Flag = Transition(label='Investigation Flag')

# Step 1: After Artifact Intake, the core research (Provenance Check, Material Scan, Style Compare) occurs in sequence
core_research = StrictPartialOrder(nodes=[Provenance_Check, Material_Scan, Style_Compare])
# order them linearly: Provenance --> Material --> Style
core_research.order.add_edge(Provenance_Check, Material_Scan)
core_research.order.add_edge(Material_Scan, Style_Compare)

# Step 2: Concurrently with core research, Digital Capture occurs
# So create a PO combining core_research and Digital_Capture as concurrent
research_and_capture = StrictPartialOrder(nodes=[core_research, Digital_Capture])
# no edges between them => concurrent

# Step 3: Then Expert Review happens after both core research and digital capture completed
expert_review_phase = StrictPartialOrder(
    nodes=[research_and_capture, Expert_Review]
)
expert_review_phase.order.add_edge(research_and_capture, Expert_Review)

# Step 4: After Expert Review, three parallel (concurrent) activities:
# Database Search, Legal Audit, Cultural Assess
cross_ref_checks = StrictPartialOrder(
    nodes=[Database_Search, Legal_Audit, Cultural_Assess]
)
# no order edges => fully concurrent

# Step 5: After cross referencing, Data Synthesis
data_analysis_phase = StrictPartialOrder(
    nodes=[cross_ref_checks, Data_Synthesis]
)
data_analysis_phase.order.add_edge(cross_ref_checks, Data_Synthesis)

# Step 6: Then Report Draft and Archival Store concurrently
report_and_archive = StrictPartialOrder(
    nodes=[Report_Draft, Archival_Store]
)
# no edges => concurrent

# Step 7: After report and archive, a choice of final outcomes:
# Display Approve OR Lender Notify OR Investigation Flag
final_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[Display_Approve, Lender_Notify, Investigation_Flag]
)

# Step 8: Compose the final straight sequence:
# Artifact Intake -> (core research || Digital Capture)
# -> Expert Review
# -> (Database Search || Legal Audit || Cultural Assess)
# -> Data Synthesis
# -> (Report Draft || Archival Store)
# -> final choice

root = StrictPartialOrder(
    nodes=[
        Artifact_Intake,
        research_and_capture,
        Expert_Review,
        cross_ref_checks,
        Data_Synthesis,
        report_and_archive,
        final_choice,
    ]
)

root.order.add_edge(Artifact_Intake, research_and_capture)
root.order.add_edge(research_and_capture, Expert_Review)
root.order.add_edge(Expert_Review, cross_ref_checks)
root.order.add_edge(cross_ref_checks, Data_Synthesis)
root.order.add_edge(Data_Synthesis, report_and_archive)
root.order.add_edge(report_and_archive, final_choice)