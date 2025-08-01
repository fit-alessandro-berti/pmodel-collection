# Generated from: d9d05537-ff8f-4fad-90e0-0b71bae8c9cd.json
# Description: This process involves managing an organization’s response to an unexpected crisis that impacts operations, reputation, and stakeholder trust. It includes rapid assessment, resource mobilization, communication strategies, legal compliance checks, and iterative recovery efforts. The process integrates cross-functional teams, external agencies, and continuous monitoring to adapt dynamically. Activities range from initial alert verification to post-crisis evaluation, ensuring resilience and minimizing damage while maintaining transparency and accountability throughout the response lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
AlertVerify      = Transition(label='Alert Verify')
ImpactAssess     = Transition(label='Impact Assess')
TeamAssemble     = Transition(label='Team Assemble')
ResourceAllocate = Transition(label='Resource Allocate')
StakeholderNotify= Transition(label='Stakeholder Notify')
LegalReview      = Transition(label='Legal Review')
MediaBrief       = Transition(label='Media Brief')
ResponseDeploy   = Transition(label='Response Deploy')
SituationMonitor = Transition(label='Situation Monitor')
DataCollect      = Transition(label='Data Collect')
RiskMitigate     = Transition(label='Risk Mitigate')
RecoveryPlan     = Transition(label='Recovery Plan')
ExternalConsult  = Transition(label='External Consult')
StatusUpdate     = Transition(label='Status Update')
PostReview       = Transition(label='Post Review')

# 1. Initial sequential assessment and mobilization
initial = StrictPartialOrder(nodes=[AlertVerify, ImpactAssess, TeamAssemble, ResourceAllocate])
initial.order.add_edge(AlertVerify, ImpactAssess)
initial.order.add_edge(ImpactAssess, TeamAssemble)
initial.order.add_edge(TeamAssemble, ResourceAllocate)

# 2. Parallel notification and compliance checks
notifications = StrictPartialOrder(nodes=[StakeholderNotify, LegalReview, MediaBrief])
# (no edges → they can run concurrently)

# 3. Monitoring and data collection sub‐process
monitor_collect = StrictPartialOrder(nodes=[SituationMonitor, DataCollect])
monitor_collect.order.add_edge(SituationMonitor, DataCollect)

# 4. Recovery iteration sequence
recovery_seq = StrictPartialOrder(nodes=[RiskMitigate, RecoveryPlan, ExternalConsult, StatusUpdate])
recovery_seq.order.add_edge(RiskMitigate,    RecoveryPlan)
recovery_seq.order.add_edge(RecoveryPlan,    ExternalConsult)
recovery_seq.order.add_edge(ExternalConsult, StatusUpdate)

# 5. Loop: monitor/collect then recovery efforts repeatedly until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_collect, recovery_seq])

# 6. Root partial order combining everything
root = StrictPartialOrder(nodes=[initial, notifications, ResponseDeploy, loop, PostReview])
root.order.add_edge(initial,       notifications)
root.order.add_edge(notifications, ResponseDeploy)
root.order.add_edge(ResponseDeploy, loop)
root.order.add_edge(loop,          PostReview)