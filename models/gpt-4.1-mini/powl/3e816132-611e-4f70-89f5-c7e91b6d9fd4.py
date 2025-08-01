# Generated from: 3e816132-611e-4f70-89f5-c7e91b6d9fd4.json
# Description: This process involves leveraging quantum computing algorithms to dynamically allocate a diversified portfolio of assets in real-time. It integrates market sentiment analysis, probabilistic risk modeling, and quantum annealing to optimize investment decisions. The workflow starts with data ingestion from unconventional sources, followed by entanglement mapping of asset correlations. Adaptive rebalancing is triggered by quantum state changes, incorporating anomaly detection and feedback loops from predictive AI models. The process concludes with secure blockchain recording of transactions and compliance verification, ensuring transparency and auditability in a highly volatile and complex financial environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
DataIngest = Transition(label='Data Ingest')
SignalFilter = Transition(label='Signal Filter')
SentimentScan = Transition(label='Sentiment Scan')
RiskModel = Transition(label='Risk Model')
EntangleMap = Transition(label='Entangle Map')
QuantumCompute = Transition(label='Quantum Compute')
ProbabilisticSort = Transition(label='Probabilistic Sort')
AnomalyDetect = Transition(label='Anomaly Detect')
PortfolioWeigh = Transition(label='Portfolio Weigh')
RebalanceTrigger = Transition(label='Rebalance Trigger')
AIFeedback = Transition(label='AI Feedback')
TradeExecute = Transition(label='Trade Execute')
BlockchainLog = Transition(label='Blockchain Log')
ComplianceCheck = Transition(label='Compliance Check')
AuditTrail = Transition(label='Audit Trail')

skip = SilentTransition()

# Step 1: Data ingestion from unconventional sources
# Model DataIngest -> SignalFilter -> SentimentScan & RiskModel in parallel (probabilistic risk modeling happens with sentiment scan)

start_po = StrictPartialOrder(nodes=[DataIngest, SignalFilter, SentimentScan, RiskModel])
start_po.order.add_edge(DataIngest, SignalFilter)
start_po.order.add_edge(SignalFilter, SentimentScan)
start_po.order.add_edge(SignalFilter, RiskModel)  # RiskModel and SentimentScan parallel after SignalFilter

# Step 2: Entanglement mapping of asset correlations
entangle_part = EntangleMap

# Step 3: Quantum computing via QuantumCompute and ProbabilisticSort (probabilistic sorting)
quantum_part = StrictPartialOrder(nodes=[QuantumCompute, ProbabilisticSort])
quantum_part.order.add_edge(QuantumCompute, ProbabilisticSort)

# Step 4: Adaptive rebalancing triggered by quantum state changes: 
# Loop:
#   RebalanceTrigger
#   choice: exit or perform AnomalyDetect -> PortfolioWeigh -> feedback loop via AI Feedback -> loop back

# Subsequence inside loop body after RebalanceTrigger:
feedback_branch = StrictPartialOrder(nodes=[AnomalyDetect, PortfolioWeigh, AIFeedback])
feedback_branch.order.add_edge(AnomalyDetect, PortfolioWeigh)
feedback_branch.order.add_edge(PortfolioWeigh, AIFeedback)

loop_body = OperatorPOWL(operator=Operator.XOR, children=[skip, feedback_branch])  # choice: exit or feedback branch
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[RebalanceTrigger, loop_body])

# Step 5: After loop ends -> trade execute and recording steps concurrent
end_po = StrictPartialOrder(nodes=[TradeExecute, BlockchainLog])
# No order implies concurrency

# Compliance and Audit steps in sequence after above concurrent ones
compliance_sequence = StrictPartialOrder(nodes=[ComplianceCheck, AuditTrail])
compliance_sequence.order.add_edge(ComplianceCheck, AuditTrail)

# Connect end_po to compliance_sequence
end_full = StrictPartialOrder(
    nodes=[TradeExecute, BlockchainLog, ComplianceCheck, AuditTrail]
)
end_full.order.add_edge(TradeExecute, ComplianceCheck)
end_full.order.add_edge(BlockchainLog, ComplianceCheck)
end_full.order.add_edge(ComplianceCheck, AuditTrail)

# Aggregate main flow:
# start_po -> entangle_part -> quantum_part -> loop_node -> end_full

root = StrictPartialOrder(
    nodes=[start_po, entangle_part, quantum_part, loop_node, end_full]
)
root.order.add_edge(start_po, entangle_part)
root.order.add_edge(entangle_part, quantum_part)
root.order.add_edge(quantum_part, loop_node)
root.order.add_edge(loop_node, end_full)