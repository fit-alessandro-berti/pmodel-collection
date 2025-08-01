# Generated from: c9a2d8a4-7ea7-442a-aac9-20a0ba338751.json
# Description: This process involves conducting a comprehensive audit of multinational trade activities to ensure full compliance with dynamic international trade regulations, sanctions, and tariffs. It includes verifying supplier certifications, screening transactions against restricted party lists, harmonizing product classifications, and assessing risk exposure across jurisdictions. The audit requires cross-functional collaboration among legal, logistics, procurement, and finance teams, integrating automated data validation with manual inspections. The process culminates in generating detailed compliance reports, identifying remediation actions, and facilitating continuous monitoring to prevent violations and optimize trade efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Initiate_Audit = Transition(label='Initiate Audit')
Gather_Documents = Transition(label='Gather Documents')
Verify_Suppliers = Transition(label='Verify Suppliers')
Screen_Transactions = Transition(label='Screen Transactions')
Classify_Products = Transition(label='Classify Products')
Assess_Risks = Transition(label='Assess Risks')
Check_Sanctions = Transition(label='Check Sanctions')
Review_Tariffs = Transition(label='Review Tariffs')
Cross_Verify_Data = Transition(label='Cross-Verify Data')
Conduct_Interviews = Transition(label='Conduct Interviews')
Analyze_Reports = Transition(label='Analyze Reports')
Identify_Gaps = Transition(label='Identify Gaps')
Recommend_Actions = Transition(label='Recommend Actions')
Implement_Changes = Transition(label='Implement Changes')
Monitor_Compliance = Transition(label='Monitor Compliance')
Finalize_Report = Transition(label='Finalize Report')

# Partial order for the initial audit preparation and verification activities, partially concurrent
prep_and_verif = StrictPartialOrder(
    nodes=[Gather_Documents, Verify_Suppliers, Screen_Transactions, Classify_Products, Assess_Risks, Check_Sanctions, Review_Tariffs]
)
# Orders to enforce partial order - Gather first, then all verifications can proceed concurrent
prep_and_verif.order.add_edge(Gather_Documents, Verify_Suppliers)
prep_and_verif.order.add_edge(Gather_Documents, Screen_Transactions)
prep_and_verif.order.add_edge(Gather_Documents, Classify_Products)
prep_and_verif.order.add_edge(Gather_Documents, Assess_Risks)
prep_and_verif.order.add_edge(Gather_Documents, Check_Sanctions)
prep_and_verif.order.add_edge(Gather_Documents, Review_Tariffs)

# Cross-functional collaboration block: Cross-Verify Data and Conduct Interviews run in parallel after verifications
cross_collab = StrictPartialOrder(
    nodes=[Cross_Verify_Data, Conduct_Interviews]
)
# No order edge => fully concurrent

# Analysis and reporting block in sequence
analysis_report = StrictPartialOrder(
    nodes=[Analyze_Reports, Identify_Gaps, Recommend_Actions, Implement_Changes, Monitor_Compliance, Finalize_Report]
)
analysis_report.order.add_edge(Analyze_Reports, Identify_Gaps)
analysis_report.order.add_edge(Identify_Gaps, Recommend_Actions)
analysis_report.order.add_edge(Recommend_Actions, Implement_Changes)
analysis_report.order.add_edge(Implement_Changes, Monitor_Compliance)
analysis_report.order.add_edge(Monitor_Compliance, Finalize_Report)

# Build the main PO with all parts
root = StrictPartialOrder(
    nodes=[
        Initiate_Audit,
        prep_and_verif,
        cross_collab,
        analysis_report
    ]
)

# Define control flow order edges among these top-level nodes

# Start with Initiate Audit
root.order.add_edge(Initiate_Audit, prep_and_verif)
# After preparation and verification, cross-functional collaboration runs
root.order.add_edge(prep_and_verif, cross_collab)
# After collaboration, analysis and reporting proceed
root.order.add_edge(cross_collab, analysis_report)