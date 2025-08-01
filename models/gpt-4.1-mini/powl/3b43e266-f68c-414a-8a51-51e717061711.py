# Generated from: 3b43e266-f68c-414a-8a51-51e717061711.json
# Description: This process governs the verification and authentication of ancient artifacts prior to acquisition by museums or private collectors. It involves multidisciplinary collaboration across historians, chemists, and legal experts. The workflow begins with preliminary artifact inspection, followed by material composition analysis using spectroscopy, radiocarbon dating, and microscopic examination. Subsequent provenance research entails tracing ownership history through archival records and cross-referencing with known historical events. Legal clearance is obtained to confirm artifact export and import compliance. Conservation specialists then assess preservation needs and recommend restoration protocols. Finally, a comprehensive authentication report is compiled, integrating scientific data, historical context, and legal validation to support acquisition decisions and prevent fraudulent transactions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
Initial_Inspect = Transition(label='Initial Inspect')

Material_Test = Transition(label='Material Test')
Radiocarbon_Date = Transition(label='Radiocarbon Date')
Microscopic_Scan = Transition(label='Microscopic Scan')

Provenance_Check = Transition(label='Provenance Check')
Archive_Search = Transition(label='Archive Search')
Owner_Verify = Transition(label='Owner Verify')

Legal_Review = Transition(label='Legal Review')
Export_Clearance = Transition(label='Export Clearance')
Import_Clearance = Transition(label='Import Clearance')

Conservation_Eval = Transition(label='Conservation Eval')
Restoration_Plan = Transition(label='Restoration Plan')

Report_Draft = Transition(label='Report Draft')
Report_Review = Transition(label='Report Review')
Final_Approval = Transition(label='Final Approval')

# Material Testing concurrent steps (Spectroscopy implied in Material Test, Radiocarbon Date, Microscopic Scan)
material_tests = StrictPartialOrder(nodes=[Material_Test, Radiocarbon_Date, Microscopic_Scan])
# no order, fully concurrent among the three tests

# Provenance research: tracing ownership history via archival records and cross-referencing 
# Combine Archive Search and Owner Verify after Provenance_Check
provenance_sub = StrictPartialOrder(nodes=[Archive_Search, Owner_Verify])
# archive search and owner verify concurrent

provenance_check_and_sub = StrictPartialOrder(nodes=[Provenance_Check, provenance_sub])
provenance_check_and_sub.order.add_edge(Provenance_Check, provenance_sub)

# Legal clearance: review then export and import clearance in parallel
legal_clearance_sub = StrictPartialOrder(nodes=[Export_Clearance, Import_Clearance])
legal_clearance = StrictPartialOrder(nodes=[Legal_Review, legal_clearance_sub])
legal_clearance.order.add_edge(Legal_Review, legal_clearance_sub)

# Conservation specialists: conservation eval then restoration plan
conservation = StrictPartialOrder(nodes=[Conservation_Eval, Restoration_Plan])
conservation.order.add_edge(Conservation_Eval, Restoration_Plan)

# Report generation sequential: draft, review, approve
report = StrictPartialOrder(nodes=[Report_Draft, Report_Review, Final_Approval])
report.order.add_edge(Report_Draft, Report_Review)
report.order.add_edge(Report_Review, Final_Approval)

# Draft the full process:

# Steps after initial inspect:
# 1) material tests (concurrent)
# 2) provenance check and its substeps
# 3) legal clearance
# 4) conservation
# 5) report

# These steps are in sequence

step2_to_5 = StrictPartialOrder(
    nodes=[material_tests, provenance_check_and_sub, legal_clearance, conservation, report]
)

step2_to_5.order.add_edge(material_tests, provenance_check_and_sub)
step2_to_5.order.add_edge(provenance_check_and_sub, legal_clearance)
step2_to_5.order.add_edge(legal_clearance, conservation)
step2_to_5.order.add_edge(conservation, report)

root = StrictPartialOrder(nodes=[Initial_Inspect, step2_to_5])
root.order.add_edge(Initial_Inspect, step2_to_5)