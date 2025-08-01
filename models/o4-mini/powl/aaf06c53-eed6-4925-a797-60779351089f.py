# Generated from: aaf06c53-eed6-4925-a797-60779351089f.json
# Description: This process governs the dynamic reallocation of physical and digital assets across multiple departments within a multinational corporation. It involves continuous monitoring of asset utilization rates, predictive demand analytics, interdepartmental negotiation for resource sharing, compliance verification with local regulations, and real-time adjustment of asset distribution to optimize operational efficiency and reduce downtime. The process includes stakeholder approvals, risk assessments, and integration with enterprise resource planning (ERP) systems to ensure seamless tracking and reporting. Additionally, it incorporates contingency planning for unexpected asset failures and rapid redeployment strategies to maintain business continuity across global locations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
asset_audit = Transition(label='Asset Audit')
util_scan = Transition(label='Utilization Scan')
demand_forecast = Transition(label='Demand Forecast')
compliance_check = Transition(label='Compliance Check')
stakeholder_meet = Transition(label='Stakeholder Meet')
risk_assess = Transition(label='Risk Assess')
approval_request = Transition(label='Approval Request')
resource_match = Transition(label='Resource Match')
transfer_plan = Transition(label='Transfer Plan')
logistics_coord = Transition(label='Logistics Coord')
system_update_A = Transition(label='System Update')
performance_track = Transition(label='Performance Track')
report_generate = Transition(label='Report Generate')

failure_detect = Transition(label='Failure Detect')
contingency_prep = Transition(label='Contingency Prep')
redeploy_assets = Transition(label='Redeploy Assets')
system_update_B = Transition(label='System Update')

# Core cycle A: monitoring, forecasting, compliance, negotiation, approval, execution, update, tracking, reporting
A = StrictPartialOrder(nodes=[
    util_scan,
    demand_forecast,
    compliance_check,
    stakeholder_meet,
    risk_assess,
    approval_request,
    resource_match,
    transfer_plan,
    logistics_coord,
    system_update_A,
    performance_track,
    report_generate
])
A.order.add_edge(util_scan, demand_forecast)
A.order.add_edge(demand_forecast, compliance_check)
A.order.add_edge(compliance_check, stakeholder_meet)
A.order.add_edge(stakeholder_meet, risk_assess)
A.order.add_edge(risk_assess, approval_request)
A.order.add_edge(approval_request, resource_match)
A.order.add_edge(resource_match, transfer_plan)
A.order.add_edge(transfer_plan, logistics_coord)
A.order.add_edge(logistics_coord, system_update_A)
A.order.add_edge(system_update_A, performance_track)
A.order.add_edge(performance_track, report_generate)

# Contingency branch B: failure detection and rapid redeployment
B = StrictPartialOrder(nodes=[
    failure_detect,
    contingency_prep,
    redeploy_assets,
    system_update_B
])
B.order.add_edge(failure_detect, contingency_prep)
B.order.add_edge(contingency_prep, redeploy_assets)
B.order.add_edge(redeploy_assets, system_update_B)

# Loop: run A, then either exit or do B then repeat A
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Entire process: initial audit then continuous loop
root = StrictPartialOrder(nodes=[asset_audit, loop])
root.order.add_edge(asset_audit, loop)