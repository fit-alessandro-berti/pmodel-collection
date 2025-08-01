# Generated from: cbc2fe47-5242-461d-99bf-57635fdccdab.json
# Description: This process involves a detailed and atypical workflow used by museums and private collectors to authenticate rare historical artifacts. It integrates multidisciplinary expertise including provenance research, scientific analysis, and expert panel reviews. The process begins with initial artifact intake and documentation, followed by layered provenance verification involving archival searches and previous ownership validation. Scientific testing such as radiocarbon dating, spectroscopy, and material composition analysis is then conducted to identify anachronisms or forgeries. Concurrently, a panel of historians and art experts assess the stylistic and contextual authenticity. The findings are compiled into a comprehensive authentication report, which then undergoes a final quality review. If authenticated, the artifact is cataloged and insured; otherwise, recommendations for further investigation or rejection are made. The workflow also includes secure data archiving and periodic re-evaluation triggered by new research or technological advancements, ensuring ongoing verification integrity over time.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
artifact_intake      = Transition('Artifact Intake')
document_check       = Transition('Document Check')
provenance_search    = Transition('Provenance Search')
ownership_validate   = Transition('Ownership Validate')
radiocarbon_test     = Transition('Radiocarbon Test')
spectroscopy_scan    = Transition('Spectroscopy Scan')
material_analysis    = Transition('Material Analysis')
style_assessment     = Transition('Style Assessment')
context_review       = Transition('Context Review')
expert_panel         = Transition('Expert Panel')
report_draft         = Transition('Report Draft')
quality_review       = Transition('Quality Review')

# Define the "authenticated" branch: Catalog Entry -> Insurance Setup
catalog_entry    = Transition('Catalog Entry')
insurance_setup  = Transition('Insurance Setup')
auth_seq = StrictPartialOrder(nodes=[catalog_entry, insurance_setup])
auth_seq.order.add_edge(catalog_entry, insurance_setup)

# Define the XOR for authentication decision
#   - If authenticated, follow auth_seq
#   - Otherwise, take a silent branch (e.g., rejection/further‐investigation)
skip = SilentTransition()
xor_auth = OperatorPOWL(operator=Operator.XOR, children=[auth_seq, skip])

# Define the loop for periodic archiving & re‐evaluation
archive_data         = Transition('Archive Data')
reevaluation_trigger = Transition('Reevaluation Trigger')
loop = OperatorPOWL(operator=Operator.LOOP, children=[archive_data, reevaluation_trigger])

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        artifact_intake,
        document_check,
        provenance_search,
        ownership_validate,
        radiocarbon_test,
        spectroscopy_scan,
        material_analysis,
        style_assessment,
        context_review,
        expert_panel,
        report_draft,
        quality_review,
        xor_auth,
        loop
    ]
)

# Sequencing: intake → document check → provenance steps
root.order.add_edge(artifact_intake, document_check)
root.order.add_edge(document_check, provenance_search)
root.order.add_edge(provenance_search, ownership_validate)

# After ownership validation, branch into:
#  1) three concurrent scientific tests
#  2) style/context assessment followed by expert panel
root.order.add_edge(ownership_validate, radiocarbon_test)
root.order.add_edge(ownership_validate, spectroscopy_scan)
root.order.add_edge(ownership_validate, material_analysis)
root.order.add_edge(ownership_validate, style_assessment)
root.order.add_edge(style_assessment, context_review)
root.order.add_edge(context_review, expert_panel)

# Synchronize all into report drafting
for src in [radiocarbon_test, spectroscopy_scan, material_analysis, expert_panel]:
    root.order.add_edge(src, report_draft)

# Continue: report → quality review → authentication decision → archiving loop
root.order.add_edge(report_draft, quality_review)
root.order.add_edge(quality_review, xor_auth)
root.order.add_edge(xor_auth, loop)