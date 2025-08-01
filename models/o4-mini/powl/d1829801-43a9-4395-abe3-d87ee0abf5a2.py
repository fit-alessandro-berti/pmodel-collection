# Generated from: d1829801-43a9-4395-abe3-d87ee0abf5a2.json
# Description: This process involves the detailed authentication of antique artifacts using a blend of scientific analysis, historical research, and expert validation. The process begins with initial artifact intake and visual inspection, followed by advanced material composition testing and radiocarbon dating. Parallelly, provenance research is conducted by examining archival records and previous ownership histories. Next, specialized experts assess stylistic and craftsmanship elements before the artifact undergoes condition assessment and restoration feasibility analysis. The process includes risk evaluation for potential forgery and legal compliance checks. Finally, findings are compiled into a comprehensive authentication report, and the artifact is cataloged into a secure database for future reference and insurance purposes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
artifact_intake   = Transition(label='Artifact Intake')
visual_inspection = Transition(label='Visual Inspection')
material_testing  = Transition(label='Material Testing')
radiocarbon       = Transition(label='Radiocarbon Dating')
provenance_check  = Transition(label='Provenance Check')
archive_research  = Transition(label='Archive Research')
expert_review     = Transition(label='Expert Review')
style_analysis    = Transition(label='Style Analysis')
craftsmanship     = Transition(label='Craftsmanship Eval')
condition_check   = Transition(label='Condition Check')
restoration_plan  = Transition(label='Restoration Plan')
forgery_risk      = Transition(label='Forgery Risk')
legal_review      = Transition(label='Legal Review')
report_drafting   = Transition(label='Report Drafting')
catalog_entry     = Transition(label='Catalog Entry')

# Build a strict partial order with all nodes
root = StrictPartialOrder(nodes=[
    artifact_intake, visual_inspection,
    material_testing, radiocarbon,
    provenance_check, archive_research,
    expert_review, style_analysis, craftsmanship,
    condition_check, restoration_plan,
    forgery_risk, legal_review,
    report_drafting, catalog_entry
])

# 1. Sequence: Artifact Intake -> Visual Inspection
root.order.add_edge(artifact_intake, visual_inspection)

# 2. After visual inspection, run tests and provenance research in parallel
for nxt in [material_testing, radiocarbon, provenance_check, archive_research]:
    root.order.add_edge(visual_inspection, nxt)

# 3. Once testing & provenance are done, do expert review
for prev in [material_testing, radiocarbon, provenance_check, archive_research]:
    root.order.add_edge(prev, expert_review)

# 4. Expert review precedes style & craftsmanship analysis (in parallel)
root.order.add_edge(expert_review, style_analysis)
root.order.add_edge(expert_review, craftsmanship)

# 5. Both analyses feed into the condition check
root.order.add_edge(style_analysis, condition_check)
root.order.add_edge(craftsmanship, condition_check)

# 6. Condition check -> Restoration plan
root.order.add_edge(condition_check, restoration_plan)

# 7. Restoration plan -> Forgery risk & Legal review (parallel)
root.order.add_edge(restoration_plan, forgery_risk)
root.order.add_edge(restoration_plan, legal_review)

# 8. Both risk/legal feed into report drafting
root.order.add_edge(forgery_risk, report_drafting)
root.order.add_edge(legal_review, report_drafting)

# 9. Finally, report drafting -> Catalog entry
root.order.add_edge(report_drafting, catalog_entry)