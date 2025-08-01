# Generated from: 5abe9b3a-77dc-40a7-bf02-2a5af4cddc05.json
# Description: This process involves the detailed examination and verification of rare artifacts obtained from private collectors and archaeological digs. Experts perform multi-disciplinary analyses including material composition testing, provenance tracing, and historical context validation. The process integrates advanced imaging techniques, chemical assays, and consultation with historians to confirm authenticity. Following authentication, artifacts undergo conservation assessment and are prepared for either museum display or private sale. Throughout, secure documentation and chain-of-custody protocols are strictly maintained to ensure legal compliance and provenance integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
artifact_receipt   = Transition(label='Artifact Receipt')
initial_inspection = Transition(label='Initial Inspection')

material_testing   = Transition(label='Material Testing')
imaging_scan       = Transition(label='Imaging Scan')
provenance_check   = Transition(label='Provenance Check')
historical_review  = Transition(label='Historical Review')
expert_consultation= Transition(label='Expert Consultation')
chemical_assay     = Transition(label='Chemical Assay')
forgery_analysis   = Transition(label='Forgery Analysis')

condition_report   = Transition(label='Condition Report')
conservation_plan  = Transition(label='Conservation Plan')

documentation      = Transition(label='Documentation')
chain_custody      = Transition(label='Chain Custody')
legal_review       = Transition(label='Legal Review')

display_setup      = Transition(label='Display Setup')
sale_preparation   = Transition(label='Sale Preparation')
final_approval     = Transition(label='Final Approval')

# XOR choice between museum display or private sale
display_or_sale = OperatorPOWL(operator=Operator.XOR, children=[display_setup, sale_preparation])

# Build the partial order
root = StrictPartialOrder(nodes=[
    artifact_receipt,
    initial_inspection,
    material_testing,
    imaging_scan,
    provenance_check,
    historical_review,
    expert_consultation,
    chemical_assay,
    forgery_analysis,
    condition_report,
    conservation_plan,
    display_or_sale,
    final_approval,
    documentation,
    chain_custody,
    legal_review
])

# Define the main flow
root.order.add_edge(artifact_receipt, initial_inspection)

# Parallel analyses after inspection
analyses = [
    material_testing,
    imaging_scan,
    provenance_check,
    historical_review,
    expert_consultation,
    chemical_assay,
    forgery_analysis
]
for a in analyses:
    root.order.add_edge(initial_inspection, a)
    root.order.add_edge(a, condition_report)

# Continue after analyses
root.order.add_edge(condition_report, conservation_plan)
root.order.add_edge(conservation_plan, display_or_sale)
root.order.add_edge(display_or_sale, final_approval)

# Ongoing compliance tasks (can interleave from receipt to final approval)
for t in [documentation, chain_custody, legal_review]:
    root.order.add_edge(artifact_receipt, t)
    root.order.add_edge(t, final_approval)