# Generated from: e300561d-2900-4766-a97e-1fd1ba9c2e40.json
# Description: This process involves the systematic verification and authentication of historical artifacts within a museum's acquisition department. It begins with the initial artifact intake, where physical condition and provenance documentation are recorded. The artifact then undergoes material composition testing using spectrometry and other scientific methods to verify age and origin. Concurrently, expert historians conduct stylistic analysis comparing the artifact to known references. Any discrepancies trigger a secondary review involving cross-institutional consultation. Provenance authenticity is validated through archival research and digital ledger cross-checks. Upon successful authentication, conservation specialists prepare the artifact for display or storage, documenting all interventions. The final step involves creating a detailed report and updating the museum database to reflect the artifact's authenticated status and provenance trail, ensuring traceability and future re-verification capability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Intake_Check = Transition(label='Intake Check')
Condition_Log = Transition(label='Condition Log')
Provenance_Review = Transition(label='Provenance Review')

Material_Test = Transition(label='Material Test')
Spectrometry_Scan = Transition(label='Spectrometry Scan')

Stylistic_Analysis = Transition(label='Stylistic Analysis')
Expert_Consult = Transition(label='Expert Consult')

Archive_Search = Transition(label='Archive Search')
Ledger_Verification = Transition(label='Ledger Verification')

Secondary_Review = Transition(label='Secondary Review')
Cross_Check = Transition(label='Cross-Check')

Conservation_Prep = Transition(label='Conservation Prep')
Documentation = Transition(label='Documentation')

Report_Creation = Transition(label='Report Creation')
Database_Update = Transition(label='Database Update')

# Model concurrency and structure

# Intake phase: Intake Check --> Condition Log and Provenance Review in sequence
intake_seq = StrictPartialOrder(nodes=[Intake_Check, Condition_Log, Provenance_Review])
intake_seq.order.add_edge(Intake_Check, Condition_Log)
intake_seq.order.add_edge(Condition_Log, Provenance_Review)

# Material Test phase: Material Test then Spectrometry Scan in sequence
material_seq = StrictPartialOrder(nodes=[Material_Test, Spectrometry_Scan])
material_seq.order.add_edge(Material_Test, Spectrometry_Scan)

# Expert Analysis phase: Stylistic Analysis then Expert Consult in sequence
expert_seq = StrictPartialOrder(nodes=[Stylistic_Analysis, Expert_Consult])
expert_seq.order.add_edge(Stylistic_Analysis, Expert_Consult)

# Provenance authenticity validation: Archive Search then Ledger Verification in sequence
provenance_seq = StrictPartialOrder(nodes=[Archive_Search, Ledger_Verification])
provenance_seq.order.add_edge(Archive_Search, Ledger_Verification)

# Secondary review with cross-institutional consultation (triggered by discrepancies)
secondary_seq = StrictPartialOrder(nodes=[Secondary_Review, Cross_Check])
secondary_seq.order.add_edge(Secondary_Review, Cross_Check)

# After expert analysis, if discrepancies, do secondary review before continuing
# So Expert_Consult followed optionally by Secondary_Review & Cross_Check

# Model secondary review loop as: loop(ExpertConsultResult, SecondaryReview)
# Here Secondary review triggered after Expert consult

# Create loop: execute expert_seq, then choose either exit or secondary_seq then expert_seq again

loop_expert = OperatorPOWL(
    operator=Operator.LOOP,
    children=[expert_seq, secondary_seq]
)

# Parallel testing of Material Test / Spectrometry Scan and looped Expert Analysis
material_and_expert = StrictPartialOrder(nodes=[material_seq, loop_expert])
material_and_expert.order.add_edge(material_seq, loop_expert)

# Provenance validation (Archive Search -> Ledger Verification)
# Assume it runs concurrently with Material+Expert analyses after Intake

# So we have Intake --> parallel branches:
#   1) material_and_expert
#   2) provenance_seq

post_intake_parallel = StrictPartialOrder(
    nodes=[material_and_expert, provenance_seq]
)
post_intake_parallel.order.add_edge(material_and_expert, provenance_seq)

# Conservation Prep and Documentation happen after all validations complete
cons_doc_seq = StrictPartialOrder(nodes=[Conservation_Prep, Documentation])
cons_doc_seq.order.add_edge(Conservation_Prep, Documentation)

# Final report creation and database update after conservation/documentation
final_seq = StrictPartialOrder(nodes=[Report_Creation, Database_Update])
final_seq.order.add_edge(Report_Creation, Database_Update)

# Combine conservation/documentation with final tasks in sequence
post_auth_seq = StrictPartialOrder(nodes=[cons_doc_seq, final_seq])
post_auth_seq.order.add_edge(cons_doc_seq, final_seq)

# Now the full process:

# Intake sequence --> post intake parallel (material_and_expert + provenance_seq)
# --> post authentication sequence

root = StrictPartialOrder(
    nodes=[intake_seq, post_intake_parallel, post_auth_seq]
)
root.order.add_edge(intake_seq, post_intake_parallel)
root.order.add_edge(post_intake_parallel, post_auth_seq)