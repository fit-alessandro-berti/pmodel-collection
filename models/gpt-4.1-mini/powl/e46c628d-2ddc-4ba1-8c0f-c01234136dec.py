# Generated from: e46c628d-2ddc-4ba1-8c0f-c01234136dec.json
# Description: This process involves the rapid mobilization and coordination of multiple agencies and resources to manage unforeseen emergency situations such as natural disasters, industrial accidents, or security threats. It includes initial threat assessment, resource allocation, communication synchronization, public information dissemination, and post-event analysis to improve future responsiveness. Stakeholders must work under high pressure with dynamic priorities, ensuring safety, compliance, and efficient recovery while adapting to evolving conditions on the ground. The process integrates technology, field operations, and strategic decision-making to mitigate impact effectively.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
ThreatAssess = Transition(label='Threat Assess')
AlertDispatch = Transition(label='Alert Dispatch')
ResourceCheck = Transition(label='Resource Check')
TeamMobilize = Transition(label='Team Mobilize')
CommandSetup = Transition(label='Command Setup')
IntelGather = Transition(label='Intel Gather')
RiskEvaluate = Transition(label='Risk Evaluate')
PrioritySet = Transition(label='Priority Set')
FieldDeploy = Transition(label='Field Deploy')
CommSync = Transition(label='Comm Sync')
PublicUpdate = Transition(label='Public Update')
SupplyManage = Transition(label='Supply Manage')
SafetyMonitor = Transition(label='Safety Monitor')
IncidentLog = Transition(label='Incident Log')
RecoveryPlan = Transition(label='Recovery Plan')
DebriefTeam = Transition(label='Debrief Team')
DataArchive = Transition(label='Data Archive')

# Model 1: Initial threat assessment and resource allocation partial order
po_initial = StrictPartialOrder(nodes=[ThreatAssess, AlertDispatch, ResourceCheck])
po_initial.order.add_edge(ThreatAssess, AlertDispatch)
po_initial.order.add_edge(ThreatAssess, ResourceCheck)

# Model 2: Mobilization and command setup partial order after resource check
po_mobilize = StrictPartialOrder(nodes=[TeamMobilize, CommandSetup])
po_mobilize.order.add_edge(TeamMobilize, CommandSetup)

# Model 3: Intelligence, risk and priority partial order - can be done concurrently
po_intel_risk_priority = StrictPartialOrder(nodes=[IntelGather, RiskEvaluate, PrioritySet])

# Model 4: Field deploy depends on mobilize, command setup, intel, risk and priority evaluation
# We model the partial order to combine mobilization and intelligence nodes before FieldDeploy
po_field_prep = StrictPartialOrder(
    nodes=[po_mobilize, po_intel_risk_priority, FieldDeploy]
)
# mobilize -> field deploy
po_field_prep.order.add_edge(po_mobilize, FieldDeploy)
# intel_risk_priority -> field deploy
po_field_prep.order.add_edge(po_intel_risk_priority, FieldDeploy)

# Model 5: Communication sync and public update are concurrent after field deploy
po_comm_public = StrictPartialOrder(nodes=[CommSync, PublicUpdate])

# Model 6: Supply management and safety monitoring concurrent after comm and public update
po_supply_safety = StrictPartialOrder(nodes=[SupplyManage, SafetyMonitor])

# Connect communication/public update and supply/safety monitoring partial orders
po_comm_public_supply_safety = StrictPartialOrder(
    nodes=[po_comm_public, po_supply_safety]
)
po_comm_public_supply_safety.order.add_edge(po_comm_public, po_supply_safety)

# Model 7: Incident logging after supply and safety monitoring
po_log = StrictPartialOrder(nodes=[IncidentLog])
# Connect po_supply_safety -> IncidentLog
po_log_full = StrictPartialOrder(
    nodes=[po_comm_public_supply_safety, IncidentLog]
)
po_log_full.order.add_edge(po_comm_public_supply_safety, IncidentLog)

# Model 8: Recovery plan after incident log
po_recovery = StrictPartialOrder(nodes=[IncidentLog, RecoveryPlan])
po_recovery.order.add_edge(IncidentLog, RecoveryPlan)

# Model 9: Debrief team after recovery plan
po_debrief = StrictPartialOrder(nodes=[RecoveryPlan, DebriefTeam])
po_debrief.order.add_edge(RecoveryPlan, DebriefTeam)

# Model 10: Data archive after debrief team
po_archive = StrictPartialOrder(nodes=[DebriefTeam, DataArchive])
po_archive.order.add_edge(DebriefTeam, DataArchive)

# Combine all major parts into one top-level partial order:
# Start with initial -> mobilize -> field prep -> comm/public -> supply/safety -> log -> recovery -> debrief -> archive

root = StrictPartialOrder(
    nodes=[
        po_initial,
        po_mobilize,
        po_intel_risk_priority,
        FieldDeploy,
        po_comm_public,
        po_supply_safety,
        IncidentLog,
        RecoveryPlan,
        DebriefTeam,
        DataArchive
    ]
)

# order edges connecting the major phases:

# initial -> mobilize (mobilization depends on resources checked etc)
root.order.add_edge(po_initial, po_mobilize)
# initial -> intel_risk_priority (can begin once threat assessed)
root.order.add_edge(po_initial, po_intel_risk_priority)

# mobilize -> FieldDeploy
root.order.add_edge(po_mobilize, FieldDeploy)
# intel_risk_priority -> FieldDeploy
root.order.add_edge(po_intel_risk_priority, FieldDeploy)

# FieldDeploy -> CommSync & PublicUpdate (po_comm_public)
root.order.add_edge(FieldDeploy, po_comm_public)

# po_comm_public -> supply and safety
root.order.add_edge(po_comm_public, po_supply_safety)

# supply_safety -> IncidentLog
root.order.add_edge(po_supply_safety, IncidentLog)

# IncidentLog -> RecoveryPlan
root.order.add_edge(IncidentLog, RecoveryPlan)

# RecoveryPlan -> DebriefTeam
root.order.add_edge(RecoveryPlan, DebriefTeam)

# DebriefTeam -> DataArchive
root.order.add_edge(DebriefTeam, DataArchive)