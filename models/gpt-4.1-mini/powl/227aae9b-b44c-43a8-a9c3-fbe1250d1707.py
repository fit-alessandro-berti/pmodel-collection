# Generated from: 227aae9b-b44c-43a8-a9c3-fbe1250d1707.json
# Description: This process outlines the detailed steps involved in authenticating historical artifacts for museums or private collectors. It begins with initial artifact intake and documentation, followed by non-invasive imaging and chemical analysis to identify materials and age. Experts conduct provenance research and comparative stylistic evaluation to verify authenticity. If discrepancies arise, advanced techniques like carbon dating or microscopic fiber analysis are employed. After scientific validation, legal checks ensure compliance with cultural heritage laws. The process concludes with detailed reporting, certification issuance, and secure archive storage. Throughout, cross-disciplinary collaboration and iterative reviews maintain accuracy and integrity in authentication.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
Artifact_Intake = Transition(label='Artifact Intake')
Initial_Scan = Transition(label='Initial Scan')
Material_Test = Transition(label='Material Test')
Provenance_Check = Transition(label='Provenance Check')
Style_Compare = Transition(label='Style Compare')
Carbon_Dating = Transition(label='Carbon Dating')
Fiber_Analysis = Transition(label='Fiber Analysis')
Legal_Review = Transition(label='Legal Review')
Expert_Panel = Transition(label='Expert Panel')
Condition_Report = Transition(label='Condition Report')
Data_Archive = Transition(label='Data Archive')
Certification = Transition(label='Certification')
Client_Brief = Transition(label='Client Brief')
Secure_Storage = Transition(label='Secure Storage')
Final_Approval = Transition(label='Final Approval')

# Advanced techniques choice if discrepancies arise
advanced_techniques = OperatorPOWL(
    operator=Operator.XOR,
    children=[Carbon_Dating, Fiber_Analysis]
)

# Loop for discrepancy handling: after initial checks, 
# if discrepancies -> advanced technique + provenance & style checks again (Expert_Panel)
# The description says loop over provenance research and comparative stylistic evaluation 
# after advanced techniques, to ensure accuracy.

# loop: (* (A, B)) means: execute A then choose exit, or B then A again
# Here A is provenance research & style compare + expert panel (review after advanced)
# B is advanced_techniques

# Define the repeated verification phase:
verification = StrictPartialOrder(nodes=[Provenance_Check, Style_Compare, Expert_Panel])
verification.order.add_edge(Provenance_Check, Style_Compare)
verification.order.add_edge(Style_Compare, Expert_Panel)

# Define the loop for discrepancy handling:
# Execute verification, then choose to exit or do advanced_techniques then verification again
loop_discrepancy = OperatorPOWL(operator=Operator.LOOP, children=[verification, advanced_techniques])

# Initial partial order: Artifact Intake -> (Initial Scan & Material Test in parallel)
initial_tests = StrictPartialOrder(nodes=[Initial_Scan, Material_Test])
# Initial Scan and Material Test can happen in parallel after Artifact Intake
initial_seq = StrictPartialOrder(nodes=[Artifact_Intake, initial_tests])
initial_seq.order.add_edge(Artifact_Intake, initial_tests)

# Partial order combining initial tests and discrepancy loop
pre_scientific_validation = StrictPartialOrder(nodes=[initial_seq, loop_discrepancy])
pre_scientific_validation.order.add_edge(initial_seq, loop_discrepancy)

# After scientific validation (loop_discrepancy), Legal Review next
# Then final reporting etc. in partial order, with some concurrency where possible

post_legal_and_reporting = StrictPartialOrder(
    nodes=[Legal_Review, Condition_Report, Certification, Client_Brief, Secure_Storage, Data_Archive, Final_Approval]
)
# Legal Review before all downstream activities (reporting, certification, storage, final approval)
post_legal_and_reporting.order.add_edge(Legal_Review, Condition_Report)
post_legal_and_reporting.order.add_edge(Legal_Review, Certification)
post_legal_and_reporting.order.add_edge(Legal_Review, Client_Brief)
post_legal_and_reporting.order.add_edge(Legal_Review, Secure_Storage)
post_legal_and_reporting.order.add_edge(Legal_Review, Data_Archive)

# The final approval is after certification and client brief (ensuring all reports and certification done)
post_legal_and_reporting.order.add_edge(Certification, Final_Approval)
post_legal_and_reporting.order.add_edge(Client_Brief, Final_Approval)

# Secure storage and data archive can be concurrent and before final approval
post_legal_and_reporting.order.add_edge(Secure_Storage, Final_Approval)
post_legal_and_reporting.order.add_edge(Data_Archive, Final_Approval)

# Combine the whole process: pre_scientific_validation -> Legal Review etc.
root = StrictPartialOrder(
    nodes=[pre_scientific_validation, post_legal_and_reporting]
)
root.order.add_edge(pre_scientific_validation, post_legal_and_reporting)