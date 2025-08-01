# Generated from: e300561d-2900-4766-a97e-1fd1ba9c2e40.json
# Description: This process involves the systematic verification and authentication of historical artifacts within a museum's acquisition department. It begins with the initial artifact intake, where physical condition and provenance documentation are recorded. The artifact then undergoes material composition testing using spectrometry and other scientific methods to verify age and origin. Concurrently, expert historians conduct stylistic analysis comparing the artifact to known references. Any discrepancies trigger a secondary review involving cross-institutional consultation. Provenance authenticity is validated through archival research and digital ledger cross-checks. Upon successful authentication, conservation specialists prepare the artifact for display or storage, documenting all interventions. The final step involves creating a detailed report and updating the museum database to reflect the artifact's authenticated status and provenance trail, ensuring traceability and future re-verification capability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
intake_check = Transition(label="Intake Check")
condition_log = Transition(label="Condition Log")
provenance_review = Transition(label="Provenance Review")
archive_search = Transition(label="Archive Search")
ledger_verification = Transition(label="Ledger Verification")
material_test = Transition(label="Material Test")
spectrometry_scan = Transition(label="Spectrometry Scan")
stylistic_analysis = Transition(label="Stylistic Analysis")
secondary_review = Transition(label="Secondary Review")
expert_consult = Transition(label="Expert Consult")
cross_check = Transition(label="Cross-Check")
conservation_prep = Transition(label="Conservation Prep")
documentation = Transition(label="Documentation")
report_creation = Transition(label="Report Creation")
database_update = Transition(label="Database Update")

# Silent skip for the XOR
skip = SilentTransition()

# 1) Parallel branch: Material Test -> Spectrometry Scan  ||  Stylistic Analysis
parallel_po = StrictPartialOrder(nodes=[material_test, spectrometry_scan, stylistic_analysis])
parallel_po.order.add_edge(material_test, spectrometry_scan)
# (stylistic_analysis is concurrent, no edges to/from it here)

# 2) Secondary‐review branch: Secondary Review -> Expert Consult -> Cross-Check
secondary_po = StrictPartialOrder(
    nodes=[secondary_review, expert_consult, cross_check]
)
secondary_po.order.add_edge(secondary_review, expert_consult)
secondary_po.order.add_edge(expert_consult, cross_check)

# 3) XOR between skipping review or doing the secondary review
xor_review = OperatorPOWL(operator=Operator.XOR, children=[skip, secondary_po])

# 4) Assemble the whole process as one big partial order
root = StrictPartialOrder(
    nodes=[
        intake_check,
        condition_log,
        provenance_review,
        archive_search,
        ledger_verification,
        parallel_po,
        xor_review,
        conservation_prep,
        documentation,
        report_creation,
        database_update,
    ]
)

# Define the control‐flow / causal edges
root.order.add_edge(intake_check, condition_log)
root.order.add_edge(condition_log, provenance_review)
root.order.add_edge(provenance_review, archive_search)
root.order.add_edge(archive_search, ledger_verification)

# After provenance validation, go into the parallel test & analysis
root.order.add_edge(ledger_verification, parallel_po)

# After parallel analyses, choose to review or not
root.order.add_edge(parallel_po, xor_review)

# After the XOR, continue with conservation and reporting
root.order.add_edge(xor_review, conservation_prep)
root.order.add_edge(conservation_prep, documentation)
root.order.add_edge(documentation, report_creation)
root.order.add_edge(report_creation, database_update)