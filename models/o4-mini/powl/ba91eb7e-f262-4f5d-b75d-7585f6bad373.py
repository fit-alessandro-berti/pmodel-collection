# Generated from: ba91eb7e-f262-4f5d-b75d-7585f6bad373.json
# Description: This process involves the detailed authentication and valuation of antique assets for high-end auction houses. It begins with provenance verification through historical records and expert interviews, followed by material composition analysis using advanced spectroscopy. The condition assessment involves microscopic imaging and restoration history review. Ethical sourcing checks are conducted to ensure no illicit trade connections. Concurrently, market trend analysis predicts asset value fluctuations. Legal compliance reviews historical ownership rights and export restrictions. The process culminates in a comprehensive report combining technical data and market insights, enabling informed auction decisions and risk mitigation for stakeholders.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities
pcheck = Transition(label='Provenance Check')
expert_interview = Transition(label='Expert Interview')
material_analysis = Transition(label='Material Analysis')
spectroscopy_scan = Transition(label='Spectroscopy Scan')
condition_review = Transition(label='Condition Review')
microscopic_imaging = Transition(label='Microscopic Imaging')
restoration_audit = Transition(label='Restoration Audit')
ethics_screening = Transition(label='Ethics Screening')
trade_verification = Transition(label='Trade Verification')
market_analysis = Transition(label='Market Analysis')
trend_forecast = Transition(label='Trend Forecast')
legal_review = Transition(label='Legal Review')
ownership_audit = Transition(label='Ownership Audit')
export_check = Transition(label='Export Check')
report_compilation = Transition(label='Report Compilation')
risk_assessment = Transition(label='Risk Assessment')

# Build the partial order
root = StrictPartialOrder(nodes=[
    pcheck, expert_interview,
    material_analysis, spectroscopy_scan,
    condition_review, microscopic_imaging, restoration_audit,
    ethics_screening, trade_verification,
    market_analysis, trend_forecast,
    legal_review, ownership_audit, export_check,
    report_compilation, risk_assessment
])

# Provenance verification
root.order.add_edge(pcheck, expert_interview)

# Material analysis
root.order.add_edge(expert_interview, material_analysis)
root.order.add_edge(material_analysis, spectroscopy_scan)

# Condition assessment (two parallel subtasks)
root.order.add_edge(spectroscopy_scan, condition_review)
root.order.add_edge(condition_review, microscopic_imaging)
root.order.add_edge(condition_review, restoration_audit)

# Ethical sourcing after both condition subtasks
root.order.add_edge(microscopic_imaging, ethics_screening)
root.order.add_edge(restoration_audit, ethics_screening)

# Market trend analysis concurrently after condition review
root.order.add_edge(condition_review, market_analysis)

# Legal compliance after ethics screening and market analysis
root.order.add_edge(ethics_screening, legal_review)
root.order.add_edge(market_analysis, legal_review)

# Legal subtasks
root.order.add_edge(legal_review, ownership_audit)
root.order.add_edge(legal_review, export_check)

# Report compilation after all compliance subtasks
root.order.add_edge(ownership_audit, report_compilation)
root.order.add_edge(export_check, report_compilation)

# Final risk assessment
root.order.add_edge(report_compilation, risk_assessment)