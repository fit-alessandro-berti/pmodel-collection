# Generated from: aaf06c53-eed6-4925-a797-60779351089f.json
# Description: This process governs the dynamic reallocation of physical and digital assets across multiple departments within a multinational corporation. It involves continuous monitoring of asset utilization rates, predictive demand analytics, interdepartmental negotiation for resource sharing, compliance verification with local regulations, and real-time adjustment of asset distribution to optimize operational efficiency and reduce downtime. The process includes stakeholder approvals, risk assessments, and integration with enterprise resource planning (ERP) systems to ensure seamless tracking and reporting. Additionally, it incorporates contingency planning for unexpected asset failures and rapid redeployment strategies to maintain business continuity across global locations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
AssetAudit = Transition(label='Asset Audit')
UtilizationScan = Transition(label='Utilization Scan')
DemandForecast = Transition(label='Demand Forecast')
ComplianceCheck = Transition(label='Compliance Check')
StakeholderMeet = Transition(label='Stakeholder Meet')
RiskAssess = Transition(label='Risk Assess')
ApprovalRequest = Transition(label='Approval Request')
ResourceMatch = Transition(label='Resource Match')
TransferPlan = Transition(label='Transfer Plan')
LogisticsCoord = Transition(label='Logistics Coord')
SystemUpdate = Transition(label='System Update')
PerformanceTrack = Transition(label='Performance Track')
FailureDetect = Transition(label='Failure Detect')
ContingencyPrep = Transition(label='Contingency Prep')
RedeployAssets = Transition(label='Redeploy Assets')
ReportGenerate = Transition(label='Report Generate')

# Silent transition for skip or silent steps (if needed)
skip = SilentTransition()

# Loop node representing continuous monitoring + adjustment + contingency handling
# Loop(
#    A = StrictPartialOrder of monitoring & planning steps
#    B = contingency handling path
# )

# Define the monitoring and planning partial order (A):
# Asset Audit --> Utilization Scan & Demand Forecast (concurrent)
# These both lead to Compliance Check
# Followed by Stakeholder Meet --> Risk Assess --> Approval Request
# After approval: Resource Match --> Transfer Plan --> Logistics Coord
# Then System Update --> Performance Track
monitoring_nodes = [AssetAudit, UtilizationScan, DemandForecast, ComplianceCheck, StakeholderMeet,
                    RiskAssess, ApprovalRequest, ResourceMatch, TransferPlan,
                    LogisticsCoord, SystemUpdate, PerformanceTrack]
monitoring = StrictPartialOrder(nodes=monitoring_nodes)
# Order edges for A:

monitoring.order.add_edge(AssetAudit, UtilizationScan)
monitoring.order.add_edge(AssetAudit, DemandForecast)

monitoring.order.add_edge(UtilizationScan, ComplianceCheck)
monitoring.order.add_edge(DemandForecast, ComplianceCheck)

monitoring.order.add_edge(ComplianceCheck, StakeholderMeet)
monitoring.order.add_edge(StakeholderMeet, RiskAssess)
monitoring.order.add_edge(RiskAssess, ApprovalRequest)

monitoring.order.add_edge(ApprovalRequest, ResourceMatch)
monitoring.order.add_edge(ResourceMatch, TransferPlan)
monitoring.order.add_edge(TransferPlan, LogisticsCoord)

monitoring.order.add_edge(LogisticsCoord, SystemUpdate)
monitoring.order.add_edge(SystemUpdate, PerformanceTrack)

# Define contingency handling partial order (B):
# Failure Detect --> Contingency Prep --> Redeploy Assets
contingency_nodes = [FailureDetect, ContingencyPrep, RedeployAssets]
contingency = StrictPartialOrder(nodes=contingency_nodes)
contingency.order.add_edge(FailureDetect, ContingencyPrep)
contingency.order.add_edge(ContingencyPrep, RedeployAssets)

# Loop node combining monitoring and contingency
loop = OperatorPOWL(operator=Operator.LOOP, children=[monitoring, contingency])

# After loop, the process ends with Report Generate
# So a partial order of loop --> Report Generate
root_nodes = [loop, ReportGenerate]
root = StrictPartialOrder(nodes=root_nodes)
root.order.add_edge(loop, ReportGenerate)