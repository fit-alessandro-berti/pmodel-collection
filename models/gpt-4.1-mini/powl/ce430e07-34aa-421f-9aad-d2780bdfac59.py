# Generated from: ce430e07-34aa-421f-9aad-d2780bdfac59.json
# Description: This process details the dynamic adaptation of a global supply chain in response to an unexpected geopolitical crisis. It involves rapid risk assessment, alternative sourcing, logistics rerouting, stakeholder communication, compliance verification, and continuous monitoring to ensure minimal disruption. The process integrates cross-functional teams, leverages real-time data analytics, and incorporates contingency protocols to maintain operational continuity while managing cost and compliance risks. It requires iterative feedback loops and decision gates to adapt to evolving conditions and regulatory environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
Risk_Assess = Transition(label='Risk Assess')
Source_Alternatives = Transition(label='Source Alternatives')
Supplier_Audit = Transition(label='Supplier Audit')
Contract_Review = Transition(label='Contract Review')
Regulation_Check = Transition(label='Regulation Check')
Inventory_Scan = Transition(label='Inventory Scan')
Logistics_Reroute = Transition(label='Logistics Reroute')
Customs_Notify = Transition(label='Customs Notify')
Stakeholder_Alert = Transition(label='Stakeholder Alert')
Data_Analyze = Transition(label='Data Analyze')
Cost_Forecast = Transition(label='Cost Forecast')
Compliance_Verify = Transition(label='Compliance Verify')
Scenario_Plan = Transition(label='Scenario Plan')
Decision_Gate = Transition(label='Decision Gate')
Feedback_Loop = Transition(label='Feedback Loop')
Report_Generate = Transition(label='Report Generate')
Market_Monitor = Transition(label='Market Monitor')
Team_Sync = Transition(label='Team Sync')

# Modeling iterative feedback loops and decision gates with LOOP and XOR

# Feedback loop: execute Feedback_Loop then either exit or continue with FeedBack (dummy step place if needed)
# Here utilize LOOP operator: * (A, B) means execute A, then choose exit or (B then A again)
# Use Feedback_Loop as A, Decision_Gate as B to model iteration over decision gate and feedback

feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Loop, Decision_Gate])

# Decision Gate leads to choice of scenarios to adapt supply chain:
# After Decision_Gate loop, next steps are either Scenario_Plan OR Report_Generate (like a choice)
scenario_or_report = OperatorPOWL(operator=Operator.XOR, children=[Scenario_Plan, Report_Generate])

# Risk assessment precedes the alternative sourcing and audits and reviews (partial order)
preparation_PO = StrictPartialOrder(nodes=[Risk_Assess, Source_Alternatives, Supplier_Audit, Contract_Review])
preparation_PO.order.add_edge(Risk_Assess, Source_Alternatives)
preparation_PO.order.add_edge(Source_Alternatives, Supplier_Audit)
preparation_PO.order.add_edge(Supplier_Audit, Contract_Review)

# Compliance chain: Regulation_Check -> Inventory_Scan -> Compliance_Verify
compliance_PO = StrictPartialOrder(nodes=[Regulation_Check, Inventory_Scan, Compliance_Verify])
compliance_PO.order.add_edge(Regulation_Check, Inventory_Scan)
compliance_PO.order.add_edge(Inventory_Scan, Compliance_Verify)

# Logistics chain: Logistics_Reroute -> Customs_Notify
logistics_PO = StrictPartialOrder(nodes=[Logistics_Reroute, Customs_Notify])
logistics_PO.order.add_edge(Logistics_Reroute, Customs_Notify)

# Communication chain: Stakeholder_Alert -> Team_Sync -> Market_Monitor
communication_PO = StrictPartialOrder(nodes=[Stakeholder_Alert, Team_Sync, Market_Monitor])
communication_PO.order.add_edge(Stakeholder_Alert, Team_Sync)
communication_PO.order.add_edge(Team_Sync, Market_Monitor)

# Analytics subchain: Data_Analyze -> Cost_Forecast
analytics_PO = StrictPartialOrder(nodes=[Data_Analyze, Cost_Forecast])
analytics_PO.order.add_edge(Data_Analyze, Cost_Forecast)

# Combine all major concurrent blocks into a large PO with partial order edges where logical

# Central order edges:
# Contract_Review, Compliance_Verify, Market_Monitor, scenario_or_report and feedback_loop interact
# After Contract_Review, trigger compliance_PO (Regulation_Check) and analytics_PO(Data_Analyze) concurrently
# After analytics_PO and compliance_PO done, trigger communication_PO, logistics_PO, then feedback loop
# Finally, scenario_or_report after feedback loop

root = StrictPartialOrder(
    nodes=[
        preparation_PO,
        compliance_PO,
        logistics_PO,
        communication_PO,
        analytics_PO,
        feedback_loop,
        scenario_or_report
    ]
)

# Add edges for process flow across these components
root.order.add_edge(preparation_PO, compliance_PO)
root.order.add_edge(preparation_PO, analytics_PO)
root.order.add_edge(compliance_PO, communication_PO)
root.order.add_edge(analytics_PO, communication_PO)
root.order.add_edge(communication_PO, logistics_PO)
root.order.add_edge(logistics_PO, feedback_loop)
root.order.add_edge(feedback_loop, scenario_or_report)