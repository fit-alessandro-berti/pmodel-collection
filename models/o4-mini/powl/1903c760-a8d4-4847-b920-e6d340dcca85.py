# Generated from: 1903c760-a8d4-4847-b920-e6d340dcca85.json
# Description: This process involves the comprehensive authentication of antiques for high-end auction houses. It starts with initial artifact intake and condition review, followed by provenance verification through archival research and expert interviews. Scientific testing includes material composition analysis and radiocarbon dating to validate age. Parallelly, stylistic comparison against known period examples is performed by art historians. Legal clearance ensures no illicit trade history. Finally, a detailed report is generated combining all findings to inform auction valuation and marketing strategies. This workflow mitigates fraud and enhances buyer confidence in rare artifact transactions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
artifact_intake      = Transition(label='Artifact Intake')
condition_check      = Transition(label='Condition Check')
prov_research        = Transition(label='Provenance Research')
expert_interview     = Transition(label='Expert Interview')
historical_context   = Transition(label='Historical Context')
documentation_review = Transition(label='Documentation Review')
material_testing     = Transition(label='Material Testing')
radiocarbon_date     = Transition(label='Radiocarbon Date')
stylistic_compare    = Transition(label='Stylistic Compare')
forgery_analysis     = Transition(label='Forgery Analysis')
legal_clearance      = Transition(label='Legal Clearance')
report_drafting      = Transition(label='Report Drafting')
valuation_meeting    = Transition(label='Valuation Meeting')
marketing_prep       = Transition(label='Marketing Prep')
final_approval       = Transition(label='Final Approval')

# Stage 1: Intake and condition review
stage1 = StrictPartialOrder(nodes=[artifact_intake, condition_check])
stage1.order.add_edge(artifact_intake, condition_check)

# Stage 2: Provenance verification (all parallel)
stage2 = StrictPartialOrder(nodes=[
    prov_research,
    expert_interview,
    historical_context,
    documentation_review
])

# Stage 3: Scientific testing (material -> radiocarbon) with concurrent stylistic compare and forgery analysis
scientific_tests = StrictPartialOrder(nodes=[material_testing, radiocarbon_date])
scientific_tests.order.add_edge(material_testing, radiocarbon_date)

stage3 = StrictPartialOrder(nodes=[
    scientific_tests,
    stylistic_compare,
    forgery_analysis
])

# Stage 4: Legal clearance then report drafting
stage4 = StrictPartialOrder(nodes=[legal_clearance, report_drafting])
stage4.order.add_edge(legal_clearance, report_drafting)

# Stage 5: Valuation & marketing in parallel, then final approval
stage5_prep = StrictPartialOrder(nodes=[valuation_meeting, marketing_prep])
stage5 = StrictPartialOrder(nodes=[stage5_prep, final_approval])
stage5.order.add_edge(stage5_prep, final_approval)

# Root: sequence of all stages
root = StrictPartialOrder(nodes=[stage1, stage2, stage3, stage4, stage5])
root.order.add_edge(stage1, stage2)
root.order.add_edge(stage2, stage3)
root.order.add_edge(stage3, stage4)
root.order.add_edge(stage4, stage5)