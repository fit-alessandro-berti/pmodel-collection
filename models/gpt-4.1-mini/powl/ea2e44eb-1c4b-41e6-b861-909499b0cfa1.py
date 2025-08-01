# Generated from: ea2e44eb-1c4b-41e6-b861-909499b0cfa1.json
# Description: This process outlines the complex steps involved in authenticating rare historical artifacts for a museum acquisition. It begins with initial artifact intake, followed by detailed provenance research including archival cross-referencing and expert consultations. Scientific analysis is conducted using non-invasive imaging techniques such as XRF and 3D scanning to determine material composition and manufacturing methods. Parallelly, stylistic comparisons with known artifact databases are performed. Results from all investigations are consolidated and reviewed in a multidisciplinary panel. Based on the consensus, a certification report is generated detailing authenticity, condition, and historical significance. Final steps include secure storage arrangement, digital cataloging, and preparation for public display or loan agreements with external institutions. Continuous monitoring protocols are established to ensure artifact preservation post-acquisition.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Artifact_Intake = Transition(label='Artifact Intake')
Provenance_Check = Transition(label='Provenance Check')
Archive_Search = Transition(label='Archive Search')
Expert_Consult = Transition(label='Expert Consult')
Material_Scan = Transition(label='Material Scan')
Imaging_3D = Transition(label='3D Imaging')
Stylistic_Match = Transition(label='Stylistic Match')
Database_Query = Transition(label='Database Query')
Panel_Review = Transition(label='Panel Review')
Certify_Report = Transition(label='Certify Report')
Condition_Assess = Transition(label='Condition Assess')
Storage_Plan = Transition(label='Storage Plan')
Catalog_Entry = Transition(label='Catalog Entry')
Display_Prep = Transition(label='Display Prep')
Loan_Arrange = Transition(label='Loan Arrange')
Monitor_Setup = Transition(label='Monitor Setup')

# Provenance Check is composed of Archive Search and Expert Consult, presumably sequentially
# scientific analysis is Material Scan and 3D Imaging in parallel
# stylistic comparison is Stylistic Match and Database Query in parallel
# these investigations must complete, then Panel Review
# then Certify Report, which includes Condition Assess (likely before/within)
# Final steps: Storage Plan, Catalog Entry, then a choice between Display Prep or Loan Arrange
# Then Monitor Setup last

# provenance research PO
provenance_PO = StrictPartialOrder(nodes=[Provenance_Check, Archive_Search, Expert_Consult])
provenance_PO.order.add_edge(Provenance_Check, Archive_Search)
provenance_PO.order.add_edge(Archive_Search, Expert_Consult)  # Assuming Archive Search precedes Expert Consult

# scientific analysis partial order: Material Scan || 3D Imaging (concurrent)
scientific_PO = StrictPartialOrder(nodes=[Material_Scan, Imaging_3D])
# no order edges = concurrent

# stylistic comparison partial order: Stylistic Match || Database Query (concurrent)
stylistic_PO = StrictPartialOrder(nodes=[Stylistic_Match, Database_Query])
# no order edges = concurrent

# investigations combined: provenance_PO, scientific_PO, stylistic_PO in parallel
investigations = StrictPartialOrder(
    nodes=[provenance_PO, scientific_PO, stylistic_PO]
)
# no order edges = investigations in parallel

# after investigations complete -> Panel Review
main_flow1 = StrictPartialOrder(
    nodes=[investigations, Panel_Review]
)
main_flow1.order.add_edge(investigations, Panel_Review)

# After Panel Review -> Certify Report, which includes Condition Assess (likely sequentially)
certify_PO = StrictPartialOrder(nodes=[Certify_Report, Condition_Assess])
certify_PO.order.add_edge(Certify_Report, Condition_Assess)

# After condition assess, to final steps
final_steps_PO1 = StrictPartialOrder(nodes=[Storage_Plan, Catalog_Entry])
final_steps_PO1.order.add_edge(Storage_Plan, Catalog_Entry)

# Choice between Display Prep or Loan Arrange
choice_display_loan = OperatorPOWL(operator=Operator.XOR, children=[Display_Prep, Loan_Arrange])

# Final steps: final_steps_PO1 -> choice_display_loan -> Monitor Setup
final_steps_PO2 = StrictPartialOrder(nodes=[final_steps_PO1, choice_display_loan, Monitor_Setup])
final_steps_PO2.order.add_edge(final_steps_PO1, choice_display_loan)
final_steps_PO2.order.add_edge(choice_display_loan, Monitor_Setup)

# Combine certify_PO and final steps sequencially
post_panel_PO = StrictPartialOrder(nodes=[certify_PO, final_steps_PO2])
post_panel_PO.order.add_edge(certify_PO, final_steps_PO2)

# Full flow after Artifact Intake
after_intake_PO = StrictPartialOrder(nodes=[main_flow1, post_panel_PO])
after_intake_PO.order.add_edge(main_flow1, post_panel_PO)

# Overall full process: Artifact Intake -> after_intake_PO
root = StrictPartialOrder(nodes=[Artifact_Intake, after_intake_PO])
root.order.add_edge(Artifact_Intake, after_intake_PO)