# Generated from: c9a2d8a4-7ea7-442a-aac9-20a0ba338751.json
# Description: This process involves conducting a comprehensive audit of multinational trade activities to ensure full compliance with dynamic international trade regulations, sanctions, and tariffs. It includes verifying supplier certifications, screening transactions against restricted party lists, harmonizing product classifications, and assessing risk exposure across jurisdictions. The audit requires cross-functional collaboration among legal, logistics, procurement, and finance teams, integrating automated data validation with manual inspections. The process culminates in generating detailed compliance reports, identifying remediation actions, and facilitating continuous monitoring to prevent violations and optimize trade efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
initiate_audit      = Transition(label='Initiate Audit')
gather_documents    = Transition(label='Gather Documents')
verify_suppliers    = Transition(label='Verify Suppliers')
screen_transactions = Transition(label='Screen Transactions')
classify_products   = Transition(label='Classify Products')
assess_risks        = Transition(label='Assess Risks')
check_sanctions     = Transition(label='Check Sanctions')
review_tariffs      = Transition(label='Review Tariffs')
cross_verify_data   = Transition(label='Cross-Verify Data')
conduct_interviews  = Transition(label='Conduct Interviews')
analyze_reports     = Transition(label='Analyze Reports')
identify_gaps       = Transition(label='Identify Gaps')
recommend_actions   = Transition(label='Recommend Actions')
implement_changes   = Transition(label='Implement Changes')
finalize_report     = Transition(label='Finalize Report')
monitor_compliance  = Transition(label='Monitor Compliance')

# Silent transition for optional branches
skip = SilentTransition()

# XOR choice: either Conduct Interviews or skip (automated only)
xor_inspection = OperatorPOWL(
    operator=Operator.XOR,
    children=[conduct_interviews, skip]
)

# LOOP for continuous monitoring: do Monitor Compliance, then either exit or skip->repeat
loop_monitoring = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_compliance, skip]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    initiate_audit, gather_documents,
    verify_suppliers, screen_transactions, classify_products, assess_risks,
    check_sanctions, review_tariffs,
    cross_verify_data, xor_inspection,
    analyze_reports,
    identify_gaps, recommend_actions, implement_changes,
    finalize_report,
    loop_monitoring
])

# Sequence: Initiate Audit -> Gather Documents
root.order.add_edge(initiate_audit, gather_documents)

# Parallel after gathering: supplier check, transaction screening, classification, risk, sanctions, tariffs
for t in [verify_suppliers, screen_transactions, classify_products,
          assess_risks, check_sanctions, review_tariffs]:
    root.order.add_edge(gather_documents, t)

# Synchronize all into Cross-Verify Data
for t in [verify_suppliers, screen_transactions, classify_products,
          assess_risks, check_sanctions, review_tariffs]:
    root.order.add_edge(t, cross_verify_data)

# After data validation, optional manual inspection
root.order.add_edge(cross_verify_data, xor_inspection)

# Then Analyze Reports
root.order.add_edge(xor_inspection, analyze_reports)

# Remediation steps
root.order.add_edge(analyze_reports, identify_gaps)
root.order.add_edge(identify_gaps, recommend_actions)
root.order.add_edge(recommend_actions, implement_changes)

# Final report
root.order.add_edge(implement_changes, finalize_report)

# Continuous monitoring loop
root.order.add_edge(finalize_report, loop_monitoring)