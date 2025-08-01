# Generated from: 43c018a1-17d6-4953-a704-d02d613c0d22.json
# Description: This process governs the detailed authentication of historical artifacts prior to acquisition by a museum or private collector. It involves multidisciplinary examination including provenance research, material analysis, and expert validation. The workflow integrates scientific testing methods such as radiocarbon dating and spectroscopy, alongside archival investigation and comparative stylistic analysis. Stakeholders coordinate through iterative reviews to confirm authenticity, assess conservation needs, and finalize acquisition terms. This atypical yet realistic business process ensures artifacts meet strict cultural and legal standards while minimizing risks of forgery or misattribution, ultimately preserving historical integrity and value.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Initial_Review = Transition(label='Initial Review')

# Multidisciplinary examination branch: provenance research, material analysis, expert validation
Provenance_Check = Transition(label='Provenance Check')

# Material Analysis sub-activities: Material Sampling followed by Radiocarbon Test and Spectroscopy Scan in parallel
Material_Sampling = Transition(label='Material Sampling')
Radiocarbon_Test = Transition(label='Radiocarbon Test')
Spectroscopy_Scan = Transition(label='Spectroscopy Scan')
Stylistic_Compare = Transition(label='Stylistic Compare')

# Archival Search and Expert Consult
Archival_Search = Transition(label='Archival Search')
Expert_Consult = Transition(label='Expert Consult')

# Stakeholder coordination and assessments
Condition_Assess = Transition(label='Condition Assess')
Conservation_Plan = Transition(label='Conservation Plan')
Risk_Analysis = Transition(label='Risk Analysis')
Legal_Verify = Transition(label='Legal Verify')
Acquisition_Offer = Transition(label='Acquisition Offer')
Stakeholder_Review = Transition(label='Stakeholder Review')
Final_Approval = Transition(label='Final Approval')

# Material Analysis partial order: after sampling, Radiocarbon Test and Spectroscopy Scan run concurrently
mat_analysis = StrictPartialOrder(
    nodes=[Material_Sampling, Radiocarbon_Test, Spectroscopy_Scan]
)
mat_analysis.order.add_edge(Material_Sampling, Radiocarbon_Test)
mat_analysis.order.add_edge(Material_Sampling, Spectroscopy_Scan)

# Provenance research partial order: Provenance Check, Archival Search, Stylistic Compare, Expert Consult
prov_research = StrictPartialOrder(
    nodes=[Provenance_Check, Archival_Search, Stylistic_Compare, Expert_Consult]
)
# Assume Provenance Check precedes Archival Search and Stylistic Compare
prov_research.order.add_edge(Provenance_Check, Archival_Search)
prov_research.order.add_edge(Provenance_Check, Stylistic_Compare)
# Expert Consult after Archival Search and Stylistic Compare
prov_research.order.add_edge(Archival_Search, Expert_Consult)
prov_research.order.add_edge(Stylistic_Compare, Expert_Consult)

# Multidisciplinary examination is the parallel execution of prov_research and mat_analysis,
# and then Expert Consult as a synchronization join is already placed above after both
# Actually Expert Consult depends on Archival Search and Stylistic Compare, but not on mat_analysis
# So allow mat_analysis and prov_research to run concurrently, but Expert Consult is part of prov_research

# We will create a partial order combining prov_research and mat_analysis with concurrency
multidisciplinary = StrictPartialOrder(
    nodes=[prov_research, mat_analysis]
)
# No order edges between prov_research and mat_analysis for concurrency

# After multidisciplinary examination, Condition Assess and Conservation Plan run in parallel,
# then Risk Analysis, then Legal Verify and Acquisition Offer in sequence,
# Stakeholder Review after Acquisition Offer, and Final Approval finalizes.

cons_and_assess = StrictPartialOrder(
    nodes=[Condition_Assess, Conservation_Plan]
)
# No order => concurrent

post_exam = StrictPartialOrder(
    nodes=[cons_and_assess, Risk_Analysis]
)
post_exam.order.add_edge(cons_and_assess, Risk_Analysis)

legal_and_offer = StrictPartialOrder(
    nodes=[Legal_Verify, Acquisition_Offer]
)
legal_and_offer.order.add_edge(Legal_Verify, Acquisition_Offer)

final_stages = StrictPartialOrder(
    nodes=[legal_and_offer, Stakeholder_Review]
)
final_stages.order.add_edge(legal_and_offer, Stakeholder_Review)

final_approval_stage = StrictPartialOrder(
    nodes=[final_stages, Final_Approval]
)
final_approval_stage.order.add_edge(final_stages, Final_Approval)

# Combine post_exam, final_stages, final_approval_stage in sequence
post_exam_to_final = StrictPartialOrder(
    nodes=[post_exam, final_stages, Final_Approval]
)
post_exam_to_final.order.add_edge(post_exam, final_stages)
post_exam_to_final.order.add_edge(final_stages, Final_Approval)

# Sequence after multidisciplinary: Condition Assess & Conservation Plan parallel,
# then Risk Analysis, Legal Verify, Acquisition Offer, Stakeholder Review, Final Approval

# Build main flow
main_flow = StrictPartialOrder(
    nodes=[Initial_Review, multidisciplinary, cons_and_assess, Risk_Analysis,
           Legal_Verify, Acquisition_Offer, Stakeholder_Review, Final_Approval]
)

# Initial Review before multidisciplinary
main_flow.order.add_edge(Initial_Review, multidisciplinary)

# Multidisciplinary before Condition Assess & Conservation Plan
main_flow.order.add_edge(multidisciplinary, cons_and_assess)

# Condition Assess & Conservation Plan before Risk Analysis
main_flow.order.add_edge(cons_and_assess, Risk_Analysis)

# Risk Analysis before Legal Verify
main_flow.order.add_edge(Risk_Analysis, Legal_Verify)

# Legal Verify before Acquisition Offer
main_flow.order.add_edge(Legal_Verify, Acquisition_Offer)

# Acquisition Offer before Stakeholder Review
main_flow.order.add_edge(Acquisition_Offer, Stakeholder_Review)

# Stakeholder Review before Final Approval
main_flow.order.add_edge(Stakeholder_Review, Final_Approval)

# root is the main flow
root = main_flow