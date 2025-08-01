# Generated from: fa8c0802-8b9d-4a67-9d07-38b28904557a.json
# Description: This process involves dynamically adjusting supply chain parameters in response to real-time environmental, economic, and social data inputs. It begins with continuous sensor data aggregation followed by anomaly detection, supplier risk assessment, and predictive demand modeling. The process incorporates stakeholder feedback loops and automated negotiation protocols with suppliers to optimize inventory levels. Risk mitigation strategies are deployed through contingency resource allocation. Final calibration includes sustainability impact scoring and compliance verification before executing adaptive distribution scheduling to ensure resilience and efficiency under fluctuating global conditions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Data_Aggregation = Transition(label='Data Aggregation')
Anomaly_Detect = Transition(label='Anomaly Detect')
Risk_Assess = Transition(label='Risk Assess')
Demand_Model = Transition(label='Demand Model')
Stakeholder_Sync = Transition(label='Stakeholder Sync')
Auto_Negotiate = Transition(label='Auto Negotiate')
Inventory_Optimize = Transition(label='Inventory Optimize')
Contingency_Plan = Transition(label='Contingency Plan')
Resource_Allocate = Transition(label='Resource Allocate')
Sustainability_Check = Transition(label='Sustainability Check')
Compliance_Verify = Transition(label='Compliance Verify')
Impact_Score = Transition(label='Impact Score')
Distribution_Plan = Transition(label='Distribution Plan')
Feedback_Loop = Transition(label='Feedback Loop')
Performance_Audit = Transition(label='Performance Audit')
Schedule_Execute = Transition(label='Schedule Execute')

# Build feedback loop: Stakeholder Sync and Performance Audit loop with Feedback Loop 
# Loop node: execute Stakeholder Sync and Performance Audit, then choose to exit or execute Feedback Loop then repeat
stakeholder_audit = StrictPartialOrder(nodes=[Stakeholder_Sync, Performance_Audit])
stakeholder_audit.order.add_edge(Stakeholder_Sync, Performance_Audit)

feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_audit, Feedback_Loop])

# Automated negotiation and inventory optimize partial order
auto_inv = StrictPartialOrder(nodes=[Auto_Negotiate, Inventory_Optimize])
auto_inv.order.add_edge(Auto_Negotiate, Inventory_Optimize)

# Contingency through resource allocate partial order
contingency = StrictPartialOrder(nodes=[Contingency_Plan, Resource_Allocate])
contingency.order.add_edge(Contingency_Plan, Resource_Allocate)

# Final calibration sequence: Impact Score -> Sustainability Check -> Compliance Verify
final_calibration = StrictPartialOrder(nodes=[Impact_Score, Sustainability_Check, Compliance_Verify])
final_calibration.order.add_edge(Impact_Score, Sustainability_Check)
final_calibration.order.add_edge(Sustainability_Check, Compliance_Verify)

# Distribution plan and schedule execute partial order
distribution = StrictPartialOrder(nodes=[Distribution_Plan, Schedule_Execute])
distribution.order.add_edge(Distribution_Plan, Schedule_Execute)

# Core sequence before feedback loop and negotiations:
# Data Aggregation -> Anomaly Detect -> Risk Assess -> Demand Model
core_sequence = StrictPartialOrder(nodes=[Data_Aggregation, Anomaly_Detect, Risk_Assess, Demand_Model])
core_sequence.order.add_edge(Data_Aggregation, Anomaly_Detect)
core_sequence.order.add_edge(Anomaly_Detect, Risk_Assess)
core_sequence.order.add_edge(Risk_Assess, Demand_Model)

# Combine multiple flows:
# From Demand Model:
# 1) to feedback_loop
# 2) to auto_inv
# 3) to contingency
# These three run concurrently after Demand Model

# Create a PO including core_sequence nodes plus feedback_loop, auto_inv, contingency
root = StrictPartialOrder(
    nodes=[core_sequence, feedback_loop, auto_inv, contingency, final_calibration, distribution]
)

# Order edges for core sequence inside root
root.order.add_edge(core_sequence, feedback_loop)
root.order.add_edge(core_sequence, auto_inv)
root.order.add_edge(core_sequence, contingency)

# After feedback_loop, auto_inv and contingency, all converge to final_calibration
root.order.add_edge(feedback_loop, final_calibration)
root.order.add_edge(auto_inv, final_calibration)
root.order.add_edge(contingency, final_calibration)

# After final_calibration, order to distribution
root.order.add_edge(final_calibration, distribution)