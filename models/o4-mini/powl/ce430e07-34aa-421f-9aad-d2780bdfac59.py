# Generated from: ce430e07-34aa-421f-9aad-d2780bdfac59.json
# Description: This process details the dynamic adaptation of a global supply chain in response to an unexpected geopolitical crisis. It involves rapid risk assessment, alternative sourcing, logistics rerouting, stakeholder communication, compliance verification, and continuous monitoring to ensure minimal disruption. The process integrates cross-functional teams, leverages real-time data analytics, and incorporates contingency protocols to maintain operational continuity while managing cost and compliance risks. It requires iterative feedback loops and decision gates to adapt to evolving conditions and regulatory environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL Transitions
risk_assess        = Transition(label='Risk Assess')
source_alternatives= Transition(label='Source Alternatives')
supplier_audit     = Transition(label='Supplier Audit')
contract_review    = Transition(label='Contract Review')
regulation_check   = Transition(label='Regulation Check')
inventory_scan     = Transition(label='Inventory Scan')
logistics_reroute  = Transition(label='Logistics Reroute')
customs_notify     = Transition(label='Customs Notify')
stakeholder_alert  = Transition(label='Stakeholder Alert')
data_analyze       = Transition(label='Data Analyze')
cost_forecast      = Transition(label='Cost Forecast')
compliance_verify  = Transition(label='Compliance Verify')
scenario_plan      = Transition(label='Scenario Plan')
decision_gate      = Transition(label='Decision Gate')
feedback_loop      = Transition(label='Feedback Loop')
report_generate    = Transition(label='Report Generate')
market_monitor     = Transition(label='Market Monitor')
team_sync          = Transition(label='Team Sync')

# Build the loop: first child is (Scenario Plan -> Decision Gate),
# second child is the redo sequence (Feedback Loop -> Report Generate -> Market Monitor -> Team Sync)
seq_A = StrictPartialOrder(nodes=[scenario_plan, decision_gate])
seq_A.order.add_edge(scenario_plan, decision_gate)

seq_B = StrictPartialOrder(nodes=[feedback_loop, report_generate, market_monitor, team_sync])
seq_B.order.add_edge(feedback_loop, report_generate)
seq_B.order.add_edge(report_generate, market_monitor)
seq_B.order.add_edge(market_monitor, team_sync)

loop = OperatorPOWL(operator=Operator.LOOP, children=[seq_A, seq_B])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    risk_assess,
    source_alternatives,
    supplier_audit,
    contract_review,
    regulation_check,
    inventory_scan,
    logistics_reroute,
    customs_notify,
    stakeholder_alert,
    data_analyze,
    cost_forecast,
    compliance_verify,
    loop
])

# Define the main linear sequence up to inventory scan
root.order.add_edge(risk_assess, source_alternatives)
root.order.add_edge(source_alternatives, supplier_audit)
root.order.add_edge(supplier_audit, contract_review)
root.order.add_edge(contract_review, regulation_check)
root.order.add_edge(regulation_check, inventory_scan)

# After inventory scan, three activities can run in parallel
root.order.add_edge(inventory_scan, logistics_reroute)
root.order.add_edge(inventory_scan, customs_notify)
root.order.add_edge(inventory_scan, stakeholder_alert)

# Those three feed into the analytics sub‐process
for prior in (logistics_reroute, customs_notify, stakeholder_alert):
    root.order.add_edge(prior, data_analyze)
    root.order.add_edge(prior, cost_forecast)
    root.order.add_edge(prior, compliance_verify)

# After analytics, enter the adaptation loop
root.order.add_edge(data_analyze, loop)
root.order.add_edge(cost_forecast, loop)
root.order.add_edge(compliance_verify, loop)