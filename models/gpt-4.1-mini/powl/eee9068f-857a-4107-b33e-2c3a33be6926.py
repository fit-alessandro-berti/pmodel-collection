# Generated from: eee9068f-857a-4107-b33e-2c3a33be6926.json
# Description: This process outlines the comprehensive steps involved in authenticating historical artifacts for museum acquisition and scholarly research. It begins with initial artifact intake, followed by provenance verification through archival research and expert interviews. Non-invasive material analysis is conducted using advanced imaging techniques to assess composition and age. Parallel to scientific testing, stylistic comparison with known artifacts is performed to identify cultural and temporal context. Legal clearance checks ensure no ownership disputes exist. Findings from all investigations are compiled into a detailed report, which undergoes peer review by a panel of historians and conservators. The final authentication decision informs acquisition strategy and potential restoration planning. Throughout the process, secure documentation and data integrity are maintained to support future reference and exhibit planning.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Artifact_Intake = Transition(label='Artifact Intake')

Provenance_Check = Transition(label='Provenance Check')
Archive_Search = Transition(label='Archive Search')
Expert_Interview = Transition(label='Expert Interview')

Material_Scan = Transition(label='Material Scan')
Age_Analysis = Transition(label='Age Analysis')

Stylistic_Review = Transition(label='Stylistic Review')
Context_Mapping = Transition(label='Context Mapping')

Legal_Clearance = Transition(label='Legal Clearance')

Data_Compilation = Transition(label='Data Compilation')
Report_Drafting = Transition(label='Report Drafting')

Peer_Review = Transition(label='Peer Review')

Final_Assessment = Transition(label='Final Assessment')
Acquisition_Plan = Transition(label='Acquisition Plan')
Restoration_Prep = Transition(label='Restoration Prep')

Documentation = Transition(label='Documentation')
Data_Backup = Transition(label='Data Backup')

# Provenance verification as PO of Archive Search and Expert Interview, both after Provenance Check
provenance_po = StrictPartialOrder(nodes=[Provenance_Check, Archive_Search, Expert_Interview])
provenance_po.order.add_edge(Provenance_Check, Archive_Search)
provenance_po.order.add_edge(Provenance_Check, Expert_Interview)

# Material analysis as PO of Material Scan then Age Analysis (sequential)
material_analysis_po = StrictPartialOrder(nodes=[Material_Scan, Age_Analysis])
material_analysis_po.order.add_edge(Material_Scan, Age_Analysis)

# Stylistic review as PO of Stylistic Review then Context Mapping (sequential)
stylistic_po = StrictPartialOrder(nodes=[Stylistic_Review, Context_Mapping])
stylistic_po.order.add_edge(Stylistic_Review, Context_Mapping)

# Scientific testing in parallel with stylistic review
# so a PO combining material_analysis_po and stylistic_po, both concurrent
science_and_style_po = StrictPartialOrder(nodes=[material_analysis_po, stylistic_po])

# Legal clearance after scientific and stylistic evaluation
legal_clearance_po = StrictPartialOrder(nodes=[science_and_style_po, Legal_Clearance])
legal_clearance_po.order.add_edge(science_and_style_po, Legal_Clearance)

# Data compilation after provenance check and legal clearance
compilation_po = StrictPartialOrder(nodes=[provenance_po, legal_clearance_po, Data_Compilation])
compilation_po.order.add_edge(provenance_po, Data_Compilation)
compilation_po.order.add_edge(legal_clearance_po, Data_Compilation)

# Report drafting after data compilation
report_po = StrictPartialOrder(nodes=[Data_Compilation, Report_Drafting])
report_po.order.add_edge(Data_Compilation, Report_Drafting)

# Peer review after report drafting
peer_review_po = StrictPartialOrder(nodes=[Report_Drafting, Peer_Review])
peer_review_po.order.add_edge(Report_Drafting, Peer_Review)

# Final assessment after peer review
final_assessment_po = StrictPartialOrder(nodes=[Peer_Review, Final_Assessment])
final_assessment_po.order.add_edge(Peer_Review, Final_Assessment)

# Acquisition plan and restoration prep after final assessment (parallel)
acq_rest_po = StrictPartialOrder(nodes=[Final_Assessment, Acquisition_Plan, Restoration_Prep])
acq_rest_po.order.add_edge(Final_Assessment, Acquisition_Plan)
acq_rest_po.order.add_edge(Final_Assessment, Restoration_Prep)

# Documentation and data backup run throughout and concurrently with entire process
# They can be modeled as concurrent to Artifact Intake, the full main flow starts after Artifact Intake
# So we create a PO with root artifact intake, then main process, and concurrent documentation+backup

# Main process: provenance_pro checks+ scientific/style and legal clearance + compilation + report + peer + final + acquisition/restoration
main_flow = StrictPartialOrder(nodes=[
    provenance_po, 
    science_and_style_po, 
    legal_clearance_po, 
    compilation_po, 
    report_po, 
    peer_review_po, 
    final_assessment_po, 
    acq_rest_po
])
# Define the order edges connecting these phases:
# provenance_po and science_and_style_po are concurrent, but legal_clearance requires science_and_style_po
main_flow.order.add_edge(science_and_style_po, legal_clearance_po)
# compilation_po depends on provenance_po and legal_clearance_po
main_flow.order.add_edge(provenance_po, compilation_po)
main_flow.order.add_edge(legal_clearance_po, compilation_po)
# report_po depends on compilation_po
main_flow.order.add_edge(compilation_po, report_po)
# peer_review_po depends on report_po
main_flow.order.add_edge(report_po, peer_review_po)
# final_assessment_po depends on peer_review_po
main_flow.order.add_edge(peer_review_po, final_assessment_po)
# acq_rest_po depends on final_assessment_po
main_flow.order.add_edge(final_assessment_po, acq_rest_po)

# Overall process root PO: Artifact Intake --> main_flow; Documentation & Data Backup concurrent to main_flow
doc_backup_po = StrictPartialOrder(nodes=[Documentation, Data_Backup])

# Compose root PO with nodes: Artifact Intake, main_flow, Documentation, Data Backup
root = StrictPartialOrder(nodes=[Artifact_Intake, main_flow, Documentation, Data_Backup])
# Artifact Intake precedes main_flow
root.order.add_edge(Artifact_Intake, main_flow)
# Documentation and Data_Backup concurrent with main_flow and after Artifact Intake -- no explicit order needed to maintain concurrency and parallelism

# The final root POWL object: