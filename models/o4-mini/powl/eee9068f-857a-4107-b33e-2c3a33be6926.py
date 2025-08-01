# Generated from: eee9068f-857a-4107-b33e-2c3a33be6926.json
# Description: This process outlines the comprehensive steps involved in authenticating historical artifacts for museum acquisition and scholarly research. It begins with initial artifact intake, followed by provenance verification through archival research and expert interviews. Non-invasive material analysis is conducted using advanced imaging techniques to assess composition and age. Parallel to scientific testing, stylistic comparison with known artifacts is performed to identify cultural and temporal context. Legal clearance checks ensure no ownership disputes exist. Findings from all investigations are compiled into a detailed report, which undergoes peer review by a panel of historians and conservators. The final authentication decision informs acquisition strategy and potential restoration planning. Throughout the process, secure documentation and data integrity are maintained to support future reference and exhibit planning.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
artifact_intake     = Transition(label='Artifact Intake')
provenance_check    = Transition(label='Provenance Check')
archive_search      = Transition(label='Archive Search')
expert_interview    = Transition(label='Expert Interview')
material_scan       = Transition(label='Material Scan')
age_analysis        = Transition(label='Age Analysis')
stylistic_review    = Transition(label='Stylistic Review')
context_mapping     = Transition(label='Context Mapping')
legal_clearance     = Transition(label='Legal Clearance')
data_compilation    = Transition(label='Data Compilation')
report_drafting     = Transition(label='Report Drafting')
peer_review         = Transition(label='Peer Review')
final_assessment    = Transition(label='Final Assessment')
acquisition_plan    = Transition(label='Acquisition Plan')
restoration_prep    = Transition(label='Restoration Prep')
documentation       = Transition(label='Documentation')
data_backup         = Transition(label='Data Backup')

# Build the partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    provenance_check,
    archive_search,
    expert_interview,
    material_scan,
    age_analysis,
    stylistic_review,
    context_mapping,
    legal_clearance,
    data_compilation,
    report_drafting,
    peer_review,
    final_assessment,
    acquisition_plan,
    restoration_prep,
    documentation,
    data_backup
])

# Artifact intake leads to provenance check
root.order.add_edge(artifact_intake, provenance_check)

# Provenance check leads to archival research and expert interview
root.order.add_edge(provenance_check, archive_search)
root.order.add_edge(provenance_check, expert_interview)

# After both archival research and interviews, start scientific testing
root.order.add_edge(archive_search, material_scan)
root.order.add_edge(expert_interview, material_scan)
root.order.add_edge(material_scan, age_analysis)

# After provenance check, start stylistic comparison in parallel
root.order.add_edge(archive_search, stylistic_review)
root.order.add_edge(expert_interview, stylistic_review)
root.order.add_edge(stylistic_review, context_mapping)

# Legal clearance awaits results of scientific and stylistic analyses
root.order.add_edge(age_analysis, legal_clearance)
root.order.add_edge(context_mapping, legal_clearance)

# Compile findings into a report
root.order.add_edge(legal_clearance, data_compilation)
root.order.add_edge(data_compilation, report_drafting)

# Report undergoes peer review and final assessment
root.order.add_edge(report_drafting, peer_review)
root.order.add_edge(peer_review, final_assessment)

# Final assessment drives acquisition and restoration planning
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# documentation and data_backup remain unconstrained (can occur anytime)