# Generated from: 9ed97d72-319b-4337-bcc9-c01958d0e1e3.json
# Description: This complex process involves the detailed authentication of antique artifacts by combining scientific analysis, provenance research, and expert evaluation. Initially, artifacts undergo non-invasive imaging and material composition tests to detect forgeries or restorations. Concurrently, historical records and ownership chains are meticulously verified through archival research and interviews. The process also includes stylistic comparison with verified pieces and consultation with domain experts. Finally, all gathered data is synthesized into a comprehensive report that determines authenticity, estimated value, and historical significance, ensuring the artifact's credibility in the market and preservation archives.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Visual_Scan = Transition(label='Visual Scan')
Material_Test = Transition(label='Material Test')
Imaging_Analysis = Transition(label='Imaging Analysis')
Provenance_Check = Transition(label='Provenance Check')
Archive_Search = Transition(label='Archive Search')
Interview_Experts = Transition(label='Interview Experts')
Stylistic_Match = Transition(label='Stylistic Match')
Forgery_Detect = Transition(label='Forgery Detect')
Condition_Report = Transition(label='Condition Report')
Market_Compare = Transition(label='Market Compare')
Historical_Cross = Transition(label='Historical Cross')
Expert_Review = Transition(label='Expert Review')
Database_Update = Transition(label='Database Update')
Value_Estimation = Transition(label='Value Estimation')
Final_Report = Transition(label='Final Report')

# Build Non-invasive imaging and material composition tests
# "Initially, artifacts undergo non-invasive imaging and material composition tests"
# Non-invasive imaging = Visual Scan and Imaging Analysis and Forgery Detect (forgeries/restorations detection)
# Material test separate activity
imaging_po = StrictPartialOrder(nodes=[Visual_Scan, Imaging_Analysis, Forgery_Detect])
imaging_po.order.add_edge(Visual_Scan, Imaging_Analysis)
imaging_po.order.add_edge(Imaging_Analysis, Forgery_Detect)

material_test_po = StrictPartialOrder(nodes=[Material_Test])

# Combine Imaging and Material tests concurrently
initial_tests = StrictPartialOrder(nodes=[imaging_po, material_test_po])

# Provenance research: "historical records and ownership chains verified through archival research and interviews"
# Provenance Check -> (Archive Search and Interview Experts in parallel)

archive_interview_po = StrictPartialOrder(nodes=[Archive_Search, Interview_Experts])
provenance_po = StrictPartialOrder(nodes=[Provenance_Check, archive_interview_po])
provenance_po.order.add_edge(Provenance_Check, archive_interview_po)

# Stylistic comparison and domain expert consultation happen concurrently,
# but after provenance research and initial tests?
# The description says "also includes stylistic comparison ... and consultation with experts", 
# likely these after provenance and initial tests can be concurrent:
stylistic_expert_po = StrictPartialOrder(nodes=[Stylistic_Match, Expert_Review])

# Historical Cross and Market Compare and Condition Report mentioned in report synthesis phase
# Actually Condition Report, Historical Cross, Market Compare are mentioned in "Finally all gathered data is synthesized..."
# To synthesize, let's assume the previous parallel branches join in a partial order and then these activities run in parallel,
# followed by Database Update and Value Estimation then Final Report

# Compose all parallel initial branches
# initial_tests, provenance_po, stylistic_expert_po run concurrently
parallel_branches = StrictPartialOrder(nodes=[initial_tests, provenance_po, stylistic_expert_po])

# Then three activities run in parallel: Condition Report, Market Compare, Historical Cross
final_data_gathering = StrictPartialOrder(nodes=[Condition_Report, Market_Compare, Historical_Cross])

# After data gathering, Expert Review already done in stylistic_expert_po, but the description suggests this is part of synthesis
# We link expert review before final reporting just in case to ensure order
# But since Expert Review is included earlier, maybe we consider Database Update and Value Estimation then Final Report after

# After final data gathering, Database Update and Value Estimation occur sequentially before Final Report
post_data = StrictPartialOrder(nodes=[Database_Update, Value_Estimation])
post_data.order.add_edge(Database_Update, Value_Estimation)

# Final Report after Value Estimation
final_phase = StrictPartialOrder(nodes=[post_data, Final_Report])
final_phase.order.add_edge(post_data, Final_Report)

# Now put the ordering edges to chain these phases:
root = StrictPartialOrder(nodes=[parallel_branches, final_data_gathering, final_phase])
root.order.add_edge(parallel_branches, final_data_gathering)
root.order.add_edge(final_data_gathering, final_phase)